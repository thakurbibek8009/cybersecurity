import re

def check_password_strength(password):
    strength = 0
    remarks = []

    # Length check
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters long")

    # Uppercase
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add at least one uppercase letter")

    # Lowercase
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Add at least one lowercase letter")

    # Numbers
    if re.search(r"\d", password):
        strength += 1
    else:
        remarks.append("Add at least one number")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks.append("Add at least one special character")

    # Strength rating
    if strength <= 2:
        return "Weak", remarks
    elif strength <= 4:
        return "Medium", remarks
    else:
        return "Strong", remarks


def suggest_password(password):
    suggestion = password

    if not re.search(r"[A-Z]", suggestion):
        suggestion += "A"
    if not re.search(r"[a-z]", suggestion):
        suggestion += "a"
    if not re.search(r"\d", suggestion):
        suggestion += "1"
    if not re.search(r"[!@#$%^&*]", suggestion):
        suggestion += "@"

    while len(suggestion) < 12:
        suggestion += "X"

    return suggestion


def main():
    print("🔐 Password Strength Analyzer\n")

    password = input("Enter your password: ")

    strength, remarks = check_password_strength(password)

    print(f"\nStrength: {strength}")

    if remarks:
        print("\nSuggestions to improve:")
        for r in remarks:
            print(f"- {r}")

        print("\nSuggested Strong Password:")
        print(suggest_password(password))
    else:
        print("Your password is strong! 💪")


if __name__ == "__main__":
    main()