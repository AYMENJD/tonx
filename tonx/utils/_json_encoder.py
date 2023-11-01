import importlib
import tonlib


# Currently this class is not used and i am not planing to, but maybe i change my min
class JSONEncoder:
    def __init__(self):
        self.json_lib = None
        self._set_json_lib()
        self.lib_name = self.json_lib.__name__

    def _set_json_lib(self):
        libraries = ["orjson", "ujson", "json"]
        for lib in libraries:
            try:
                self.json_lib = importlib.import_module(lib)
                break
            except ImportError:
                continue

        if self.json_lib is None:
            raise ImportError("No suitable JSON library found.")

    def obj_to_json(self, obj, **kwargs):
        if self.json_lib.__name__ == "orjson":
            return self.json_lib.dumps(self._serialize_obj(obj), **kwargs) + b"\0"
        else:
            return self.json_lib.dumps(self._serialize_obj(obj), **kwargs).encode(
                "utf-8"
            )

    def json_to_obj(self, json_str, **kwargs):
        return self._deserialize_obj(self.json_lib.loads(json_str, **kwargs))

    def _serialize_obj(self, obj):
        if hasattr(obj, "to_dict"):
            return self._serialize_obj(obj.to_dict())
        elif isinstance(obj, list):
            return [self._serialize_obj(item) for item in obj]
        elif isinstance(obj, dict):
            return {key: self._serialize_obj(value) for key, value in obj.items()}
        else:
            return obj

    def _deserialize_obj(self, obj):
        if isinstance(obj, dict):
            if "@type" in obj:
                return getattr(
                    tonlib.types, tonlib.utils.to_camel_case(obj["@type"])
                ).from_dict(obj)
            else:
                return {key: self._deserialize_obj(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [self._deserialize_obj(item) for item in obj]
        else:
            return obj
