import json
import urllib.request


def tl_definition_to_dict(tl_definition):
    parts = tl_definition.strip().split("=")

    if len(parts) == 2:
        tl_type_part = parts[0].strip()
        result_type = parts[1].strip().replace(";", "")
        type_components = tl_type_part.split()

        if len(type_components) >= 1:
            tl_type = type_components[0]
            tl_dict = {"type": tl_type, "args": {}, "result_type": result_type}
            param_list = type_components[1:]
            current_param = None

            for param in param_list:
                if ":" in param:
                    param_parts = param.split(":")
                    if len(param_parts) == 2:
                        param_name, param_type = param_parts
                        current_param = {"type": param_type}
                        tl_dict["args"][param_name] = current_param
                elif current_param:
                    current_param["type"] += f" {param}"

            return tl_dict
        elif len(type_components) == 1:
            tl_type = type_components[0]
            return {"type": tl_type, "result_type": result_type}

    return None


def parse_tl_schema(tl_schema: str):
    start_parsing = False
    is_functions = False
    data = {
        "name": "Auto-generated JSON TonLib API for PyTonJSON ~ https://github.com/pytdbot/client",
        "classes": {},
        "types": {},
        "functions": {},
    }

    for line in tl_schema.splitlines():
        line = line.strip()
        if "--functions--" in line:
            is_functions = True
            continue

        if line.startswith("error"):
            start_parsing = True
        elif line == "" or line.startswith("//"):
            continue

        if start_parsing:
            tl_def = tl_definition_to_dict(line)
            tl_def_name = tl_def["type"]

            del tl_def["type"]

            if tl_def["result_type"] not in data["classes"]:
                data["classes"][tl_def["result_type"]] = {}

                data["classes"][tl_def["result_type"]]["types"] = []
                data["classes"][tl_def["result_type"]]["functions"] = []

            if is_functions:
                data["functions"][tl_def_name] = tl_def
                data["classes"][tl_def["result_type"]]["functions"].append(tl_def_name)
            else:
                data["types"][tl_def_name] = tl_def
                data["classes"][tl_def["result_type"]]["types"].append(tl_def_name)

    return data


if __name__ == "__main__":
    urllib.request.urlretrieve(
        "https://raw.githubusercontent.com/ton-blockchain/ton/master/tl/generate/scheme/tonlib_api.tl",
        "tonlib_api.tl",
    )

    with open("tonlib_api.tl", "r") as f:
        tl_json = parse_tl_schema(f.read())

        with open("tonlib_api.json", "w+") as f:
            f.write(json.dumps(tl_json, indent=4))
