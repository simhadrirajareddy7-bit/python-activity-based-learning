# Case Study 29: Password Policy Validation Engine
password = input("Enter a sample password to validate: ")

has_upper = any(ch.isupper() for ch in password)
has_lower = any(ch.islower() for ch in password)
has_digit = any(ch.isdigit() for ch in password)
has_special = any(not ch.isalnum() for ch in password)

errors = []
if len(password) < 8:
    errors.append("At least 8 characters are required.")
if not has_upper:
    errors.append("At least one uppercase letter is required.")
if not has_lower:
    errors.append("At least one lowercase letter is required.")
if not has_digit:
    errors.append("At least one digit is required.")
if not has_special:
    errors.append("At least one special character is required.")

if not errors:
    print("All sample password rules are satisfied.")
else:
    print("Password rules not satisfied:")
    for error in errors:
        print("-", error)
