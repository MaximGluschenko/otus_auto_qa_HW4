SCHEMA_1 = {
    "type": "object",
    "properties": {
        "message": {
            "type": "object",
            "patternProperties": {
                "^[a-z]+$": {
                    "type": "array",
                    "items": {"type": "string"}
                }
            }
        }
    },
    "required": ["message", "status"]
}

SCHEMA_2 = {
    "type": "object",
    "properties": {
        "message": {
            "type": "array",
            "breed": {"type": "string"}
        },
        "status": {"type": "string"}
    },
    "required": ["message", "status"]
}

SCHEMA_3 = {
    "type": "object",
    "properties": {
        "message": {"type": "string"},
        "status": {"type": "string"}
    },
    "required": ["message", "status"]
}
