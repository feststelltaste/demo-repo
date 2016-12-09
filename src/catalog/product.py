class Product:
    def __init__(self, sku, name, price):
        self.sku = sku
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product({self.sku!r}, {self.name!r}, {self.price})"

# Add unit tests (2014-03-09 19:57:40 +0000)

# Update documentation (2014-04-01 17:42:34 +0000)

# Add logging (2014-11-28 15:07:01 +0000)

# Update dependencies (2015-06-10 05:37:52 +0000)

# Extract helper method (2015-08-27 13:47:25 +0000)

# Fix bug in checkout flow (2015-10-12 03:54:39 +0000)

# Improve performance (2015-12-27 01:01:40 +0000)

# Refactor service layer (2016-09-20 06:33:28 +0000)

# Fix flaky test (2016-11-03 21:33:43 +0000)

# Fix typo (2016-11-08 10:45:26 +0000)

# Add unit tests (2016-12-09 16:45:17 +0000)
