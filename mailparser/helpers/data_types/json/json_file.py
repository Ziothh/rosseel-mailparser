from json import load


def get_json_data(json_file_path: str):
    with open(json_file_path, "r") as f:
        return load(f)
