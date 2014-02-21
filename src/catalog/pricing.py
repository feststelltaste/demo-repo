TAX_RATE = 0.19


def calculate_tax(net_amount):
    return round(net_amount * TAX_RATE, 2)


def calculate_gross_price(net_amount):
    return round(net_amount + calculate_tax(net_amount), 2)


def apply_discount(net_amount, percentage):
    return round(net_amount * (1 - percentage / 100), 2)
