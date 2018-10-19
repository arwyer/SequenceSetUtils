/*
A KBase module: SequenceSetUtils
*/

module SequenceSetUtils {
    /*
        Insert your typespec information here.
    */
	
	typedef string Contig_id;
	typedef string orientation;
	
	/*
	genome_ref - handle to genome
	genlocations - list of locations in the genome to build a single sequence from, usually length 1
	*/
	typedef structure{
		string genome_ref;
		list<tuple<Contig_id,int,orientation,int>> genlocations;
	} sequence_location;

	
	/*
	ws_name - workspace name
	path - path to fasta in the workspace
	*/
	typedef structure{
		string ws_name;
		string path;
	} FastaInputParams;
	
	/*
	ws_name - workspace name
	seqlocations - list of sequence locations
	*/
	typedef structure{
		string ws_name;
		list<sequence_location> seqlocations;
	} LocationInputParams;
	
	/*
	ws_name - workspace name
	FeatureSet_ref - handle to input feature set
	genome_ref - handle to genome to extract features from
	upstream_length - length of region upstream of features to extract sequences from
	*/
	typedef structure{
		string ws_name;
		string FeatureSet_ref;
		string genome_ref;
		int upstream_length;
	} FeatureSetInputParams;
	
	
	/*
	SequenceSet_ref - handle to the new SequenceSet object
	*/
	typedef structure{
		string SequenceSet_ref;
	} SequenceSetOutputParams;
	
	funcdef buildFromFasta(FastaInputParams params)
		returns (SequenceSetOutputParams out) authentication required;
	
	funcdef buildFromLocations(LocationInputParams params)
		returns (SequenceSetOutputParams out) authentication required;
		
	funcdef buildFromFeatureSet(FeatureSetInputParams params)
		returns (SequenceSetOutputParams out) authentication required;
};
