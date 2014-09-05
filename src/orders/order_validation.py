import re

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
PHONE_RE = re.compile(r"^\+?[0-9\-\s]{7,15}$")


def validate_email(value):
    if not value:
        return False
    return bool(EMAIL_RE.match(value))


def validate_phone(value):
    if not value:
        return False
    return bool(PHONE_RE.match(value))


def validate_order_input(data):
    errors = []
    if not validate_email(data.get("email")):
        errors.append("invalid email")
    if not validate_phone(data.get("phone")):
        errors.append("invalid phone")
    return errors

# Update dependencies (2014-03-03 14:19:35 +0000)

# Fix email validation regex (2014-03-18 23:59:49 +0000)

# Fix null pointer exception (2014-06-19 05:15:49 +0000)

# Add unit tests (2014-09-05 01:47:45 +0000)
