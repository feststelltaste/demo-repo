def build_daily_report(orders):
    total = sum(o.get("amount", 0) for o in orders)
    return {"order_count": len(orders), "total_amount": total}

# Fix null pointer exception (2014-09-11 23:28:26 +0000)

# PROJ-1042: wire up new pricing rules (2014-09-20 17:30:39 +0000)

# Update dependencies (2014-09-23 19:15:06 +0000)
