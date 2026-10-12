sessions = {
    "Python": 45,
    "JavaScript": 30,
    "React": 50,
    "SQL": 25
}

total = sum(sessions.values())
best = max(sessions, key=sessions.get)

print("Study Report")
print("-" * 20)

for subject, minutes in sessions.items():
    print(f"{subject}: {minutes} min")

print(f"\nTotal Study Time: {total} min")
print(f"Most Studied: {best}")
