from .forms import FormSpecsCollection


class Reference:

    def __init__(self, forms_path: str = None, form_types_path: str = None) -> None:
        # Assign the file locations or use the default locations
        if not forms_path and not form_types_path:
            self.FILE_LOCATIONS = ("default", "default")
            reference_data = FormSpecsCollection()
        elif forms_path and form_types_path:
            self.FILE_LOCATIONS = (forms_path, form_types_path)
            reference_data = FormSpecsCollection(
                forms_path=forms_path,
                form_types_path=form_types_path
            )
        else:
            raise AssertionError(f"expected 2x truthy or falsy, got: forms_path: {forms_path} and form_types_path: {form_types_path}")  # nopep8

        self.sources = reference_data.sources

        forms_by_source = {}
        for source in self.sources:
            forms_by_source[source] = reference_data._get_forms_by_source(source)  # nopep8

        print(forms_by_source)

        # self.forms: dict = reference_data["forms"]  # ! changeme
        # self.required_fields = reference_data["requiredFields"]

        # self.companies = [form["company"] for form in self.forms]

    def __repr__(self) -> str:
        repr_list = [f"Reference("]
        repr_list.append(f" file_paths: {self.FILE_LOCATIONS}")
        repr_list.append(f" form sources: {self.sources}")
        repr_list.append(")")
        return "\n".join(repr_list)

    def get_form_details_by_company(self, company: str) -> dict:
        for form in self.forms:
            form_company = form["company"]
            if form_company == company:
                form_copy = form.copy()
                del form_copy["company"]
                return form_copy

    def has_all_required_fields(self, details: dict):
        for key, required in self.required_fields.items():
            value = details.get(key)
            if required:
                if not value:
                    return False
            elif not value:
                details[key] = ""
        return True


if __name__ == "__main__":
    Reference()
