from pandas import DataFrame
import pandas


def get_excel_DataFrame(excel_file_path: str, sheet_name: str):
    """Will read an excel file and dump its contents into a csv file"""
    from pandas import read_excel

    return read_excel(excel_file_path, sheet_name=sheet_name)


if __name__ == "__main__":
    from ....constants.FILE_PATHS import TEMP_EXCEL_FILE_PATH
    import json
    get_excel_DataFrame(TEMP_EXCEL_FILE_PATH, "Export")

    # with open("test.json", "w") as jf:
    #     jf.write(json.dumps(x))
