import json
from jsonschema import validate

FINAL_SCHEMA = {
    "type": "object",
    "properties": {
        "original_input": {"type": "string"},
        "model_a_initial": {"type": "string"},
        "model_b_critique": {"type": "string"},
        "model_a_revised": {"type": "string"},
        "final_evaluation": {"type": "string"}
    },
    "required": [
        "original_input",
        "model_a_initial",
        "model_b_critique",
        "model_a_revised",
        "final_evaluation"
    ]
}

def validate_topic(text):
    if len(text.strip()) < 20:
        raise ValueError("Input too short or not meaningful.")
    return True

def validate_final_json(output):
    validate(instance=output, schema=FINAL_SCHEMA)