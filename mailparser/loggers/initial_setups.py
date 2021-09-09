def setup_loggers():
    from logging.config import dictConfig
    from json import load
    from ..constants.CONFIG_PATHS import LOGGING_CONFIG_PATH

    with open(LOGGING_CONFIG_PATH, "r") as f:
        dictConfig(load(f))

    add_CustomHandlers()


def add_CustomHandlers():
    """Adds CustomHandler classes to certain logger instances"""
    from .CustomHandlers import RosseelWebhookHandler, SlackErrorHandler
    from .LOGGER_INSTANCES import ROSSEEL_POSTER, SLACK_POSTER, ERROR_LOGGER

    ROSSEEL_POSTER.addHandler(RosseelWebhookHandler)
    SLACK_POSTER.addHandler(SlackErrorHandler)


class ActionSettings:
    def __init__(self, actions: "dict[str, bool]") -> None:
        self.actions = actions

    def get_action(self, action_name: str, default_value=False, return_reversed=True) -> bool:

        action_bool = self.actions.get(action_name, default_value)
        assert isinstance(action_bool, bool), f"{action_bool} is not of type bool"  # nopep8
        return not action_bool if return_reversed else action_bool


def activate_loggers(action: "dict[str, bool]"):
    """
    Will activate the loggers:\n
    SLACK_POSTER, ROSSEEL_POSTER, PARSED_DATA_FILE_LOGGER, PARSED_DATA_CONSOLE_LOGGER

    based on the attributes:\n
    post_errors_to_slack, post_data_to_webhook, log_parsed_data, print_parsed_data
    """

    from .LOGGER_INSTANCES import ERROR_LOGGER, ROSSEEL_POSTER, PARSED_DATA_FILE_LOGGER, PARSED_DATA_CONSOLE_LOGGER

    action_settings = ActionSettings(actions=action)

    # slack
    if action_settings.get_action("post_errors_to_slack"):
        from .CustomHandlers import SlackErrorHandler
        ERROR_LOGGER.addHandler(SlackErrorHandler)

    # rosseel
    ROSSEEL_POSTER.disabled = action_settings.get_action(
        "post_data_to_webhook")

    # logfile
    PARSED_DATA_FILE_LOGGER.disabled = action_settings.get_action(
        "log_parsed_data")

    # print
    PARSED_DATA_CONSOLE_LOGGER.disabled = action_settings.get_action("print_parsed_data")  # nopep8
