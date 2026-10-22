def is_armstrong(num):
    digits = str(num)
    total = sum(int(d) ** len(digits) for d in digits)
    return total == num

n = int(input("Enter number: "))
print("Armstrong Number" if is_armstrong(n) else "Not Armstrong")
