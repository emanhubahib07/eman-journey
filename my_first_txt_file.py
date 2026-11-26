def add_student():
    with open("student.txt", "a") as file:
        file.write("====== New Record ======\n")
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Course: {course}\n")

def write_student():
    with open("student.txt", "w") as file:
        file.write("====== Student Information ======\n")
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Course: {course}\n")

def show_student():
    with open("student.txt","r") as file:
        context = file.read()
        print(context)

while True:
    print("[1] Write/Overwrite Information!")
    print("[2] Add Student!")
    print("[3] Show Student!")
    print("[4] Exit")
    select = (input("Choose number: "))

    if select == '1':
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        course = input("Enter your course: ")
        write_student()
    elif select == '2':
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        course = input("Enter your course: ")
        add_student()
    elif select == '3':
        show_student()
    elif select == '4':
        break
    again = input("Do you want to try again? y/n")
    if again.lower() != 'y':
        break
