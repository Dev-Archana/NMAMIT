password = input("enter the password")
password = password.replace(" ", "")
print(f'current password is {password}')
special_char = '!@#$%^&*()-_=+[]{}|;:,.<>'
has_up = any(a.isupper() for a in password)
has_digit = any(a.isdigit() for a in password)
has_special = any(a in special_char for a in password)

if has_up and has_digit and has_special:
    print("Password is strong")
else:
    print("Password is weak")