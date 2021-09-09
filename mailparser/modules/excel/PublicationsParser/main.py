from ....constants.FILE_PATHS import TEMP_EXCEL_FILE_PATH

from ....helpers.data_types.json import get_json_data

from ..utils.conversions import get_excel_DataFrame


class PublicationsParser:
    def __init__(self) -> None:
        self.keys_config: "dict[str,list[dict[str, str]]]" = get_json_data("./mailparser/modules/excel/PublicationsParser/config.json")  # nopep8
        self.data_frame = get_excel_DataFrame(
            excel_file_path=TEMP_EXCEL_FILE_PATH,
            sheet_name="Export"
        )


if __name__ == "__main__":
    pp = PublicationsParser()
    print(pp.keys_config)
