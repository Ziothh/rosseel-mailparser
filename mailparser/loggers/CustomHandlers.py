from logging import ERROR, Handler, INFO, Formatter, LogRecord
import requests
from ..constants.WEBHOOK_LOCATIONS import SLACK_WEBHOOK, ROSSEEL_WEBHOOK


# class SlackParsedDataHandlerClass(Handler):
#     # Maybe add styling?
#     def emit(self, record: LogRecord):
#         # msg is supposed to be a dict
#         record.msg = "\n".join([f"{key}: {value}" for key, value in record.msg.items()])  # nopep8
#         log_entry = self.format(record)
#         URL = SLACK_WEBHOOK
#         return requests.post(URL, json={"text": str(log_entry)}).content


class SlackErrorHandlerClass(Handler):
    # Maybe add styling? -> see slack api
    URL = SLACK_WEBHOOK

    def emit(self, record: LogRecord):
        log_entry = self.format(record)
        return requests.post(self.URL, json={"text": str(log_entry)}).content


class RosseelWebhookHandlerClass(Handler):
    URL = ROSSEEL_WEBHOOK

    def emit(self, record: LogRecord):
        return requests.post(self.URL, json=record.msg).content


SlackErrorHandler = SlackErrorHandlerClass(level=ERROR)
SlackErrorHandler.setFormatter(Formatter("%(asctime)s - %(name)s - %(levelname)s\n%(message)s", datefmt="%d-%m-%Y %H:%M:%S"))  # nopep8


RosseelWebhookHandler = RosseelWebhookHandlerClass(level=INFO)
RosseelWebhookHandler.setFormatter(Formatter("%(message)s"))
