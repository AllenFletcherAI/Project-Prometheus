# Goal: Write a program that takes user input (name, age, favourite number) and displays a formatted message.

# Key Concepts: Variables, input(), data types, type conversion, f-strings.

def get_user_input():
    """Gets user input for name, age, and favourite number."""
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    favourite_number = int(input("Enter your favourite number: "))
    return name, age, favourite_number

def display_message(name, age, favourite_number):
    """Displays a formatted message with the user's input."""
    print(f"Hello, {name}! You are {age} years old and your favourite number is {favourite_number}")


def main():
    """Main function to orchestrate getting the input and displaying the output."""
    name, age, favourite_number = get_user_input()
    display_message(name, age, favourite_number)

if __name__ == "__main__":
    main()