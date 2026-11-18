while True:
    math = float(input("Enter Your Math Grade: "))
    english = float(input("Enter Your English Grade: "))
    science = float(input("Enter Your Science Grade: "))

    print("===== Grade Summary =====")
    total = math + english + science 
    print(f"Total: {total}")
    average = total / 3
    print(f"Average: {average:.2f}")
    passed = average >= 75 
    print(f"Passed: {passed}")
    excelent = average >= 90
    print(f"Excelent: {excelent}")
     
    again = input("Do you want to input grade again? y/n")
    if again.lower() != 'y':
       break

