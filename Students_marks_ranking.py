marks = [78, 92, 65, 88, 95, 71]

ranking = sorted(marks, reverse=True)

for rank, mark in enumerate(ranking, 1):
    print(rank, "->", mark)
