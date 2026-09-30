scores = {
    "Sathish": 86,
    "Rahul": 92,
    "Priya": 78,
    "Anil": 95,
    "Divya": 88
}

ranking = sorted(scores.items(), key=lambda item: item[1], reverse=True)

for rank, (name, score) in enumerate(ranking, start=1):
    print(f"Rank {rank}: {name} - {score}")

print("Highest Score:", max(scores.values()))
print("Average Score:", round(sum(scores.values()) / len(scores), 2))
