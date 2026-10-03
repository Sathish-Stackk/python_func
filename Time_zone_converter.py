from datetime import datetime, timedelta

time = datetime.now()
offset = int(input("Enter hour difference: "))

converted = time + timedelta(hours=offset)

print("Current Time:", time.strftime("%H:%M:%S"))
print("Converted Time:", converted.strftime("%H:%M:%S"))
