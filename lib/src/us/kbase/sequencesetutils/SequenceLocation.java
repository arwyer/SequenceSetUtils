
package us.kbase.sequencesetutils;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import us.kbase.common.service.Tuple4;


/**
 * <p>Original spec-file type: sequence_location</p>
 * <pre>
 * genome_ref - handle to genome
 * genlocations - list of locations in the genome to build a single sequence from, usually length 1
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "genome_ref",
    "genlocations"
})
public class SequenceLocation {

    @JsonProperty("genome_ref")
    private java.lang.String genomeRef;
    @JsonProperty("genlocations")
    private List<Tuple4 <String, Long, String, Long>> genlocations;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("genome_ref")
    public java.lang.String getGenomeRef() {
        return genomeRef;
    }

    @JsonProperty("genome_ref")
    public void setGenomeRef(java.lang.String genomeRef) {
        this.genomeRef = genomeRef;
    }

    public SequenceLocation withGenomeRef(java.lang.String genomeRef) {
        this.genomeRef = genomeRef;
        return this;
    }

    @JsonProperty("genlocations")
    public List<Tuple4 <String, Long, String, Long>> getGenlocations() {
        return genlocations;
    }

    @JsonProperty("genlocations")
    public void setGenlocations(List<Tuple4 <String, Long, String, Long>> genlocations) {
        this.genlocations = genlocations;
    }

    public SequenceLocation withGenlocations(List<Tuple4 <String, Long, String, Long>> genlocations) {
        this.genlocations = genlocations;
        return this;
    }

    @JsonAnyGetter
    public Map<java.lang.String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(java.lang.String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public java.lang.String toString() {
        return ((((((("SequenceLocation"+" [genomeRef=")+ genomeRef)+", genlocations=")+ genlocations)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
