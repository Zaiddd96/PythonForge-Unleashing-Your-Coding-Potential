import math
from replit import clear
from artt import calcultor_logo

def add(num1, num2):
    """Add two numbers"""
    return num1 + num2

def subtract(num1, num2):
    """Subtract two numbers"""
    return num1 - num2

def multiply(num1, num2):
    """Multiply two numbers"""
    return num1 * num2

def divide(num1, num2):
    """Divide two numbers"""
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Cannot divide by zero"

def square_root(num):
    "Find Squareroot of number"
    return math.sqrt(num)

def factorial(num):
    """Find Factorial of a number """
    if num < 0:
        return "Error: Factorial is not defined for negative numbers"
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "sqrt": square_root,
    "!": factorial
}

def calculator():
    print(calcultor_logo)
    num1 = float(input("Enter the first number: "))
    for operator in operations:
        print(operator)
    should_continue = True
    while should_continue:
        symbol = input("Enter the operation: ")
        if symbol not in operations:
            print("Invalid operation. Please choose from +, -, *, /, sqrt, or !.")
            continue
        if symbol == "sqrt":
            num1 = square_root(num1)
            print(f"Square root of {num1:.2f} = {num1:.2f}")
        elif symbol == "!":
            result = factorial(int(num1))
            print(f"{int(num1)}! = {result}")
        else:
            num2 = float(input("Enter the next number: "))
            function = operations[symbol]
            result = function(num1, num2)
            print(f"{num1} {symbol} {num2} = {result}")
            if input("Type 'y' to continue or 'n' to start a new calculation: ").lower() == "y":
                num1 = result
            else:
                clear()
                calculator()

calculator()
