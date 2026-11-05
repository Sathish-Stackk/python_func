def merge_intervals(intervals):
    intervals.sort()
    result = []
    for start, end in intervals:
        if result and start <= result[-1][1]:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])
    return result

print(merge_intervals([[1, 3], [2, 6], [8, 10]]))
