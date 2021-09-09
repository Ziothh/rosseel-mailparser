from email.message import Message
from .message_body import get_message_body
from ....constants.FILE_PATHS.TEMP_PATHS import TEMP_MAILBODY_DUMPFILE_PATH

def dump_message_to_file(msg):
    with open(TEMP_MAILBODY_DUMPFILE_PATH, "w", encoding="utf-8") as f:
        f.write(get_message_body(msg))
        
def get_message_from_tempfile(msg: Message) -> str:
    with open(TEMP_MAILBODY_DUMPFILE_PATH, "r") as f:
        return f.read()