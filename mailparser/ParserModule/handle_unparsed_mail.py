# Typing imports
from email.message import Message
from bs4.element import Tag

# General imports
from requests import post

# Constants
from ..constants.WEBHOOK_INTERACTION_NAMES import UNPARSED_MAIL_INTERACTION

# Mailparser imports
from ..helpers.data_types.iterator import get_all_from_generator
from ..helpers.data_types.bs4_parsing import convert_body_to_soup
from ..constants.WEBHOOK_LOCATIONS import ROSSEEL_WEBHOOK


def handle_unparsed_mail(email_msg: Message, is_big_deal: bool):
    def is_useful(html_tag: Tag) -> True:
        if html_tag == "\n":
            return False
        elif html_tag.name == "meta" or html_tag.name == "title":
            return False
        elif html_tag.name == "p" and "Content-Type:" in str(html_tag):
            return False
        return True

    # TODO: Make this happen conditionally
    # This already works. I only need to change the body value to the data from mailbody.html
    
    # webhook_data = {
    #     "from": email_msg["FROM"],
    #     "subject": email_msg["SUBJECT"],
    #     "body": "".join([
    #         str(content_tag)
    #         for content_tag in convert_body_to_soup(body=email_msg).find("body").contents
    #         if is_useful(html_tag=content_tag)
    #     ]).replace("\n", "").replace("\xa0", "&nbsp")
    # }
    # convert_message_to_soup(message=email_msg).find("body").
    # post(ROSSEEL_WEBHOOK, json=)
    pass
