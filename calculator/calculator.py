from art import logo
import os

# Add numbers
def add(num1, num2):
    return num1 + num2

# subsctract number
def subtract(num1, num2):
    return num1 - num2

# multiply
def multiply(num1, num2):
    return num1 * num2

# divide
def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "=": subtract,
    "*": multiply,
    "/": divide
}

def calculation():
    print(logo)
    num1 = float(input("What 's the first number? "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operations_symbol = input("Pick an operation: ")    

        num2 = float(input("What 's the next number? "))
        answer = operations[operations_symbol](num1, num2)

        print(f"{num1} {operations_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with the {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            os.system('clear')
            calculation()
calculation()            