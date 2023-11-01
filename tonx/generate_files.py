import json, black, pathlib, keyword

indent = "    "


def to_camel_case(input_str: str, delimiter: str = ".", is_class: bool = True) -> str:
    if not input_str:
        return ""

    parts = input_str.split(delimiter)
    camel_case_str = ""

    for i, part in enumerate(parts):
        if i > 0:
            camel_case_str += part[0].upper() + part[1:]
        else:
            camel_case_str += part

    if camel_case_str:
        camel_case_str = (
            camel_case_str[0].upper() if is_class else camel_case_str[0].lower()
        ) + camel_case_str[1:]

    return camel_case_str


def getArgTypePython(type_name: str, is_function: bool = False):
    if type_name == "double":
        return "float"
    elif type_name in {"string", "secureString"}:
        return "str"
    elif type_name in {"int32", "int53", "int64", "int256"}:
        return "int"
    elif type_name in {"bytes", "secureBytes"}:
        return "bytes"
    elif type_name == "Bool":
        return "bool"
    elif type_name in {"Object", "Function"}:
        return "dict"
    elif type_name == "#":
        return "int"
    elif "?" in type_name:
        return getArgTypePython(type_name.split("?")[-1], is_function)
    elif type_name.startswith("("):
        type_name = type_name.removeprefix("(").removesuffix(")")
        a, b = type_name.split(" ")
        if a == "vector":
            return f"List[{getArgTypePython(b, is_function)}]"
        else:
            raise Exception(f"Unknown data type {a}/{b}")
    elif type_name.startswith("vector<"):
        inner_type_start = type_name.find("<") + 1
        inner_type_end = type_name.rfind(">")
        inner_type = type_name[inner_type_start:inner_type_end]
        return f"List[{getArgTypePython(inner_type, is_function)}]"
    else:
        return (
            to_camel_case(type_name, is_class=True)
            if not is_function
            else "types." + to_camel_case(type_name, is_class=True)
        )


def generate_arg_value(arg_type, arg_name):
    if arg_type == "int":
        arg_value = f"int({arg_name})"
    elif arg_type == "float":
        arg_value = f"float({arg_name})"
    elif arg_type == "bytes":
        arg_value = f"b64decode({arg_name})"
    elif arg_type == "bool":
        arg_value = f"bool({arg_name})"
    elif arg_type.startswith("List[") or arg_type == "list":
        arg_value = f"{arg_name} or []"
    else:
        arg_value = arg_name

    return arg_value


def generate_arg_default(arg_type):
    if arg_type == "int":
        arg_value = f"0"
    elif arg_type == "str":
        arg_value = '""'
    elif arg_type == "float":
        arg_value = f"0.0"
    elif arg_type == "bytes":
        arg_value = f'b""'
    elif arg_type == "bool":
        arg_value = f"False"
    else:
        arg_value = "None"

    return arg_value


def generate_args_def(args, is_function: bool = False):
    args_list = ["self"]
    for arg_name, arg_data in args.items():
        if arg_name in keyword.kwlist:
            arg_name += "_"

        arg_type = getArgTypePython(arg_data["type"], is_function)

        args_list.append(f"{arg_name}: {arg_type} = {generate_arg_default(arg_type)}")

    return ", ".join(args_list)


def generate_union_types(arg_type, arg_type_name, classes, noneable=True):
    unions = [arg_type]

    if (
        arg_type_name in classes
    ):  # The arg type is a class which has subclasses and we need to include them
        unions.pop(0)

        for type_name in classes[arg_type_name]["types"]:
            unions.append(to_camel_case(type_name, is_class=True))

    if noneable:
        unions.append("None")

    return f"Union[{', '.join(unions)}]"


def generate_self_args(args, classes):
    args_list = []
    for arg_name, arg_data in args.items():
        if arg_name in keyword.kwlist:
            arg_name += "_"

        arg_type = getArgTypePython(arg_data["type"])
        arg_value = generate_arg_value(arg_type, arg_name)
        if arg_value == arg_name:  # a.k.a field can be None
            arg_type = generate_union_types(arg_type, arg_data["type"], classes)

        args_list.append(f"self.{arg_name}: {arg_type} = {arg_value}")
    return "; ".join(args_list)


def generate_to_dict_return(args):
    args_list = ['"@type": self.getType()']
    for arg_name, _ in args.items():
        if arg_name in keyword.kwlist:
            arg_name += "_"
        args_list.append(f'"{arg_name}": self.{arg_name}')

    args_list.append(f'"@extra": self.extra_id')
    return ", ".join(args_list)


def generate_from_dict_kwargs(args):
    args_list = []
    for arg_name, arg_data in args.items():
        if arg_name in keyword.kwlist:
            arg_name += "_"

        args_list.append(
            f'{arg_name}=data.get("{arg_name}", {generate_arg_default(getArgTypePython(arg_data["type"]))})'
        )
    args_list.append(f'extra_id=data.get("@extra")')

    return ", ".join(args_list)


def generate_function_invoke_args(args):
    args_list = []
    for arg_name, _ in args.items():
        if arg_name in keyword.kwlist:
            arg_name += "_"
        args_list.append(f'"{arg_name}": {arg_name}')

    return ", ".join(args_list)


class_template = """class {class_name}:
    \"\"\"{docstring}\"\"\"

    pass"""


def generate_classes(f, classes):
    for class_name in classes.keys():
        f.write(
            class_template.format(
                class_name=to_camel_case(class_name, is_class=True),
                docstring=f"Class for ``{class_name}``",
            )
            + "\n\n"
        )


types_template = """class {class_name}(TlObject, {inherited_class}):
    \"\"\"{docstring}\"\"\"

    def __init__({init_args}, extra_id: str = None) -> None:
        {self_args}
        self.extra_id: str = extra_id

    def __str__(self):
        return str(tonx.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["{type_name}"]:
        return "{type_name}"

    def getClass(self) -> Literal["{class_type_name}"]:
        return "{class_type_name}"

    def to_dict(self) -> dict:
        data = {{{to_dict_return}}}

        if not self.extra_id:
            del data['@extra']

        return data

    @classmethod
    def from_dict(cls, data: dict) -> Union["{class_name}", None]:
        return cls({from_dict_kwargs}) if data else None"""


def generate_types(f, types, classes):
    for type_name, type_data in types.items():
        args_def = generate_args_def(type_data["args"])
        self_args = generate_self_args(type_data["args"], classes)
        to_return_dict = generate_to_dict_return(type_data["args"])
        from_dict_kwargs = generate_from_dict_kwargs(type_data["args"])

        f.write(
            types_template.format(
                class_name=to_camel_case(type_name, is_class=True),
                inherited_class=to_camel_case(type_data["result_type"], is_class=True),
                class_type_name=type_data["result_type"],
                docstring=f"Type for ``{type_name}``",
                init_args=args_def,
                self_args=self_args,
                type_name=type_name,
                to_dict_return=to_return_dict,
                from_dict_kwargs=from_dict_kwargs,
            )
            + "\n\n"
        )


functions_template = """async def {function_name}({function_args}, request_timeout: float = 10.0, wait_sync: bool = False) -> Union[types.Error, types.{return_type}]:
        \"\"\"{docstring}\"\"\"

        return await self.invoke({{'@type': '{method_name}', {function_invoke_args}}}, timeout=request_timeout, wait_sync=wait_sync)"""


def generate_functions(f, types):
    for function_name, function_data in types.items():
        args_def = generate_args_def(function_data["args"], True)
        invoke_args = generate_function_invoke_args(function_data["args"])

        f.write(
            indent
            + functions_template.format(
                function_name=to_camel_case(function_name, is_class=False),
                function_args=args_def,
                return_type=to_camel_case(function_data["result_type"], is_class=True),
                docstring=f"Method for ``{function_name}``",
                method_name=function_name,
                function_invoke_args=invoke_args,
            )
            + "\n\n"
        )


if __name__ == "__main__":
    with open("tonlib_api.json", "r") as f:
        tl_json = json.loads(f.read())

    with open("types/tonlib_types.py", "w+") as types_file:
        types_file.write("from typing import Union, Literal, List\n")
        types_file.write("from base64 import b64decode\n")
        types_file.write("\nimport tonx\n\n")
        types_file.write(
            """class TlObject:
    \"\"\"Base class for TL Objects\"\"\"

    def getType(self):
        raise NotImplementedError

    def getClass(self):
        raise NotImplementedError

    def to_dict(self) -> dict:
        raise NotImplementedError

    @classmethod
    def from_dict(cls, data: dict):
        raise NotImplementedError\n\n"""
        )

        generate_classes(types_file, tl_json["classes"])
        generate_types(types_file, tl_json["types"], tl_json["classes"])

    with open("methods/tonlib_functions.py", "w+") as functions_file:
        functions_file.write("from typing import Union, List\nfrom .. import types\n\n")

        functions_file.write("class TonlibFunctions:\n")
        functions_file.write(
            f'{indent}"""A class that include all tonlib functions"""\n\n'
        )

        generate_functions(functions_file, tl_json["functions"])

    black_mode = black.Mode(
        target_versions={
            black.TargetVersion.PY39,
            black.TargetVersion.PY310,
            black.TargetVersion.PY311,
            black.TargetVersion.PY312,
        }
    )

    black.format_file_in_place(
        pathlib.Path("types/tonlib_types.py"),
        fast=False,
        write_back=black.WriteBack.YES,
        mode=black_mode,
    )

    black.format_file_in_place(
        pathlib.Path("methods/tonlib_functions.py"),
        fast=False,
        write_back=black.WriteBack.YES,
        mode=black_mode,
    )
