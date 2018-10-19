# -*- coding: utf-8 -*-
import unittest
import os  # noqa: F401
import json  # noqa: F401
import time
import requests

from os import environ
try:
    from ConfigParser import ConfigParser  # py2
except:
    from configparser import ConfigParser  # py3

from pprint import pprint  # noqa: F401

from biokbase.workspace.client import Workspace as workspaceService
from SequenceSetUtils.SequenceSetUtilsImpl import SequenceSetUtils
from SequenceSetUtils.SequenceSetUtilsServer import MethodContext
from SequenceSetUtils.authclient import KBaseAuth as _KBaseAuth
from random import choice
from DataFileUtil.DataFileUtilClient import DataFileUtil

class SequenceSetUtilsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('SequenceSetUtils'):
            cls.cfg[nameval[0]] = nameval[1]
        # Getting username from Auth profile for token
        authServiceUrl = cls.cfg['auth-service-url']
        auth_client = _KBaseAuth(authServiceUrl)
        user_id = auth_client.get_user(token)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'SequenceSetUtils',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = workspaceService(cls.wsURL)
        cls.serviceImpl = SequenceSetUtils(cls.cfg)
        cls.scratch = cls.cfg['scratch']
        cls.callback_url = os.environ['SDK_CALLBACK_URL']

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        if hasattr(self.__class__, 'wsName'):
            return self.__class__.wsName
        suffix = int(time.time() * 1000)
        wsName = "test_SequenceSetUtils_" + str(suffix)
        ret = self.getWsClient().create_workspace({'workspace': wsName})  # noqa
        self.__class__.wsName = wsName
        return wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx

    # NOTE: According to Python unittest naming rules test method names should start from 'test'. # noqa
    def test_buildFromFasta(self):
        # Prepare test objects in workspace if needed using
        # self.getWsClient().save_objects({'workspace': self.getWsName(),
        #                                  'objects': []})
        #
        # Run your method by
        # ret = self.getImpl().your_method(self.getContext(), parameters...)
        #
        # Check returned data with
        # self.assertEqual(ret[...], ...) or other unittest methods
        fastaPath = '/kb/module/work/tmp/testFasta.fasta'
        testFasta = open(fastaPath,'w')
        numSeq = 5
        seqNames = []
        seqs = []
        nameLen = 10
        seqLen = 100
        for n in range(0,numSeq):
            randname = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(nameLen))
            testaFasta.write('>' + randname + '\n')
            randseq=""
            for count in range(0,seqLen):
                randseq+=choice("CGTA")
            testFasta.write(randseq + '\n')
            seqNames.append(randname)
            seqs.append(randseq)
        testaFasta.close()
       
            
        
        params = {}
        params['path'] = fastaPath
        params['ws_name'] = self.getWsName()
        result = self.getImpl().buildFromFasta(self.getContext(),params)
        dfu = DataFileUtil(self.callback_url)
        get_objects_params = {}
        get_objects_params['object_refs'] = [result[0]['SequenceSet_ref']]
        SeqSet = dfu.get_objects(get_objects_params)[0]['data'][0]
        for s in SeqSet[sequences]:
            if s['sequence_id'] not in seqNames:
                assert 1 == 0
            assert len(set([s['sequence']]) & set(seqs)) >= 1
        
        
        pass
    def test_buildFromFeatureSet(self):
        # Prepare test objects in workspace if needed using
        # self.getWsClient().save_objects({'workspace': self.getWsName(),
        #                                  'objects': []})
        #
        # Run your method by
        # ret = self.getImpl().your_method(self.getContext(), parameters...)
        #
        # Check returned data with
        # self.assertEqual(ret[...], ...) or other unittest methods
        
        params = {}
        params['ws_name'] = 'pranjan77:narrative_1517498855061'
        params['FeatureSet_ref'] = '12566/6/1'
        params['genome_ref'] = '12566/5/3'
        params['upstream_length'] = 100
        result = self.getImpl().buildFromFeatureSet(self.getContext(),params)
        dfu = DataFileUtil(self.callback_url)
        get_objects_params = {}
        get_objects_params['object_refs'] = [result[0]['SequenceSet_ref']]
        SeqSet = dfu.get_objects(get_objects_params)[0]['data'][0]
        
        pass
