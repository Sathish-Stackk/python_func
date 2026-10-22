def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

year = int(input("Enter year: "))
print("Leap Year" if is_leap_year(year) else "Not a Leap Year")
