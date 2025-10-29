# David Wylie
# CIS256 Fall 2025
# Programming Assignment 4.1 (PA 4)
# Calculator Program


def add(x, y):
    """
    Addition Function.
    :params: x, y, float - numbers to add together.
    :return: result of operation
    """
    return x + y


def subtract(x, y):
    """
    Subtraction Function.
    :params: x, y, float - numbers to subtract from each other.
    :return: result of operation
    """
    return x - y


def multiply(x, y):
    """
    Multiplication Function.
    :params: x, y, float - numbers to multiply together.
    :return: result of operation
    """
    return x * y


def divide(x, y):
    """
    Division Function.
    :params: x, y, float - numbers to divide from each other.
    :return: result of operation
    """
    return x / y


def main():
    while True:
        print("~Select a Calculator Operation~")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Enter choice(1-5): ")

        if choice in ('1', '2', '3', '4', '5'):
            # Choice 5 (exit) doesn't need number inputs
            if choice == '5':
                print("Goodbye!")
                break

            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print("-" * 40)
            except ValueError:
                print("Invalid input. Please enter a number.")
                print("-" * 40)
                continue

            match choice:
                case '1':
                    print(
                        f"Calculation: {num1} + {num2} = "
                        f"{add(num1, num2)}"
                        )
                case '2':
                    print(
                        f"Calculation: {num1} - {num2} = "
                        f"{subtract(num1, num2)}"
                        )
                case '3':
                    print(
                        f"Calculation: {num1} * {num2} = "
                        f"{multiply(num1, num2)}"
                          )
                case '4':
                    if num2 == 0:
                        print("ERROR: Cannot divide by zero.")
                    else:
                        print(
                            f"Calculation: {num1} / {num2} = "
                            f"{divide(num1, num2)}"
                              )
            print("-" * 40)
        else:
            print("Please enter a number from 1 through 5")
            print("-" * 40)


if __name__ == "__main__":
    main()
