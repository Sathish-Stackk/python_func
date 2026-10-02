names = ["Sathish", "Rahul", "Alexander", "Priya", "Kiran"]

result = sorted(names, key=len, reverse=True)

for position, name in enumerate(result, start=1):
    print(position, name, "-", len(name), "characters")

print("Longest:", max(names, key=len))
