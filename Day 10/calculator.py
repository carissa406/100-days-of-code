
import art


#calculator

#functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#dictionary of functions
operations = {"+":add,
             "-":subtract,
             "*":multiply,
             "/":divide}

def calculator():
    print(art.logo)
    keep_calculating = True
    num1 = float(input("What's the first number?: "))

    #for loop to go through dictionary and print each operations symbol
    for key in operations:
        print(key)

    operation_symbol = input("Pick an operation from the line above: ")

    num2 = float(input("What's the second number?: "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
    if choice == 'n':
        calculator()

    while keep_calculating == True:
        operation_symbol = input("Pick an operation: ")
        num3 = float(input("What's the next number?: "))
        num1 = answer
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num3)

        print(f"{num1} {operation_symbol} {num3} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
        if choice == 'n':
            calculator()
calculator()