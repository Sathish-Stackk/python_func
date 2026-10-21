def second_largest(numbers):
    unique = list(set(numbers))
    unique.sort()
    return unique[-2]

values = [12, 45, 23, 67, 34]
print("Second largest:", second_largest(values))
