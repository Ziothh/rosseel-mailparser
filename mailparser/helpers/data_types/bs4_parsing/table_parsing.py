from .__basic_imports import Tag
from ..string import StringActions
from ...forms.form_helpers import get_key_data
from ...errors import KeyNotFoundError


def __get_td_text_from_td_list(td_list: "list[Tag]", td_list_index: int, container_with_text: "tuple[str, int]") -> str:
    td = td_list[td_list_index]

    if container_with_text is None:
        text_container = td
    else:
        container_tag, nth_index = container_with_text
        text_container: Tag = td.findAll(container_tag)[nth_index]

    return text_container.text


def parse_table(table: Tag, form_fields: dict, keys: "list[str]", path: dict) -> "dict[str, str]":
    parsed_data = {}

    tr: Tag
    for tr in table.find_all("tr"):
        tds = tr.find_all("td")

        try:
            # get key and value
            key = __get_td_text_from_td_list(td_list=tds, td_list_index=path["keyTdIndex"], container_with_text=path["containerWithText"])  # nopep8
            value = __get_td_text_from_td_list(td_list=tds, td_list_index=path["valueTdIndex"], container_with_text=path["containerWithText"])  # nopep8
        except IndexError:  # If the row doesn't have enough tds, just go to the next one
            continue
        else:
            try:
                key_data = get_key_data(form_fields=form_fields, raw_key=key)
            except KeyNotFoundError:
                continue
            else:
                # Rename the key if renamedKey is not None
                key = key_data["renamedKey"]
                # Edit the value string
                value = StringActions.assign_and_perform(
                    string=value,
                    actions=key_data["valueActions"]
                )

                # If the key == "Naam" split it to "Voornaam" and "Achternaam"
                if key == "Naam":
                    parsed_data["Voornaam"] = value[0]
                    parsed_data["Achternaam"] = "".join(value[1:])
                else:
                    parsed_data[key] = value
    return parsed_data
