def format_greeting(name):
    if not name:
        name = "there"
    return f"Hi {name}, thanks for your order!"


def render_order_confirmation_sms(order):
    greeting = format_greeting(order.get("customer_name"))
    return f"{greeting} Order #{order.get('id')} confirmed."
