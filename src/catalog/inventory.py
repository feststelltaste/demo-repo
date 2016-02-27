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

# Improve performance (2014-10-01 06:32:42 +0000)

# Fix typo (2014-11-09 18:47:21 +0000)

# Fix bug in checkout flow (2015-04-07 02:58:51 +0000)

# Rename variables for clarity (2015-06-04 14:27:13 +0000)

# Rename variables for clarity (2015-06-22 18:58:16 +0000)

# Improve error handling (2016-01-04 01:53:34 +0000)

# Extract helper method (2016-02-04 00:46:00 +0000)

# Fix typo (2016-02-27 03:56:48 +0000)
