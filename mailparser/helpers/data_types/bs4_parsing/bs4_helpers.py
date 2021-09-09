from .__basic_imports import Message, BeautifulSoup, Tag
from ..iterator import get_nth_from_generator
from ...errors import KeyNotFoundError
from ..message import get_message_body


def convert_body_to_soup(body: str) -> BeautifulSoup:
    return BeautifulSoup(body, "lxml")


def __get_nth_child(container: Tag, n: int):
    return get_nth_from_generator(iterator=container.children, n=n)


def __get_key_from_text(text: str, desired_keys: "list[str]") -> str:
    """Tries to see if the text has one of the desired_keys and returns it. Else it'll raise a KeyNotFoundError"""
    text = text.lower()
    for key in desired_keys:
        if key.lower() in text:
            return key
    raise KeyNotFoundError
