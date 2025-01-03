while True:

    def validate_password(password):
        special_char = "!@#$%^&*()_-+="
        if len(password) < 8:
            return False, "Password must be at least 8 characters long."
        elif any(char.isupper() for char in password) and any(char.islower() for char in password) and any(
                char.isdigit() for char in password) and any(char in special_char for char in password):
            return True, "Password verify"
        return False, "Enter correct password"


    # driver code
    password = str(input("Enter the password: "))
    is_valid, message = validate_password(password)
    print(message)

