products = [
    ("Laptop", 5), ("Mouse", 0),
    ("Keyboard", 8), ("Monitor", 0),
    ("Headphones", 3)
]

stock = dict(products)
available = dict(filter(lambda item: item[1] > 0, stock.items()))
unavailable = list(filter(lambda item: item[1] == 0, stock.items()))

print("Available Products:", available)
print("Out of Stock:", list(dict(unavailable).keys()))
print("Total Stock:", sum(stock.values()))
