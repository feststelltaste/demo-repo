def format_greeting(name):
    if not name:
        name = "there"
    return f"Hi {name}, thanks for your order!"


def render_order_confirmation_sms(order):
    greeting = format_greeting(order.get("customer_name"))
    return f"{greeting} Order #{order.get('id')} confirmed."

# Add new feature (2015-01-06 21:18:51 +0000)

# Fix null pointer exception (2015-01-10 09:23:52 +0000)

# Update documentation (2015-07-21 16:09:57 +0000)
