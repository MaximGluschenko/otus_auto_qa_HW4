SCHEMA_1 = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "title": {"type": ["string", "null"]},
        "body": {"type": ["string", "null"]},
        "userId": {"type": "number"}
    },
    "required": ["id", "userId"]
}

SCHEMA_2 = {
    "type": "array",
    "properties": {
        "id": {"type": "number"},
        "title": {"type": ["string", "null"]},
        "body": {"type": ["string", "null"]},
        "userId": {"type": "number"}
    },
    "required": ["id", "userId"]
}

SCHEMA_3 = {
    "type": "array",
    "properties": {
        "postId": {"type": "number"},
        "id": {"type": "number"},
        "name": {"type": ["string", "null"]},
        "email": {"type": ["string", "null"]},
        "body": {"type": ["string", "null"]}
    },
    "required": ["postId", "id"]
}
