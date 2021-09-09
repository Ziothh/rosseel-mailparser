OVERWRITES = {
    "--noprint": {
        "path": ["actions", "print_parsed_data"],
        "value": False
    },
    "--nolog": {
        "path": ["actions", "log_parsed_data"],
        "value": False
    },
    "--nodelete": {
        "path": ["actions", "delete_mail_after"],
        "value": False
    },
    "--nopost": {
        "path": ["actions", "post_data_to_webhook"],
        "value": False
    },
    "--noslack": {
        "path": ["actions", "post_errors_to_slack"],
        "value": False
    },
}


def overwrite_settings(args: "list[str]", settings: dict) -> dict:
    from ...launcher import raise_argsError

    for arg in args:
        try:
            path, value = OVERWRITES[arg].values()
        except KeyError:
            raise_argsError(message=f"\"{arg}\" is not a valid argument.")
        else:
            if len(path) == 1:
                settings[path[0]] = value
            elif len(path) == 2:
                settings[path[0]][path[1]] = value
            else:
                raise NotImplementedError(f"Argument settings path of length {len(path)} is not supported")  # nopep8
    return settings
