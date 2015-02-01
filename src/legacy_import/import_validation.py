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

# Fix flaky test (2014-07-31 08:30:10 +0000)

# Add unit tests (2014-11-03 20:50:44 +0000)

# Tighten phone number validation (2014-12-08 23:10:22 +0000)

# Add validation for new field format (2015-02-01 10:37:55 +0000)
