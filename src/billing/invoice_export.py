import json


def export_invoice_as_json(invoice):
    return json.dumps(invoice, indent=2)


def export_invoice_as_csv_row(invoice):
    return f"{invoice['description']},{invoice['net_amount']},{invoice['total']}"
