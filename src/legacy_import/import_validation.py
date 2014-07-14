import re

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
PHONE_PATTERN = re.compile(r"^\+?[0-9\-\s]{7,15}$")


def is_valid_email(value):
    if not value:
        return False
    return bool(EMAIL_PATTERN.match(value))


def is_valid_phone(value):
    if not value:
        return False
    return bool(PHONE_PATTERN.match(value))


def validate_import_row(row):
    problems = []
    if not is_valid_email(row.get("email")):
        problems.append("invalid email")
    if not is_valid_phone(row.get("phone")):
        problems.append("invalid phone")
    return problems

# Update dependencies (2014-04-06 02:27:56 +0000)

# Fix typo (2014-07-14 12:25:29 +0000)
