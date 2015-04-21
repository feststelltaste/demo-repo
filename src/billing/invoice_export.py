import json


def export_invoice_as_json(invoice):
    return json.dumps(invoice, indent=2)


def export_invoice_as_csv_row(invoice):
    return f"{invoice['description']},{invoice['net_amount']},{invoice['total']}"

# Update dependencies (2014-09-28 07:49:45 +0000)

# Refactor service layer (2015-02-22 18:04:34 +0000)

# Clean up unused code (2015-03-23 05:25:21 +0000)

# Add logging (2015-04-21 20:11:09 +0000)
