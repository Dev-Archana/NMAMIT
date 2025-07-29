
class InvalidAgeError(Exception):
    pass

def get_user_age():
    try:
        age_input = input("Enter your age: ")
        age = int(age_input)

        if age <= 0:
            raise InvalidAgeError("Age must be greater than zero.")

        print(f"Age {age} accepted. Registration successful!")

    except ValueError:
        print("Error: Please enter a valid integer (e.g., 18).")
    except InvalidAgeError as e:
        print(f"Error: {e}")


get_user_age()
