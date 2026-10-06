contacts = {}

while True:
    name = input("Enter name (or exit): ")

    if name.lower() == "exit":
        break

    phone = input("Enter phone number: ")
    contacts[name] = phone

print("\n--- Contact Book ---")

for name, phone in contacts.items():
    print(name, ":", phone)
