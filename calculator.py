while True:
    num1 = float(input("Enter your 1st number: "))
    num2 = float(input("Enter your 2nd number: "))
    op = input("Enter your Operator: ")

    if op == "+":
        result = num1 + num2 
        print(result)
    elif op == "-":
        result = num1 - num2 
        print(result)
    elif op == "*":
        result = num1 * num2
        print(result)
    elif op == "/":
        result = num1 / num2
        if num2 == 0:
            print("Can't divide to zero")
            continue
        print(result)
    else:
        print(f"{op} is not an operator")
        continue
    again = input("Do you want to try again? Y/N")
    if again.lower() != 'y':
        break
