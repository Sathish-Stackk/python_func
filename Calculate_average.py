def average(numbers):
    return sum(numbers) / len(numbers)

nums = list(map(int, input("Enter numbers: ").split()))
print("Average:", average(nums))
