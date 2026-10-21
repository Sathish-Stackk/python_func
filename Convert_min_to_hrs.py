def convert_time(minutes):
    hours = minutes // 60
    remaining = minutes % 60
    return hours, remaining

total = 145
hours, minutes = convert_time(total)

print("Hours:", hours)
print("Minutes:", minutes)
