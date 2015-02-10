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

# Extract helper method (2014-11-03 03:13:39 +0000)

# Fix null pointer exception (2014-11-18 07:19:42 +0000)

# Tighten phone number validation (2014-12-08 23:10:22 +0000)

# Rename variables for clarity (2015-01-13 17:26:38 +0000)

# Add validation for new field format (2015-02-01 10:37:55 +0000)

# Fix email validation regex (2015-02-10 04:51:29 +0000)
