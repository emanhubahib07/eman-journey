def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

while True:
    num1 = float(input("Enter your 1st number: "))
    num2 = float(input("Enter your 2nd number: "))
    op = input("Enter your operator + - * /: ")

    if op == "+":
        result = add(num1, num2)
        print(result)
    elif op == "-":
        result = subtract(num1, num2)
        print(result)
    elif op == "*":
        result = multiply(num1, num2)
        print(result)
    elif op == "/":
        if num2 == 0:
            print("Can't Divide to Zero")
            continue
        result = division(num1, num2)
        print(result)
    else:
        print(f"{op} is not an operator!")
        break

    while True:
        again = input("do you want to try again? y/n").lower()
        if again == "y":
            break
        elif again == "n":
            print("Thank you for using my calculator!")
            exit()
        else:
            print("Invalid Please choose y/n!")
            
            

        

