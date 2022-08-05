#Add
def add(n1,n2):
    return n1+n2

#Substract
def substract(n1,n2):
    return n1-n2

#Multiply
def multtply(n1,n2):
    return n1*n2

#Divide
def divide(n1,n2):
    return n1/n2

#Add calculate dictionary
operations = {"+":add,
            "-":substract,
            "*":multtply,
            "/":divide}

def calculator():
    answer = float(input("What is the first number?: "))
    for index in operations:
        print(index)

    should_continue = 'y'
    while should_continue == 'y':
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))

        num1=answer
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'e' to exit, or type 'n' to start over.: ")
        if should_continue=='e':
            print('Goodbye')
        elif should_continue=='n':
            calculator()

calculator()