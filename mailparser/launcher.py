from .config.launcher_config import LAUNCH_PROFILES
from .ParserModule import Parser


def get_all_profile_names(toString: bool):
    profile_keys = LAUNCH_PROFILES.keys()
    return f"[{', '.join(profile_keys)}]" if toString else profile_keys


def raise_argsError(message: str, include_options: bool = False):
    from .helpers.errors._CustomErrors import LaunchArgumentsError
    error_message = ["!Argument Error", message]
    if include_options:
        error_message.append(f"Possible modes are {get_all_profile_names(toString=True)}")  # nopep8
    raise LaunchArgumentsError("\n".join(error_message))


class MailparserLauncher():
    def __init__(self, launch_args: "list[str]"):

        if len(launch_args) == 0:
            raise_argsError(message="You have to specify a launch mode.", include_options=True)  # nopep8

        self.args = launch_args
        self.profile = self.__get_profile()

    def start(self):
        from .config.launcher_config import overwrite_settings

        settings = self.profile["settings"]
        if len(self.args) != 0:
            settings = overwrite_settings(args=self.args, settings=settings)
        print(self.profile["running_message"])

        parser_instance = Parser(parser_settings=self.profile["settings"])
        parser_instance.parse_mailbox()

    def __args_toString(self):
        return " ".join(self.args)

    def __get_profile(self):
        try:
            return LAUNCH_PROFILES[self.args.pop(0)]
        except KeyError:
            raise_argsError(message="Wrong launche mode.", include_options=True)  # nopep8

    def __repr__(self) -> str:
        return f"Launcher({self.__args_toString()})"
