password = "Python@2026"

rules = [
    len(password) >= 8,
    any(ch.isupper() for ch in password),
    any(ch.isdigit() for ch in password),
    any(ch in "@#$%" for ch in password)
]

print("All Rules Passed:", all(rules))
print("Rules Passed:", sum(rules), "/", len(rules))
