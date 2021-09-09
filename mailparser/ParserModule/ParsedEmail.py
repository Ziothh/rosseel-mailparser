# Type imports
from email.message import Message
from ..helpers.data_types.message import get_message_body
from ..helpers.data_types.string import dump_str_to_file

# Constants
from ..constants.FILE_PATHS import FORMS_PATH, FORM_TYPES_PATH
from ..constants.FILE_PATHS.TEMP_PATHS import TEMP_MAILBODY_DUMPFILE_PATH

# General imports
from ..helpers.forms import Forms
from ..helpers.data_types.bs4_parsing import get_table, convert_body_to_soup, parse_table
from ..helpers.forms import get_keys_from_formFields

# Error types
from ..helpers.errors import FormSourceNotFoundError, ParsingError, TableNotFoundError

# ParsedEmail Class
from .ParsedData import ParsedData

# Loggers
from ..loggers.LOGGER_INSTANCES import TABLE_LOGGER


class ParsedEmail:
    FORMS_DATA = Forms(FORMS_PATH, FORM_TYPES_PATH)

    def __init__(self, email_msg: Message):
        # Convert the message payload to a string
        msg_body = get_message_body(email_msg) 
        
        # Temporary backup of the mail body 
        # Is used when the unparsed mail is send over to the webhook
        dump_str_to_file(string=msg_body, file_location=TEMP_MAILBODY_DUMPFILE_PATH) 
        
            
        # Get the source via the email address or the subject
        self.mail_source: str = email_msg["from"]
        self.subject = email_msg["subject"]
        
        # TODO: Fix this
        #  * This is for catching a bug where the header and body aren't separated in the mail data
        # Thus resulting in the email lib not being able to get the subject and sender from the data
        # ? Maybe try message_from_bytes instead of message_from_string ?
        # if (self.subject == None):
        #     print("subj")
        #     pass
        # elif (self.mail_source == None):
        #     print("src")
        #     pass
        
        self.source = self.__check_source()

        self.type: str  # will be specified after the parsing of the mail

        # Get all the form_types from that source
        self.form_types_from_source = ParsedEmail.FORMS_DATA.get_forms_by_source(self.source)  # nopep8

        self.mail_body = convert_body_to_soup(msg_body).find("body")
        
        self.parsed_data = self.__parse_mail()

    def __repr__(self) -> str:
        repr_string = "Data fetched from the e-mail:\n"
        repr_string += f"\nSource: {self.source}\n"
        for key, value in self.parsed_data.items():
            repr_string += f"\n{key.ljust(15)} {value}"
        return repr_string

    def __str__(self) -> str:
        repr_string = ""
        for key, value in self.parsed_data.items():
            repr_string += f"\n{key.ljust(15)} {value}"
        return repr_string

    def __check_source(self):
        """
        Will check the mail source by first looking at the sender.

        If that doesn't work it will look at the subject.
        """
        def source_in_string(source: str, string: str) -> True:
            source = source.lower()
            string = string.lower().replace(" ", "").replace("-", "")

            if "-" in source:
                source_bits = source.split("-")
            elif " " in source:
                source_bits = source.split(" ")
            else:
                source_bits = [source]

            for bit in source_bits:
                if bit not in string:
                    return False
            return True

        companies = ParsedEmail.FORMS_DATA.sources

        # Check the mail source first
        try:
            return [
                source for source in companies if source_in_string(source, self.mail_source)
            ].pop()
        except IndexError:
            # If that doesn't work: try the mail subject
            try:
                return [
                    source for source in companies if source_in_string(source, self.subject)
                ].pop()
            except IndexError:
                raise FormSourceNotFoundError(self.mail_source) from None

    def __parse_mail(self) -> "dict[str, str]":
        for form_type in self.form_types_from_source:
            path = form_type.path
            form_fields = form_type.formFields

            form_keys = get_keys_from_formFields(form_fields)
            try:
                table = get_table(
                    path=path["toTable"],
                    top_layer=self.mail_body,
                    keys=form_keys
                )
            except TableNotFoundError:
                TABLE_LOGGER.warn(
                    "Table has not been found from source: %s\n\n%s",
                    self.source,
                    self.mail_body
                )
            else:
                # Just loop trough every table and find the one with content
                parsed_data = parse_table(
                    table=table,
                    form_fields=form_type.formFields,
                    keys=form_keys,
                    path=path
                )

                if form_type.ParsedMail_has_all_required_data(parsed_data):
                    parsed_data["Source"] = self.source
                    parsed_data["interaction"] = form_type.webhookInteraction
                    return ParsedData(parsed_data)

        raise ParsingError(
            f"Parsing mail from company \"{self.source}\" failed"
        )


if __name__ == "__main__":
    ParsedEmail()
