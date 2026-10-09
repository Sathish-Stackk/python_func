meetings = [
    (9, 10),
    (10, 11),
    (10, 12),
    (13, 14)
]

meetings.sort()

for i in range(len(meetings) - 1):
    current_end = meetings[i][1]
    next_start = meetings[i + 1][0]

    if current_end > next_start:
        print("Conflict:", meetings[i], "and", meetings[i + 1])
