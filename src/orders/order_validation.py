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
