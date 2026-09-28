cities = ["Delhi", "Chennai", "Hyderabad", "Mumbai"]
temperatures = [38, 34, 36, 32]

data = zip(cities, temperatures)

for city, temp in data:
    print(city, ":", temp, "°C")

print("Highest:", max(temperatures))
print("Lowest:", min(temperatures))
