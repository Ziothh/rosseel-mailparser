import logging


# Error Loggers
ERROR_LOGGER = logging.getLogger("error")  # logs to error files
SLACK_POSTER = logging.getLogger("slack")  # posts to slack

# General Loggers
PARSED_DATA_CONSOLE_LOGGER = logging.getLogger("parsedDataConsoleLogger")
PARSED_DATA_FILE_LOGGER = logging.getLogger("parsedDataFileLogger")
ROSSEEL_POSTER = logging.getLogger("rosseel")

# Debug Loggers
DEBUG_LOGGER = logging.getLogger("debug")
TABLE_LOGGER = logging.getLogger("tableLogger")

DEBUG_LOGGER.disabled = True
TABLE_LOGGER.disabled = True
