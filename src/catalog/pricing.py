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

# Fix flaky test (2014-11-24 00:10:02 +0000)

# Improve performance (2014-12-24 05:46:17 +0000)

# Fix flaky test (2015-06-01 01:05:20 +0000)

# Fix bug in checkout flow (2015-08-08 06:58:23 +0000)

# Add unit tests (2015-09-02 11:30:36 +0000)

# Update documentation (2015-10-16 14:20:17 +0000)

# Extract helper method (2015-12-01 04:35:48 +0000)

# Add unit tests (2015-12-29 16:59:57 +0000)

# Fix flaky test (2016-03-01 08:43:50 +0000)
