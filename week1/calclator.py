# calculator program

while True:
    op = input("Enter Operator: (+,-,*,/) quit for exit ")
    if op == "quit":
        print("Thankyou for using calculator: ")
        break

    num1 = float(input("Enter Number 1: "))
    num2 = float(input("Enter Number 2: "))

    match op:
        case "+":
            print(f"Sum of Numbers: {num1 + num2} ")
        case "-":
            print(f"Subtraction  of Numbers: {num1 - num2} ")
        case "*":
            print(f"Product of Numbers: {num1 * num2} ")
        case "/":
            print(f"Division of Numbers: {num1 / num2} ")
        case _:
            print("Unrecognized Operation: ")