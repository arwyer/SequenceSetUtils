
package us.kbase.sequencesetutils;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: FeatureSetInputParams</p>
 * <pre>
 * ws_name - workspace name
 * FeatureSet_ref - handle to input feature set
 * genome_ref - handle to genome to extract features from
 * upstream_length - length of region upstream of features to extract sequences from
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "ws_name",
    "FeatureSet_ref",
    "genome_ref",
    "upstream_length"
})
public class FeatureSetInputParams {

    @JsonProperty("ws_name")
    private String wsName;
    @JsonProperty("FeatureSet_ref")
    private String FeatureSetRef;
    @JsonProperty("genome_ref")
    private String genomeRef;
    @JsonProperty("upstream_length")
    private Long upstreamLength;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("ws_name")
    public String getWsName() {
        return wsName;
    }

    @JsonProperty("ws_name")
    public void setWsName(String wsName) {
        this.wsName = wsName;
    }

    public FeatureSetInputParams withWsName(String wsName) {
        this.wsName = wsName;
        return this;
    }

    @JsonProperty("FeatureSet_ref")
    public String getFeatureSetRef() {
        return FeatureSetRef;
    }

    @JsonProperty("FeatureSet_ref")
    public void setFeatureSetRef(String FeatureSetRef) {
        this.FeatureSetRef = FeatureSetRef;
    }

    public FeatureSetInputParams withFeatureSetRef(String FeatureSetRef) {
        this.FeatureSetRef = FeatureSetRef;
        return this;
    }

    @JsonProperty("genome_ref")
    public String getGenomeRef() {
        return genomeRef;
    }

    @JsonProperty("genome_ref")
    public void setGenomeRef(String genomeRef) {
        this.genomeRef = genomeRef;
    }

    public FeatureSetInputParams withGenomeRef(String genomeRef) {
        this.genomeRef = genomeRef;
        return this;
    }

    @JsonProperty("upstream_length")
    public Long getUpstreamLength() {
        return upstreamLength;
    }

    @JsonProperty("upstream_length")
    public void setUpstreamLength(Long upstreamLength) {
        this.upstreamLength = upstreamLength;
    }

    public FeatureSetInputParams withUpstreamLength(Long upstreamLength) {
        this.upstreamLength = upstreamLength;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((((((("FeatureSetInputParams"+" [wsName=")+ wsName)+", FeatureSetRef=")+ FeatureSetRef)+", genomeRef=")+ genomeRef)+", upstreamLength=")+ upstreamLength)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
