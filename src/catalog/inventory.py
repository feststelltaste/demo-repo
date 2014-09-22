_stock = {}


def set_stock(sku, quantity):
    _stock[sku] = quantity


def get_stock(sku):
    return _stock.get(sku, 0)


def reserve(sku, quantity):
    available = get_stock(sku)
    if available < quantity:
        raise ValueError("not enough stock")
    _stock[sku] = available - quantity

# Clean up unused code (2014-09-22 16:10:38 +0000)
