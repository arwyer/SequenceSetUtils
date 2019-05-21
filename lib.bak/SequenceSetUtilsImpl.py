# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
import json
from Bio import SeqIO
from AssemblyUtil.AssemblyUtilClient import AssemblyUtil

from biokbase.workspace.client import Workspace

#END_HEADER


class SequenceSetUtils:
    '''
    Module Name:
    SequenceSetUtils

    Module Description:
    A KBase module: SequenceSetUtils
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/arwyer/SequenceSetUtils.git"
    GIT_COMMIT_HASH = "dd7a7b6c2663be904ff9709487ad0ca0b1dcbbfe"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        self.fastautil =
        #END_CONSTRUCTOR
        pass


    def buildFromFasta(self, ctx, params):
        """
        :param params: instance of type "FastaInputParams" (ws_name -
           workspace name path - path to fasta in the workspace) ->
           structure: parameter "ws_name" of String, parameter "path" of
           String
        :returns: instance of type "SequenceSetOutputParams" (SequenceSet_ref
           - handle to the new SequenceSet object) -> structure: parameter
           "SequenceSet_ref" of String
        """
        # ctx is the context object
        # return variables are: out
        #BEGIN buildFromFasta
        dfu = DataFileUtil(self.callback_url)
        SequenceSet = {}
        objname = 'SequenceSet' + str(int((datetime.utcnow() - datetime.utcfromtimestamp(0)).total_seconds()*1000))
        SequenceSet['sequence_set_id'] = objname
        SequenceSet['description'] = 'SequenceSet built from ' + params['path']
        SequenceSet['sequences'] = []
        fastaFile = open(params['path'],'r')
        Sequence = {}
        for line in fastaFile:
            if '>' in line:
                Sequence = {}
                Sequence['sequence_id'] = line.replace('\n','').replace('>','')
                Sequence['description'] = line.replace('\n','').replace('>','')
                Sequence['source'] = {'location':[],'assembly_id':''}
            else:
                Sequence['sequence'] = line.replace('\n','')
                SequenceSet['sequences'].append(Sequence)
        save_objects_params = {}
        save_objects_params['id'] = dfu.ws_name_to_id(params['ws_name'])
        save_objects_params['objects'] = [{'type': 'KBaseSequences.SequenceSet','data':SequenceSet,'name':objname}]
        info = dfu.save_objects(save_objects_params)[0]
        ref = "%s/%s/%s" % (info[6],info[0],info[4])
        out = {'SequenceSet_ref':ref}
        #END buildFromFasta

        # At some point might do deeper type checking...
        if not isinstance(out, dict):
            raise ValueError('Method buildFromFasta return value ' +
                             'out is not type dict as required.')
        # return the results
        return [out]

    def buildFromLocations(self, ctx, params):
        """
        :param params: instance of type "LocationInputParams" (ws_name -
           workspace name seqlocations - list of sequence locations) ->
           structure: parameter "ws_name" of String, parameter "seqlocations"
           of list of type "sequence_location" (genome_ref - handle to genome
           genlocations - list of locations in the genome to build a single
           sequence from, usually length 1) -> structure: parameter
           "genome_ref" of String, parameter "genlocations" of list of tuple
           of size 4: type "Contig_id" (Insert your typespec information
           here.), Long, type "orientation", Long
        :returns: instance of type "SequenceSetOutputParams" (SequenceSet_ref
           - handle to the new SequenceSet object) -> structure: parameter
           "SequenceSet_ref" of String
        """
        # ctx is the context object
        # return variables are: out
        #BEGIN buildFromLocations
        #question about best practices here:
        #dont want to redownload genome every time?
        sortedSeq = sorted(params['seqlocations'], key=lambda k: k['genome_ref'])
        SeqSet = {}
        #for seq in param['seqlocations']:
            #Download this
            #seq['genome_ref']
            #for loc in params['genlocations']:
                #extract the sequence

        #END buildFromLocations

        # At some point might do deeper type checking...
        if not isinstance(out, dict):
            raise ValueError('Method buildFromLocations return value ' +
                             'out is not type dict as required.')
        # return the results
        return [out]

    def buildFromFeatureSet(self, ctx, params):
        """
        :param params: instance of type "FeatureSetInputParams" (ws_name -
           workspace name FeatureSet_ref - handle to input feature set
           genome_ref - handle to genome to extract features from
           upstream_length - length of region upstream of features to extract
           sequences from) -> structure: parameter "ws_name" of String,
           parameter "FeatureSet_ref" of String, parameter "genome_ref" of
           String, parameter "upstream_length" of Long
        :returns: instance of type "SequenceSetOutputParams" (SequenceSet_ref
           - handle to the new SequenceSet object) -> structure: parameter
           "SequenceSet_ref" of String
        """
        # ctx is the context object
        # return variables are: out
        #BEGIN buildFromFeatureSet

        #Get the featureset and assembly to extract sequences from
        dfu = DataFileUtil(self.callback_url)
        objectRefs = {'object_refs' : [params['FeatureSet_ref']]}
        objects = dfu.get_objects(objectRefs)

        ws = Workspace('https://appdev.kbase.us/services/ws')
        ws_name = params['ws_name']
        subset = ws.get_object_subset([{
                                     'included':['/features/[*]/location', '/features/[*]/id','/assembly_ref'],
'ref':params['genome_ref']}])
        features = subset[0]['data']['features']
        aref = subset[0]['data']['assembly_ref']
 featureSet = objects['data'][0]['data']
        assembly_ref = {'ref': aref}
        print('Downloading Assembly data as a Fasta file.')
        assemblyUtil = AssemblyUtil(self.callback_url)
        fasta_file = assemblyUtil.get_assembly_as_fasta(assembly_ref)






        #TODO:
        #Instead of extracting promoters as strings
        #extract as sequence
        #build sequence set object
        #upload it
        #return!
        SequenceSet = {}
        objname = 'SequenceSet' + str(int((datetime.utcnow() - datetime.utcfromtimestamp(0)).total_seconds()*1000))
        SequenceSet['sequence_set_id'] = objname
        SequenceSet['description'] = 'SequenceSet built from ' + params['FeatureSet_ref'] + ' with length ' +str(params['upstream_length'])
        SequenceSet['sequences'] = []


        prom= ""
        featureFound = False
        featureLocs = {}
        for feature in featureSet['elements']:
            #print(feature)
            #print(featureSet['elements'][feature])
            featureFound = False
            for f in features:
                #print f['id']
                #print feature
                if f['id'] == feature:

                    attributes = f['location'][0]
                    featureFound = True
                    #print('found match ' + feature)
                    #print(f['location'])
                    break
            if featureFound:
                Sequence = {}
                Sequence['sequence_id'] = feature
                Sequence['description'] = feature
                #Sequence['source'] =
                Source = {}
                Source['assembly_id'] = aref
                Source['location'] = []

                for record in SeqIO.parse(fasta_file['path'], 'fasta'):
                #for record in SeqIO.parse('/kb/module/work/Gmax_189_genome_assembly.fa', 'fasta'):
                #print(record.id)
                #print(attributes[0])
                    if record.id == attributes[0]:
                        #print('adding to prom string')
                    #print(attributes[0])
                        if attributes[2] == '+':
                            #print('1')
                        #might need to offset by 1?
                            end = attributes[1]
                            start = end - params['upstream_length']
                            if start < 0:
                                start = 0
                            Source['location'].append((attributes[0],start,'+',end))
                            promoter = record.seq[start:end].upper()
                            #HERE: resolve ambiguous characters
                            Sequence['sequence'] = str(promoter)
                            prom += ">" + feature + "\n"
                            prom += promoter + "\n"


                        elif attributes[2] == '-':
                            #print('2')
                            start = attributes[1]
                            end = start + params['upstream_length']
                            if end > len(record.seq) - 1:
                                end = len(record.seq) - 1
                            Source['location'].append((feature,start,'-',end))
                            promoter = record.seq[start:end].upper()
                            complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A','N': 'N'}
                            promoter = ''.join([complement[base] for base in promoter[::-1]])
                            #HERE: resolve ambiguous characters
                            Sequence['sequence'] = str(promoter)
                            prom += ">" + feature + "\n"
                            prom += promoter + "\n"

                        else:
                            print('Error on orientation')
                Sequence['source'] = Source
                SequenceSet['sequences'].append(Sequence)

            else:
                print('Could not find feature ' + feature + 'in genome')

        save_objects_params = {}
        save_objects_params['id'] = dfu.ws_name_to_id(params['ws_name'])
        save_objects_params['objects'] = [{'type': 'KBaseSequences.SequenceSet','data':SequenceSet,'name':objname}]
        info = dfu.save_objects(save_objects_params)[0]
        ref = "%s/%s/%s" % (info[6],info[0],info[4])
        out = {'SequenceSet_ref':ref}
        #END buildFromFeatureSet

        # At some point might do deeper type checking...
        if not isinstance(out, dict):
            raise ValueError('Method buildFromFeatureSet return value ' +
                             'out is not type dict as required.')
        # return the results
        return [out]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
