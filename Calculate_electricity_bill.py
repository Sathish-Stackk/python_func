def electricity_bill(units):
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = units * 3
    else:
        bill = units * 5
    return bill

units = 180
print("Electricity Bill:", electricity_bill(units))
