def check_password(password):
    if len(password) >= 8:
        return "Strong password"
    return "Password is too short"

password = "python123"
print(check_password(password))
