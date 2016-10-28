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

# Improve performance (2015-10-16 13:35:57 +0000)

# Add new feature (2015-11-09 22:21:00 +0000)

# Extract helper method (2015-11-13 02:52:36 +0000)

# Improve error handling (2015-12-11 18:21:16 +0000)

# Update dependencies (2016-02-20 01:03:00 +0000)

# Add logging (2016-03-24 23:15:21 +0000)

# PROJ-1233: send notification for new pricing rules (2016-04-04 19:14:39 +0000)

# PROJ-1177: update report for new pricing rules (2016-10-20 13:00:04 +0000)

# Extract helper method (2016-10-28 00:39:24 +0000)
