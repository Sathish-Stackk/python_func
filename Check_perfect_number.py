def is_perfect(n):
    total = sum(i for i in range(1, n) if n % i == 0)
    return total == n

n = int(input("Enter number: "))
print("Perfect Number" if is_perfect(n) else "Not Perfect")
