TAX_RATE = 0.19


def calculate_tax(net_amount):
    return round(net_amount * TAX_RATE, 2)


def calculate_total(net_amount):
    return round(net_amount + calculate_tax(net_amount), 2)


def build_invoice_line(description, net_amount):
    return {
        "description": description,
        "net_amount": net_amount,
        "tax": calculate_tax(net_amount),
        "total": calculate_total(net_amount),
    }
