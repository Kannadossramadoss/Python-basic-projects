class Calculator:

    # function for addition of two numbers
    def addition(self, a, b):
        return a + b

    # function for subtraction of two numbers
    def subtraction(self, a, b):
        return a - b

    # function for multiplication of two numbers
    def multiplication(self, a, b):
        return a * b

        # function for division of two numbers

    def division(self, a, b):
        return a / b


# Creating object for Calculator class.
calc_obj = Calculator()

# Loop for all the operations
while True:

    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Exit")

    # Fetching the user input.
    user_input = int(input("Enter the number from 1 to 4 to action: "))
    if user_input == 5:
        print("Calculator script is finished")
        break

        # Check the user input is appropriate.
    if user_input in (1, 2, 3, 4, 5):

        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))

        if user_input == 1:
            print(f"{first_number} + {second_number} = {calc_obj.addition(first_number, second_number)}")
        elif user_input == 2:
            print(f"{first_number} - {second_number} = {calc_obj.subtraction(first_number, second_number)}")
        elif user_input == 3:
            print(f"{first_number} * {second_number} = {calc_obj.multiplication(first_number, second_number)}")
        elif user_input == 4:
            print(f"{first_number} / {second_number} = {calc_obj.division(first_number, second_number)}")
    else:
        print(f"You have entered an invalid number: {user_input}")

