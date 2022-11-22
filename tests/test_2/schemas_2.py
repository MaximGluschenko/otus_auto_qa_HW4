SCHEMA_1 = {
    "type": "array",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "brewery_type": {"type": ["string", "null"]},
        "street": {"type": ["string", "null"]},
        "address_2": {"type": ["string", "null"]},
        "address_3": {"type": ["string", "null"]},
        "city": {"type": ["string", "null"]},
        "state": {"type": ["string", "null"]},
        "county_province": {"type": ["string", "null"]},
        "postal_code": {"type": ["string", "null"]},
        "country": {"type": ["string", "null"]},
        "longitude": {"type": ["string", "null"]},
        "latitude": {"type": ["string", "null"]},
        "phone": {"type": ["string", "null"]},
        "website_url": {"type": ["string", "null"]},
        "updated_at": {"type": ["string", "null"]},
        "created_at": {"type": ["string", "null"]}
    },
    "required": ["id"]
}

SCHEMA_2 = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "brewery_type": {"type": ["string", "null"]},
        "street": {"type": ["string", "null"]},
        "address_2": {"type": ["string", "null"]},
        "address_3": {"type": ["string", "null"]},
        "city": {"type": ["string", "null"]},
        "state": {"type": ["string", "null"]},
        "county_province": {"type": ["string", "null"]},
        "postal_code": {"type": ["string", "null"]},
        "country": {"type": ["string", "null"]},
        "longitude": {"type": ["string", "null"]},
        "latitude": {"type": ["string", "null"]},
        "phone": {"type": ["string", "null"]},
        "website_url": {"type": ["string", "null"]},
        "updated_at": {"type": ["string", "null"]},
        "created_at": {"type": ["string", "null"]}
    },
    "required": ["id", "name"]
}
