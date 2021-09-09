from ..data_types.json import JSONFile
from ..errors import ParsingError


class Form:
    def __init__(self, kwargs: dict):
        self.type: str  # Form type
        self.source: str
        self.typeSpecs: dict = None
        self.formFields: list[dict]
        self.path: dict  # Path to the table that's to be parsed
        self.webhookInteraction: str  # Name of the interaction (see: DB)

        set_attributes: list[str] = []
        for key, value in kwargs.items():
            set_attributes.append(key)
            setattr(self, key, value)
        set_attributes.append("typeSpecs")  # Will be set in the Forms class
        self.__set_attributes: list[str] = set_attributes

    def __repr__(self) -> str:
        form_attrs = '\n'.join([f'{key}: {getattr(self,key)}' for key in self.__set_attributes])  # nopep8
        return f"Form(\n{form_attrs}\n)"

    def ParsedMail_has_all_required_data(self, data: dict) -> bool:
        """
        Will loop over all the keys based om the type from formTypes.json.\\
        Raises an error if: 
            > It misses a key\\
            > The key value is falsy and valuesMustBeTruthy specifies it must be truthy
        Else it will return True
        """
        errors = []
        for key, truthy in self.typeSpecs["valuesMustBeTruthy"].items():
            try:
                key_value = data[key]
            except KeyError:
                errors.append(f"Missing key: \"{key}\"")  # nopep8
            else:
                if truthy and not key_value:
                    errors.append(f"The value from key: \"{key}\" equalts to {key_value}")  # nopep8
                elif not isinstance(key_value, str):
                    errors.append(f"The value from key \"{key}\" is of type {type(key_value)} and equals to {key_value}")  # nopep8
        if len(errors) == 0:
            return True
        else:
            raise ParsingError(
                f"Errors while parsing mail from {self.source}:\n"
                + "\n".join(errors)
            )


class Forms:
    def __init__(self, forms_path: str, form_types_path: str):
        self.forms_path = forms_path
        self.form_types_path = form_types_path

        # Fetching a list of all of the Forms from forms.json
        self.FORMS = [Form(form_data) for form_data in JSONFile(self.forms_path).read()]  # nopep8
        form_types: list[dict] = JSONFile(self.form_types_path).read()

        # Assigning typeSpecs to each Form
        for form in self.FORMS:
            for form_type in form_types:
                if form.type == form_type["type"]:
                    form_type_copy = form_type.copy()
                    del form_type_copy["type"]
                    form.typeSpecs = form_type_copy

        # Getting a list of all the possible sources
        all_sources: set[str] = set()
        for form in self.FORMS:
            all_sources.add(form.source)

        self.sources = all_sources

    def get_forms_by_source(self, source: str):
        return [form for form in self.FORMS if form.source == source]

    def __repr__(self) -> str:
        forms_str = '\n\n'.join([str(form) for form in self.FORMS])
        return f"Forms(\n{forms_str}\n)"


if __name__ == "__main__":
    from pprint import pprint
    from ...constants.FILE_PATHS import FORMS_PATH, FORM_TYPES_PATH

    forms = Forms(FORMS_PATH, FORM_TYPES_PATH)
    print(forms.get_forms_by_source("immoProxio"))
    # print(a.sources)
