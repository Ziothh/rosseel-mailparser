from imaplib import IMAP4_SSL


def fetch_mailIDs_from_inbox(FROM_EMAIL: str, FROM_PWD: str, SMTP_SERVER: str, PORT: str, INBOX_LABEL: str) -> "tuple[IMAP4_SSL, list[bytes]]":
    """Logs in to the specified mailbox and returns a tuple(IMAP4_SSL, id_list)"""

    if PORT is not None:
        mail = IMAP4_SSL(SMTP_SERVER, PORT)
    else:
        mail = IMAP4_SSL(SMTP_SERVER)

    mail.login(FROM_EMAIL, FROM_PWD)
    mail.select(INBOX_LABEL)

    _, data = mail.search(None, 'ALL')

    mail_ids = data
    id_list: list[bytes] = mail_ids[0].split(b' ')

    return (mail, id_list)
