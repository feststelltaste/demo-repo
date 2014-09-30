def format_greeting(name):
    if not name:
        name = "there"
    return f"Hi {name}, thanks for your order!"


def render_order_confirmation(order):
    greeting = format_greeting(order.get("customer_name"))
    return f"{greeting}\n\nYour order #{order.get('id')} is confirmed."

# PROJ-1290: wire up new pricing rules (2014-09-30 06:44:08 +0000)
