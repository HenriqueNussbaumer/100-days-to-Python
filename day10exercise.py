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
    "/": divide
}

num1 = int(input("What is the first number?"))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation Symbol \n")
num2 = int(input("What is the second number?"))

calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")
aux = input("Do you wanna keep making operations? Type yes or no")

if aux == "yes":
    loop = True
else:
    loop = False

while loop is True:
    operation_symbol = input("Pick another operation Symbol \n")
    num3 = int(input("What is the following number?"))
    calculation_function = operations[operation_symbol]
    second_answer = calculation_function(first_answer, num3)
    print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
    first_answer = second_answer
    user_input = input("Do you wanna continue? Type yes or no")
    if user_input == "yes":
        pass
    else:
        loop = False