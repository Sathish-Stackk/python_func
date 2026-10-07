def second_largest(numbers):
    unique = list(set(numbers))
    unique.sort()
    return unique[-2]

numbers = list(map(int, input("Enter numbers: ").split()))

if len(set(numbers)) >= 2:
    print("Second Largest:", second_largest(numbers))
else:
    print("Need at least two different numbers.")
