from email.message import Message

def get_message_body(msg: Message) -> str:
    return msg._payload[1]._payload if msg.is_multipart() else msg._payload