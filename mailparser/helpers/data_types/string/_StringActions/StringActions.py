from re import findall as regex_findall
# TODO: Add other string manipulation methods
# TODO: Change .action_types.json to a MD file


class StringActionsClass():
    def __init__(self):
        self.string: str = None

    def __repr__(self) -> str:
        return self.string

    def assign_and_perform(self, string: str, actions: "list[dict[str, str | int]]"):
        self.assign_string(string)
        return self.perform(actions)

    def assign_string(self, string: str):
        self.string = string.strip()
        return self

    def perform(self, actions: "list[dict[str, str | int | dict]]") -> str:
        assert self.string is not None, "You should assign a string first before you can alter it"
        if actions:
            # Copy the actions so that they don't get altered globally
            # TODO: find a better solution
            actions_copy = [action.copy() for action in actions]
            for action in actions_copy:
                action_type = action.pop("action")
                if action_type == "capitalise":
                    self._captitalise()
                elif action_type == "split":
                    self._split(action)
                elif action_type == "regex":
                    self._regex(action)
                elif action_type == "phonenumiphy":
                    self._phonenumiphy()

        altered_string = self.string
        # remove string from memory
        self.string = None
        return altered_string

    def _split(self, kwargs: dict):
        after_actions: list[dict] = kwargs.pop("afterActions", None)
        altered_string = self.string.split(**kwargs)

        # TODO: find a better solution (same as above)
        after_actions_copy = [a_action.copy() for a_action in after_actions]
        for action in after_actions_copy:
            action_type = action.pop("action")
            if action_type == "slice":
                begin_index = action["beginIndex"] or 0
                end_index = action["endIndex"] or len(altered_string)
                altered_string = altered_string[begin_index:end_index]  # nopep8

        self.string = altered_string
        return self

    def _regex(self, kwargs: dict):
        self.string = regex_findall(kwargs["pattern"], self.string)[kwargs["match_index"]]  # nopep8

    def _captitalise(self):
        self.string = self.string.title()

    def _phonenumiphy(self):
        # BELGIAN_PHONE_NUMBER_LENGTH = 10 (reference)
        phone_number = self.string
        phone_number_length = len(phone_number)

        # Belgian mobile phone (numbers based on the phone number length reference)
        if phone_number_length == 10 and phone_number[:2] == "04":
            phone_number = phone_number.replace("04", "+324", 1)
        elif phone_number_length == 9 and phone_number[0] == "4":
            phone_number = phone_number.replace("4", "+324", 1)
        elif phone_number_length == 13 and phone_number[:4] == "0032":
            phone_number = phone_number.replace("0032", "+324", 1)

        # Belgian home telephone
        elif phone_number_length == 8 and phone_number[0] == "9":
            phone_number = phone_number.replace("9", "09", 1)

        self.string = phone_number


StringActions = StringActionsClass()


if __name__ == "__main__":
    print(StringActions.assign_and_perform(
        string="0486165184",
        actions=[
            {
                "action": "phonenumiphy"
            }
        ]
    ))
