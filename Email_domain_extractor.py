emails = [
    "sathish@gmail.com",
    "user@yahoo.com",
    "admin@outlook.com",
    "student@gmail.com"
]

domains = list(map(lambda email: email.split("@")[-1], emails))

print("Email Domains:", domains)
print("Unique Domains:", sorted(set(domains)))
print("Gmail Users:", sum("gmail.com" in email for email in emails))
