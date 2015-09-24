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

# Update documentation (2014-07-30 19:47:31 +0000)

# Improve error handling (2014-08-07 18:35:12 +0000)

# Update documentation (2014-09-25 10:25:29 +0000)

# Clean up unused code (2014-10-14 08:25:13 +0000)

# PROJ-1042: wire up new pricing rules (2014-11-04 16:00:05 +0000)

# Improve performance (2015-01-22 12:41:37 +0000)

# Fix bug in checkout flow (2015-01-25 19:46:06 +0000)

# Fix bug in checkout flow (2015-04-02 21:04:36 +0000)

# Update dependencies (2015-07-27 06:27:38 +0000)

# Fix flaky test (2015-09-24 08:17:59 +0000)
