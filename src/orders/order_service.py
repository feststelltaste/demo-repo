from src.orders.order_validation import validate_order_input


def place_order(data):
    errors = validate_order_input(data)
    if errors:
        raise ValueError(", ".join(errors))
    return {"status": "placed", "email": data["email"]}

# Clean up unused code (2014-07-20 15:06:56 +0000)
