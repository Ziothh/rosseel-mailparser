def dump_str_to_file(string: str, file_location: str):
    with open(file_location, "w", encoding="utf-8") as f:
        f.write(string)