TAX_RATE = 0.19


def calculate_tax(net_amount):
    return round(net_amount * TAX_RATE, 2)


def calculate_gross_price(net_amount):
    return round(net_amount + calculate_tax(net_amount), 2)


def apply_discount(net_amount, percentage):
    return round(net_amount * (1 - percentage / 100), 2)

# PROJ-1042: update report for new pricing rules (2014-03-19 08:52:23 +0000)

# Fix bug in checkout flow (2014-06-30 23:54:17 +0000)

# Improve error handling (2014-10-12 09:06:01 +0000)

# Fix null pointer exception (2014-10-19 06:11:49 +0000)

# Update documentation (2014-11-22 19:08:14 +0000)
