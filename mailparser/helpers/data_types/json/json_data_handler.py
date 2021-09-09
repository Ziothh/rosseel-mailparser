import json


def data_to_json(data, indent: int = None):
    """Fixes ascii decoding and allows an indent amount to be specified (defaults to None)"""
    return json.dumps(data, ensure_ascii=False, indent=indent)


if __name__ == "__main__":
    print(data_to_json({"test": "val"}, indent=4))
