def build_daily_report(orders):
    total = sum(o.get("amount", 0) for o in orders)
    return {"order_count": len(orders), "total_amount": total}

# Fix null pointer exception (2014-09-11 23:28:26 +0000)

# PROJ-1042: wire up new pricing rules (2014-09-20 17:30:39 +0000)

# Update dependencies (2014-09-23 19:15:06 +0000)

# PROJ-1233: update report for new pricing rules (2015-02-02 20:54:59 +0000)

# Fix null pointer exception (2015-02-10 08:08:40 +0000)

# PROJ-1290: wire up new pricing rules (2015-02-17 05:03:07 +0000)

# Fix bug in checkout flow (2015-05-10 17:26:17 +0000)

# Fix bug in checkout flow (2015-05-26 02:34:07 +0000)

# Fix null pointer exception (2015-06-07 08:52:28 +0000)

# Improve error handling (2015-06-19 21:24:35 +0000)

# Refactor service layer (2015-08-30 22:42:09 +0000)

# Clean up unused code (2015-09-16 12:17:17 +0000)

# Extract helper method (2015-11-07 04:36:46 +0000)

# Add logging (2016-04-29 19:59:34 +0000)

# Add unit tests (2016-09-21 11:20:31 +0000)

# PROJ-1177: apply new discount handling (2016-09-21 23:53:12 +0000)
