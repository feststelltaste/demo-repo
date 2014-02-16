def build_daily_report(orders):
    total = sum(o.get("amount", 0) for o in orders)
    return {"order_count": len(orders), "total_amount": total}
