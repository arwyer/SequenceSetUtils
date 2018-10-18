
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
 * <p>Original spec-file type: SequenceSetOutputParams</p>
 * <pre>
 * SequenceSet_ref - handle to the new SequenceSet object
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "SequenceSet_ref"
})
public class SequenceSetOutputParams {

    @JsonProperty("SequenceSet_ref")
    private String SequenceSetRef;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("SequenceSet_ref")
    public String getSequenceSetRef() {
        return SequenceSetRef;
    }

    @JsonProperty("SequenceSet_ref")
    public void setSequenceSetRef(String SequenceSetRef) {
        this.SequenceSetRef = SequenceSetRef;
    }

    public SequenceSetOutputParams withSequenceSetRef(String SequenceSetRef) {
        this.SequenceSetRef = SequenceSetRef;
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
        return ((((("SequenceSetOutputParams"+" [SequenceSetRef=")+ SequenceSetRef)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
