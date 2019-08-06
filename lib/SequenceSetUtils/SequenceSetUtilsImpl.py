# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os
from .fasta import FastaUtil
from .featureset import FeatureSetUtil
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
    GIT_COMMIT_HASH = "23c917823641dd55f275b084117b41dc12c3e650"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        self.FastaUtil = FastaUtil(config)
        self.FeatureSetUtil = FeatureSetUtil(self.callback_url, config)
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        #END_CONSTRUCTOR
        pass


    def buildFromLocations(self, ctx, params):
        """
        :param params: instance of type "LocationInputParams"
           (LocationInputParams, direct inputs for buildFromLocation:
           required: genome_ref - genome referenced by sequence locations
           genlocations - list of sequence locations sepecified by a location
           ids optional: seqsetname - name of sequence set output object) ->
           structure: parameter "ws_name" of type "workspace_name" (workspace
           name of the object), parameter "seqlocations" of list of type
           "sequence_location" (sequence_location, sequence location
           container for seperation by genome: genome_ref - genome referenced
           by sequence locations genlocations - list of sequence locations
           sepecified by a location ids) -> structure: parameter "genome_ref"
           of type "GenomeRef" (Ref to a genome @id ws KBaseGenomes.Genome),
           parameter "locations" of list of type "location_id" (Input
           parameters for buildFromLocations location_id, relevent
           identifiers to identify a sequence location: contig_id - string -
           name relevent to the assembly contig, e.g. chr1, chrX, contig1,
           etc. start - int - start of sequence end - int - end of sequence
           orientation - range("-", "+") - reference to the sense of a
           DNA/RNA strand) -> structure: parameter "contig_id" of String,
           parameter "start" of Long, parameter "sense" of type "orientation"
           (DNA/RNA strand orientation @range("-", "+")), parameter "end" of
           Long, parameter "seqsetname" of String
        :returns: instance of type "SequenceSetOutputParams" (SequenceSet_ref
           - KBase object reference to sequence set) -> structure: parameter
           "SequenceSet_ref" of type "SequenceSetRef" (Ref to a sequence set
           @id ws KBaseGeneRegulation.SequenceSet)
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

    def buildFromFasta(self, ctx, params):
        """
        :param params: instance of type "FastaInputParams" (Input parameters
           for buildFromFasta: required: ws_name - workspace name file -
           identifiers for fasta file optional: seqsetname - name of sequence
           set output object) -> structure: parameter "ws_name" of type
           "workspace_name" (workspace name of the object), parameter "file"
           of type "File" -> structure: parameter "path" of String, parameter
           "shock_id" of String, parameter "ftp_url" of String, parameter
           "seqsetname" of String
        :returns: instance of type "SequenceSetOutputParams" (SequenceSet_ref
           - KBase object reference to sequence set) -> structure: parameter
           "SequenceSet_ref" of type "SequenceSetRef" (Ref to a sequence set
           @id ws KBaseGeneRegulation.SequenceSet)
        """
        # ctx is the context object
        # return variables are: out
        #BEGIN buildFromFasta

        # TODO: params validation

        self.FastaUtil.openFasta(params['file'])
        self.FastaUtil.buildSeqSet(params)
        ref = self.FastaUtil.saveSeqSet(params)

        out = {'SequenceSet_ref': ref}

        #END buildFromFasta

        # At some point might do deeper type checking...
        if not isinstance(out, dict):
            raise ValueError('Method buildFromFasta return value ' +
                             'out is not type dict as required.')
        # return the results
        return [out]

    def SeqSetToFasta(self, ctx, params):
        """
        :param params: instance of type "SeqSet2FastaInput" -> structure:
           parameter "ws_name" of type "workspace_name" (workspace name of
           the object), parameter "SS_ref" of type "SequenceSetRef" (Ref to a
           sequence set @id ws KBaseGeneRegulation.SequenceSet)
        :returns: instance of type "SS2FastaOutputParams" -> structure:
           parameter "fasta_output" of type "File" -> structure: parameter
           "path" of String, parameter "shock_id" of String, parameter
           "ftp_url" of String
        """
        # ctx is the context object
        # return variables are: out
        #BEGIN SeqSetToFasta

        out = {
                'path' : self.FastaUtil.SS2Fasta(params)
        }

        #END SeqSetToFasta

        # At some point might do deeper type checking...
        if not isinstance(out, dict):
            raise ValueError('Method SeqSetToFasta return value ' +
                             'out is not type dict as required.')
        # return the results
        return [out]

    def buildFromFeaturePromoters(self, ctx, params):
        """
        :param params: instance of type "FeatureSetInputParams" (Input
           parameters for buildFromFeatureSet required: ws_name - workspace
           name FeatureSet_ref - validated reference to feature set
           genome_ref - validated reference to genome upstream_length -
           length of region upstream of features to extract sequences from
           optional: seqsetname - name of sequence set output object) ->
           structure: parameter "ws_name" of type "workspace_name" (workspace
           name of the object), parameter "FeatureSet_ref" of type
           "FeatureSetRef" (Ref to a feature set @id ws
           KBaseCollections.FeatureSet), parameter "genome_ref" of type
           "GenomeRef" (Ref to a genome @id ws KBaseGenomes.Genome),
           parameter "upstream_length" of Long, parameter "seqsetname" of
           String
        :returns: instance of type "SequenceSetOutputParams" (SequenceSet_ref
           - KBase object reference to sequence set) -> structure: parameter
           "SequenceSet_ref" of type "SequenceSetRef" (Ref to a sequence set
           @id ws KBaseGeneRegulation.SequenceSet)
        """
        # ctx is the context object
        # return variables are: out
        #BEGIN buildFromFeaturePromoters

        # Downloads
        self.FeatureSetUtil.getFeatureSet(params['FeatureSet_ref'])
        self.FeatureSetUtil.getGenomeData(params['genome_ref'])

        # Parsing
        sequenceset = self.FeatureSetUtil.makeSequenceSet(params)
        saveseqset = self.FeatureSetUtil.saveSequenceSet(sequenceset, params)

        out = {'SequenceSet_ref': saveseqset}

        #END buildFromFeaturePromoters

        # At some point might do deeper type checking...
        if not isinstance(out, dict):
            raise ValueError('Method buildFromFeaturePromoters return value ' +
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
