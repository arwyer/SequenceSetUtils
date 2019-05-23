import logging
import os
from datetime import datetime
from Bio import SeqIO

from installed_clients.WorkspaceClient import Workspace
from installed_clients.DataFileUtilClient import DataFileUtil
from installed_clients.AssemblyUtilClient import AssemblyUtil


def strstandard(dirtystr):
    return str(dirtystr).strip().upper()


class FeatureSetUtil:
    def __init__(self, callback, config):
        self.dfu = DataFileUtil(callback)
        self.wsc = Workspace(config['workspace-url'])
        self.asu = AssemblyUtil(callback)
        self.scratch = config['scratch']
        self.sequenceset = {}
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)

    def getFeatureSet(self, ref):
        self.features = self.dfu.get_objects({
            'object_refs': [ref]
        })['data'][0]['data']

        return self.features

    def getGenomeData(self, genomeref):
        self.genome = genomeref

        logging.info('Downloading genome feature data...\n')
        subset = self.wsc.get_object_subset([{
            'included': ['/features/[*]/location', '/features/[*]/id', '/assembly_ref'],
            'ref': genomeref
        }])

        logging.info('Downloading assembly fasta data...\n')
        self.assembly_ref = subset[0]['data']['assembly_ref']
        # For testing purposes we use a predestined file path
        self.assembly_path = os.path.join(self.scratch, 'assembly.fasta')
        assem = self.asu.get_assembly_as_fasta({'ref': self.assembly_ref, 'filename': self.assembly_path})

        # Static definition for testing purposes
        # assem = {
        #     'path': '/kb/module/test/sample_data/assembly.fasta',
        #     'assembly_name': 'CsubellipsoideaC169_v2.0.assembly'
        # }

        self.assembly_path = assem['path']
        self.assembly_name = assem['assembly_name']

        self.genomefeatures = subset[0]['data']['features']

        return subset[0]['data']['features']

    def makeSequenceSet(self, params):
        if 'seqsetname' not in params or params['seqsetname'] is '':
            self.objname = 'SequenceSet' + \
                      str(int((datetime.utcnow() - datetime.utcfromtimestamp(0)).total_seconds() * 1000))
        else:
            self.objname = params['seqsetname']

        self.sequenceset['sequence_set_id'] = self.objname
        self.sequenceset['description'] = 'SequenceSet built from the ' + str(params['upstream_length']) + \
                                          'upstream sequence of the features in the ' + \
                                          'FeatureSet (' + params['FeatureSet_ref']+ ')'
        self.sequenceset['sequences'] = []

        feature_ids_to_query = self.features['elements'].keys()
        found_features_in_genome = []

        # extract subset feature information from entire genome
        for feature in self.genomefeatures:
            if feature['id'] in feature_ids_to_query:
                found_features_in_genome.append(feature)

        # extract information about a subset of features
        found_features_locations = []
        found_features_contigs = []
        for feature in found_features_in_genome:
            found_features_locations.append(feature['location'][0])
            found_features_contigs.append(feature['location'][0][0])

        found_features_contigs = list(set(found_features_contigs))

        for record in SeqIO.parse(self.assembly_path, 'fasta'):
            if record.id in found_features_contigs:
                for location in found_features_locations:
                    if strstandard(record.id) == strstandard(location[0]):
                        sequence, source = {}, {}
                        source['assembly_id'] = self.assembly_ref
                        source['location'] = []

                        for feature in found_features_in_genome:
                            if feature['location'][0] == location:
                                sequence['sequence_id'] = feature['location'][0][0]
                                sequence['description'] = str(feature['location'][0])
                                break

                        if location[2] == "+":
                            end = location[1]

                            if (location[1] - params['upstream_length']) < 0:
                                start = 0
                            else:
                                start = location[1] - params['upstream_length']

                            promoter = record.seq[start:end].upper()
                        elif location[2] == "-":
                            start = location[1]

                            if (location[1] + params['upstream_length']) > len(record.seq) - 1:
                                end = len(record.seq) - 1
                            else:
                                end = location[1] + params['upstream_length']

                            promoter = record.seq[start:end].upper()
                            complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
                            promoter = ''.join([complement[base] for base in promoter[::-1]])
                        else:
                            raise ValueError('Location orientation not - or +: ' + str(location))

                        source['location'].append((location[0], start, '+', end))
                        sequence['sequence'] = str(promoter)
                        sequence['source'] = source

                        self.sequenceset['sequences'].append(sequence)
                    else:
                        continue
            else:
                continue
        return self.sequenceset

    def saveSequenceSet(self, seqset, params):
        if not self.objname:
            if 'seqsetname' not in params or params['seqsetname'] is '':
                self.objname = 'SequenceSet' + 'SequenceSet' + \
                          str(int((datetime.utcnow() - datetime.utcfromtimestamp(0)).total_seconds() * 1000))
            else:
                self.objname = params['seqsetname']

        ss = {
            'id': self.dfu.ws_name_to_id(params['ws_name']),
            'objects': [{
                'type': 'KBaseSequences.SequenceSet',
                'data': seqset,
                'name': self.objname
            }]
        }

        save = self.dfu.save_objects(ss)[0]
        return str(save[6]) + '/' + str(save[0]) + '/' + str(save[4])
