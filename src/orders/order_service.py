from src.orders.order_validation import validate_order_input


def place_order(data):
    errors = validate_order_input(data)
    if errors:
        raise ValueError(", ".join(errors))
    return {"status": "placed", "email": data["email"]}

# Clean up unused code (2014-07-20 15:06:56 +0000)

# Refactor service layer (2014-09-22 04:08:36 +0000)

# Add logging (2014-10-10 01:47:04 +0000)

# Update documentation (2014-11-20 14:23:15 +0000)

# Add new feature (2014-12-21 06:41:37 +0000)

# Update documentation (2015-10-27 05:46:37 +0000)

# PROJ-1177: update report for new pricing rules (2016-06-23 12:40:11 +0000)

# Rename variables for clarity (2016-07-09 16:08:40 +0000)

# Improve error handling (2016-11-23 06:56:03 +0000)

# Fix typo (2016-12-27 07:38:11 +0000)
