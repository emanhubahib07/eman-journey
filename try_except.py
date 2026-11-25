while True:
    try:
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))
        print(num1 / num2)
        break
    except ValueError:
        print("Invalid Please try again!")

    except ZeroDivisionError:
        print("Can't divide to zero")

    finally:
        print("Thank you for using my program!")
