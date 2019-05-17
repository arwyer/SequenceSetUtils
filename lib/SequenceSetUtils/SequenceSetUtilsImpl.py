# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os

from installed_clients.KBaseReportClient import KBaseReport
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
    GIT_URL = "https://github.com/kbasecollaborations/SequenceSetUtils.git"
    GIT_COMMIT_HASH = "b44fe2aefa144aea9e592122d7964e5b9b746e7f"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
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
