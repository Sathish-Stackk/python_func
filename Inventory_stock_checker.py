stock = {"Laptop": 5, "Mouse": 0, "Keyboard": 8, "Monitor": 2}

available = dict(filter(lambda item: item[1] > 0, stock.items()))
empty = list(filter(lambda item: item[1] == 0, stock.items()))

print("Available Products:", available)
print("Out of Stock:", list(map(lambda item: item[0], empty)))
print("Total Units:", sum(stock.values()))
print("Lowest Stock:", min(stock, key=stock.get))
