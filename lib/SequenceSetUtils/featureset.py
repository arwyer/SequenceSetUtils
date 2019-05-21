from installed_clients.DataFileUtilClient import DataFileUtil

class featuresetutil:
    def __init__(self, callback):
        self.dfu = DataFileUtil(callback)

    def getFeatureSet(self, ref):
        self.fset = self.dfu.get_objects({
            'object_refs': ref
        })[0]

        return self.fset

    def getGenomes(self, genome_list):
