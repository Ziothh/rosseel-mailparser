# Used to decode the mail bytes from Quoted-Printable
from quopri import decodestring

from ..constants.FILE_PATHS.TEMP_PATHS import TEMP_MAILBODY_DUMPFILE_PATH

from ..loggers.LOGGER_INSTANCES import (
    ERROR_LOGGER,
    ROSSEEL_POSTER,
    PARSED_DATA_CONSOLE_LOGGER,
    PARSED_DATA_FILE_LOGGER,
    DEBUG_LOGGER,
)
from ..loggers import activate_loggers

from .ParsedData import ParsedData
from .handle_unparsed_mail import handle_unparsed_mail


class Parser:
    def __init__(self, parser_settings: dict):
        # First, set up the actions when a mail get parsed
        activate_loggers(parser_settings["actions"])

        self.mailbox_details: dict = parser_settings["mailbox_details"]
        self.form_data_paths: dict[str, str] = parser_settings[
            "form_data_paths"
        ]  # nopep8
        self.delete_mail_after: bool = parser_settings["actions"]["delete_mail_after"]

    def _perform_actions_after_parsing(self, parsed_data: ParsedData, mail_id: str):
        """
        Performs the actions specified in SETTINGS.py.

        The function activate_loggers in self.__init__ already disabled the
        actions that don't have to be executed.
        """
        ROSSEEL_POSTER.info(parsed_data.get())
        parsed_data_str = str(parsed_data)

        PARSED_DATA_CONSOLE_LOGGER.info("%s\n", parsed_data_str)
        PARSED_DATA_FILE_LOGGER.info("%s\n", parsed_data_str)

        if self.delete_mail_after:
            self.mailbox.store(mail_id, "+FLAGS", "\\DELETED")
            self.mailbox.expunge()

    def parse_mailbox(self):
        from email import message_from_string, message_from_bytes

        from .ParsedEmail import ParsedEmail
        from ..helpers.mailboxModule import fetch_mailIDs_from_inbox
        from ..helpers.errors import (
            ParsingError,
            EmptyMailboxError,
            FormSourceNotFoundError,
        )

        self.mailbox, id_list = fetch_mailIDs_from_inbox(
            **self.mailbox_details
        )  # nopep8
        try:
            first_email_id = int(id_list[0])
            latest_email_id = int(id_list[-1])
        except (ValueError, IndexError):
            raise EmptyMailboxError

        # Goes over all the mails from last to first
        for mail_id in range(first_email_id, latest_email_id):
            mail_id = str(mail_id)

            # data's content: [b'(id (RFC822{number}', message body bytes), b'FLAGS(...)']
            _, data = self.mailbox.fetch(mail_id, "(RFC822)")

            # INFO:
            # Actual mail data: data[0][1]
            # Encoding: Quoted-Printable
            # Decode with utf-8 if UnicodeDecodeError: decode with latin1
            try:
                msg_str = str(
                    decodestring(data[0][1]),
                    errors="replace", # When UnicodeDecodeError: will cause an error that's caught in the except
                    encoding="utf-8",
                )
            except (TypeError, UnicodeDecodeError):
                msg_str = str(
                    decodestring(data[0][1]),
                    errors="replace",
                    encoding="latin1",
                )
            
            msg = message_from_string(s=msg_str)

            try:
                # Mail gets parsed and returns a ParsedEmail instance
                # parsed_email.parsed_data will contain the parsed data
                parsed_email = ParsedEmail(email_msg=msg)
            except FormSourceNotFoundError as e:
                # Not that important
                handle_unparsed_mail(email_msg=msg, is_big_deal=False)

                ERROR_LOGGER.warn("%s: %s", e.__class__.__name__, str(e))  # nopep8
            except ParsingError as e:
                # Big problem
                # handle_unparsed_mail(email_msg=msg, is_big_deal=True)
                print("ayo")
                ERROR_LOGGER.error(e, exc_info=True)
            else:
                self._perform_actions_after_parsing(
                    parsed_data=parsed_email.parsed_data, mail_id=mail_id
                )

        self.mailbox.close()
        self.mailbox.logout()
