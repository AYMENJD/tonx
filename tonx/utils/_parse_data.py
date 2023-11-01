import json
from base64 import b64encode

import tonx


def parse_data(data):
    if isinstance(data, dict):
        return getattr(tonx.types, tonx.utils.to_camel_case(data["@type"])).from_dict(
            data
        )
    elif isinstance(data, list):
        return [parse_data(el) for el in data]
    elif isinstance(data, bytes):
        return b64encode(data).decode("utf-8")
    else:
        return data


def serialize_obj(obj):
    if isinstance(obj, bytes):
        return b64encode(obj).decode("utf-8")

    return obj.to_dict()


def obj_to_json(obj, **kwargs):
    return json.dumps(obj, default=serialize_obj, **kwargs)


def json_to_obj(json_obj, **kwargs):
    return json.loads(json_obj, object_hook=parse_data, **kwargs)
