#import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    #print(art.logo)
    result = 0
    primary = float(input("What is the first number?: "))
    chosen_operation = input("Please choose an operation: '+', '-'. '*', '/':  ")
    secondary = float(input("What is the next number?: "))
    result += operations[chosen_operation](primary, secondary)
    print(f"Result: {result}")

    progression = input("Would you like to continue with the previous results?: ").lower()

    while progression == "yes":
        new_chosen_operation = input("Please choose an operation: '+', '-'. '*', '/':  ")
        new_secondary = float(input("What is the next number?: "))
        result = operations[new_chosen_operation](result, new_secondary)
        print(f"Result: {result}")
        progression = input("Would you like to continue with the previous results?: ").lower()
    else:
        print("\n" * 100)
        calculator()

calculator()