def format_greeting(name):
    if not name:
        name = "there"
    return f"Hi {name}, thanks for your order!"


def render_order_confirmation(order):
    greeting = format_greeting(order.get("customer_name"))
    return f"{greeting}\n\nYour order #{order.get('id')} is confirmed."

# PROJ-1290: wire up new pricing rules (2014-09-30 06:44:08 +0000)

# Update documentation (2014-12-13 21:27:13 +0000)

# Refactor service layer (2014-12-26 19:06:54 +0000)

# PROJ-1233: wire up new pricing rules (2015-03-04 00:30:07 +0000)

# Add logging (2015-06-24 11:29:44 +0000)

# Fix flaky test (2015-09-01 19:22:56 +0000)

# Improve performance (2015-10-08 06:11:29 +0000)
