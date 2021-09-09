from ...constants.FILE_PATHS import FORMS_PATH, FORM_SOURCES_PATH, FORM_TYPES_PATH

__DEFAULT_SETTINGS = {
    "form_data_paths": {
        "forms_path": FORMS_PATH,
        "form_sources_path": FORM_SOURCES_PATH,
        "form_types_path": FORM_TYPES_PATH,
    },
    "mailbox_details": None,  # Requires a mailbox to login to
    "actions": {
        "post_data_to_webhook": True,
        "post_errors_to_slack": False,
        "log_parsed_data": True,
        "print_parsed_data": False,
        "delete_mail_after": False,
    }
}

__ROSSEEL_INBOX = {
    "FROM_EMAIL": "redacted",
    "FROM_PWD": "redacted",
    "SMTP_SERVER": "outlook.office365.com",
    "PORT": 993,
    "INBOX_LABEL": "INBOX",
}

ROSSEEL = {
    **__DEFAULT_SETTINGS,
    "mailbox_details": __ROSSEEL_INBOX,
    "actions": {
        "post_data_to_webhook": True,
        "post_errors_to_slack": True,
        "log_parsed_data": False,
        "print_parsed_data": False,
        "delete_mail_after": True,
    }
}

ROSSEEL_TEST = {
    **ROSSEEL,
    "actions": {
        "post_data_to_webhook": False,
        "post_errors_to_slack": False,
        "log_parsed_data": True,
        "print_parsed_data": True,
        "delete_mail_after": False,
    }
}

if __name__ == "__main__":
    print(ROSSEEL_TEST, sep="\n")
