def dict_replace(string: str, old_new_pair: "dict[str, str]") -> str:
    for key, value in old_new_pair.items():
        string = string.replace(key, value)
    return string
