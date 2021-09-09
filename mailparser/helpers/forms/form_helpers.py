from ..errors import KeyNotFoundError


def get_keys_from_formFields(form_fields: "list[dict]") -> "list[str]":
    return [form_field["keyNames"] for form_field in form_fields]


def get_key_data(form_fields: "list[dict]", raw_key: str) -> dict:
    for form_field in form_fields:
        for keyName in form_field["keyNames"]:
            if keyName in raw_key:
                return form_field
    raise KeyNotFoundError(f"The key {raw_key} is was not found in form_fields")  # nopep8
