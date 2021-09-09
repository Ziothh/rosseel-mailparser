import json
from json.decoder import JSONDecodeError
from os import waitpid
from .json_data_handler import data_to_json


class JSONFile:
    def __init__(self, file_location: str, get_file_data_type: bool = False):
        self.FILE_LOCATION = file_location

        self.data_type = None
        if get_file_data_type:
            try:  # Check if the file already exists
                file_data = self.read()
            except FileNotFoundError:
                pass
            else:
                if file_data != None:
                    self.data_type = type(file_data)

    def __repr__(self) -> str:
        return f"JSONFile(FILE_LOCATION = {self.FILE_LOCATION}, data_type = {self.data_type})"

    def read(self, default_value=None):
        """
        Will read the file and return its data.\n
        If the file is not found and default_value is specified it will return that value
        """

        if type(default_value) == type:
            default_value = default_value()

        file_data = None
        try:
            with open(self.FILE_LOCATION, "rb") as rf:
                file_data = json.load(rf)

        #! This can lead to bugs if you're not careful since you'll always get something back
        except FileNotFoundError as e:
            if not default_value:
                raise e
            file_data = default_value
        except JSONDecodeError:
            return default_value

        return file_data

    @property
    def exists(self) -> bool:
        """Checks if the specified file exists"""
        try:
            with open(self.FILE_LOCATION) as f:
                return True
        except FileNotFoundError:
            return False
        except JSONDecodeError:
            return True

    def write(self, data: dict, data_type=None, raw_data: bool = False, keep_old_data: bool = True):
        """
        data (dict): The data to be added to the JSON file
        data_type (list | dict | None, optional): if the current file doesn't already have data the data will be added to a list or dict. Defaults to None.
        raw_data (bool, optional): if it's true, then the raw data object will be written to the file. Defaults to False.
        keep_old_data (bool, optional): self explanatory. Defaults to True.
        """

        def write_to_JSON_file(file_location: str, data):
            with open(file_location, "w") as wf:
                wf.write(data_to_json(data, indent=4))

        # if both data_types aren't specified it will just write the raw data to the file file
        if not data_type and not self.data_type:
            raw_data = True

        file_data = None
        if not raw_data:
            if keep_old_data:
                # data_type is a class so you'll have to instanciate it
                file_data = self.read(default_value=data_type)

                if self.data_type == list:
                    file_data.append(data)
                elif self.data_type == dict:
                    file_data.update(data)
            else:
                if data_type == list:
                    file_data = [].append(data)
                elif data_type == dict:
                    file_data = {}.update(data)
        else:
            file_data = data

        write_to_JSON_file(self.FILE_LOCATION, data=file_data)
        return self

    def print_data(self):
        print(self.read())
        return self

    def clear(self):
        """Empties the file"""
        with open(self.FILE_LOCATION, "w") as f:
            pass

    def remove(self):
        """Deletes the file"""
        import os
        os.remove(self.FILE_LOCATION)


if __name__ == "__main__":
    f = JSONFile("./data/test.json")
    print(f)
    f.write(data={"s": "val"})
