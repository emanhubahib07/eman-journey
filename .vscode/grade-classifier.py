while True:
    grade = int(input("Enter your grade: "))

    if grade >= 90:
        print("Excellent")
    elif grade >= 75:
        print("Passed!")
    else:
        print("Failed!")

    again = input("Do you want to input again? y/n ")
    if again.lower() != 'y':
        break