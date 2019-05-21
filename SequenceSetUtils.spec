/*
A KBase module: SequenceSetUtils
*/

module SequenceSetUtils {
    /* Ref to a genome
        @id ws KBaseGenomes.Genome
    */
    typedef string GenomeRef;

    /* Ref to a feature set
        @id ws KBaseCollections.FeatureSet
    */
    typedef string FeatureSetRef;

     /* Ref to a sequence set
        @id ws KBaseGeneRegulation.SequenceSet
    */
    typedef string SequenceSetRef;

    /* DNA/RNA strand orientation
        @range("-", "+")
     */
    typedef string orientation;

    typedef structure {
        string path;
        string shock_id;
        string ftp_url;
    } File;

    /* workspace name of the object */
    typedef string workspace_name;

    /* An X/Y/Z style reference */
    typedef string obj_ref;

    /*
	    SequenceSet_ref - KBase object reference to sequence set
	*/
	typedef structure{
		SequenceSetRef SequenceSet_ref;
	} SequenceSetOutputParams;

	/*
	    Input parameters for buildFromLocations

	    location_id, relevent identifiers to identify a sequence location:
	        contig_id - string - name relevent to the assembly contig, e.g. chr1, chrX, contig1, etc.
	        start - int - start of sequence
	        end - int - end of sequence
	        orientation - range("-", "+") - reference to the sense of a DNA/RNA strand
	*/

	typedef structure{
	    string contig_id;
	    int start;
	    orientation sense;
	    int end;
	} location_id;

	/*
	    sequence_location, sequence location container for seperation by genome:
	        genome_ref - genome referenced by sequence locations
	        genlocations - list of sequence locations sepecified by a location ids
	*/

	typedef structure{
		GenomeRef genome_ref;
		list<location_id> locations;
	} sequence_location;

	/*
	    LocationInputParams, direct inputs for buildFromLocation:
	        required:
                genome_ref - genome referenced by sequence locations
                genlocations - list of sequence locations sepecified by a location ids

            optional:
                seqsetname - name of sequence set output object
	*/

	typedef structure{
		workspace_name ws_name;
		list<sequence_location> seqlocations;
		string seqsetname;
	} LocationInputParams;

	funcdef buildFromLocations(LocationInputParams params)
		returns (SequenceSetOutputParams out) authentication required;
	
	/*
	    Input parameters for buildFromFasta:
            required:
                ws_name - workspace name
                file - identifiers for fasta file

            optional:
                seqsetname - name of sequence set output object
	*/

	typedef structure{
		workspace_name ws_name;
		File file;
		string seqsetname;
	} FastaInputParams;

	funcdef buildFromFasta(FastaInputParams params)
		returns (SequenceSetOutputParams out) authentication required;

	/*
	    Input parameters for buildFromFeatureSet
	        required:
                ws_name - workspace name
                FeatureSet_ref - validated reference to feature set
                genome_ref - validated reference to genome
                upstream_length - length of region upstream of features to extract sequences from

            optional:
                seqsetname - name of sequence set output object
	*/

	typedef structure{
		workspace_name  ws_name;
		FeatureSetRef FeatureSet_ref;
		GenomeRef genome_ref;
		int upstream_length;
		string seqsetname;
	} FeatureSetInputParams;

	funcdef buildFromFeatureSet(FeatureSetInputParams params)
		returns (SequenceSetOutputParams out) authentication required;
};
