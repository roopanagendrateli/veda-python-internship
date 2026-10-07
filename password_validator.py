import string


def validate_password(password):
    errors = []

    # Check minimum length
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")

    # Check uppercase letter
    if not any(char.isupper() for char in password):
        errors.append("Password must contain at least one uppercase letter.")

    # Check lowercase letter
    if not any(char.islower() for char in password):
        errors.append("Password must contain at least one lowercase letter.")

    # Check digit
    if not any(char.isdigit() for char in password):
        errors.append("Password must contain at least one number.")

    # Check special character
    special_characters = string.punctuation

    if not any(char in special_characters for char in password):
        errors.append("Password must contain at least one special character.")

    # Display result
    if len(errors) == 0:
        print("\nPassword is valid!")
        return True
    else:
        print("\nPassword is invalid.")

        print("\nValidation messages:")
        for error in errors:
            print("-", error)

        return False


# Main program
print("=" * 45)
print("       PASSWORD VALIDATOR")
print("=" * 45)

password = input("Enter your password: ")

validate_password(password)

print("\nProgram completed successfully!")