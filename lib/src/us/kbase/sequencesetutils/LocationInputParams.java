
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


/**
 * <p>Original spec-file type: LocationInputParams</p>
 * <pre>
 * ws_name - workspace name
 * seqlocations - list of sequence locations
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "ws_name",
    "seqlocations"
})
public class LocationInputParams {

    @JsonProperty("ws_name")
    private String wsName;
    @JsonProperty("seqlocations")
    private List<SequenceLocation> seqlocations;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("ws_name")
    public String getWsName() {
        return wsName;
    }

    @JsonProperty("ws_name")
    public void setWsName(String wsName) {
        this.wsName = wsName;
    }

    public LocationInputParams withWsName(String wsName) {
        this.wsName = wsName;
        return this;
    }

    @JsonProperty("seqlocations")
    public List<SequenceLocation> getSeqlocations() {
        return seqlocations;
    }

    @JsonProperty("seqlocations")
    public void setSeqlocations(List<SequenceLocation> seqlocations) {
        this.seqlocations = seqlocations;
    }

    public LocationInputParams withSeqlocations(List<SequenceLocation> seqlocations) {
        this.seqlocations = seqlocations;
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
        return ((((((("LocationInputParams"+" [wsName=")+ wsName)+", seqlocations=")+ seqlocations)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
