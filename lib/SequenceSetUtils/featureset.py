import logging

from installed_clients.WorkspaceClient import Workspace
from installed_clients.DataFileUtilClient import DataFileUtil
from installed_clients.AssemblyUtilClient import AssemblyUtil

class featuresetutil:
    def __init__(self, callback, config):
        self.dfu = DataFileUtil(callback)
        self.wsc = Workspace(config['workspace-url'])
        self.asu = AssemblyUtil(callback)
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
        self.assembly = subset[0]['data']['assembly_ref']
        exit(self.assembly)
        self.asu.get_assembly_as_fasta(self.assembly)

        self.genomefeatures = subset[0]['data']['features']

        return subset[0]['data']['features']

    def makeSequenceSet(self, params):
        if 'seqsetname' not in params or params['seqsetname'] is '':
            self.objname = 'SequenceSet' + 'SequenceSet' + \
                      str(int((datetime.utcnow() - datetime.utcfromtimestamp(0)).total_seconds() * 1000))
        else:
            self.objname = params['seqsetname']

        self.sequenceset['sequence_set_id'] = self.objname
        self.sequenceset['description'] = 'SequenceSet built from the ' + str(params['upstream_length']) + \
                                          ' FeatureSet ' + params['FeatureSetRef']
        self.sequenceset['sequences'] = []

        exit(self.features['elements'])


