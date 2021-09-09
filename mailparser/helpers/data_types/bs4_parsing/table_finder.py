from logging import fatal
from .__basic_imports import BeautifulSoup, Tag
from ...errors import TableNotFoundError


def __table_has_keys(keys_list: "list[list[str]]", table: Tag):
    def one_key_in_table(key_list: "list[str]", table: str):
        for key in key_list:
            if key.lower() in table:
                return True
        return False

    table = str(table).lower()
    for key_list in keys_list:
        if not one_key_in_table(key_list=key_list, table=table):
            return False
    return True


def __get_table_via_path(path: list, top_layer: BeautifulSoup) -> BeautifulSoup:
    current_layer = top_layer
    try:
        # at start of function: current_layer = top level of the document
        for xml_tag, tag_index in path:
            if tag_index == 0:
                current_layer = current_layer.find(xml_tag)
            else:
                current_layer = current_layer.find_all(xml_tag)[tag_index]
    except IndexError:
        return None
    return current_layer


def _get_last_table_containing_keys(keys: "list[str]", top_layer: BeautifulSoup):
    table: Tag
    for table in top_layer.find_all("table"):
        if not table.find("table") and __table_has_keys(keys_list=keys, table=table):
            return table
    return None


def get_table(path: list, top_layer: BeautifulSoup, keys: "list[str]") -> Tag:
    # Get the table via the specified path
    table = __get_table_via_path(path=path, top_layer=top_layer)
    if table and __table_has_keys(keys_list=keys, table=table):
        # If the table has been found and it has all the keys
        return table
    else:
        table = _get_last_table_containing_keys(keys=keys, top_layer=top_layer)
        if table:
            return table

    raise TableNotFoundError
