class ParsedData:
    def __init__(self, parsed_data: "dict[str, str]" = {}):
        self._data = parsed_data

    def add(self, key: str, value: str):
        self._data[key] = value

    def get(self) -> "dict[str, str]":
        return self._data

    def __str__(self) -> str:
        string_list = [f"{key}: {value}" for key, value in self._data.items()]  # nopep8
        return "\n".join(string_list)

   

if __name__ == "__main__":
    a = ParsedData({"kaas": "brood", "afslfk": "asdfz"})
    print(a)
