student = [
{
    "Name": "Emman",
    "Age": 20,
    "Course": "BSIT",
    "Grade": 85
},
{
    "Name": "Rodelons",
    "Age": 20,
    "Course": "BSIT",
    "Grade": 78
},
{
    "Name": "Angello",
    "Age": 21,
    "Course": "BSIT",
    "Grade": 89

},
{
    "Name": "Lian",
    "Age": 22,
    "Course": "BSIT",
    "Grade": 83
},
{
    "Name": "Jayferson",
    "Age": 21,
    "Course": "BSIT",
    "Grade": 82
}
]
def display_student():
    for students_info in student:
        print(f"Name: {students_info['Name']}")
        print(f"Age: {students_info['Age']}")
        print(f"Course: {students_info['Course']}")
        print(f"Grade: {students_info['Grade']}\n")

def add_student():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    course = input("Enter your course: ")
    grade = int(input("Enter your grade: "))

    student.append({
        "Name": name,
        "Age": age,
        "Course": course,
        "Grade": grade
    })
def search_student():
    search_name = input("Enter student name: ")
    found = False

    for student_info in student:
        if search_name.lower() == student_info["Name"].lower():
            print(f"Student Found!: {student_info}")
            found = True
            break
    if not found:
        print("Student Not found!")

def update_grade():
    search_name = input("Enter Student name: ")
    found = False

    for student_info in student:
        if search_name.lower() == student_info["Name"].lower():
            new_grade = int(input("Enter new grade: "))
            student_info["Grade"] = new_grade
            found = True
            print("Student Grade succesfully updated!")
            break
    if not found:
        print("Not found!\n")

def delete_student():
    search_name = input("Enter Student name: ")
    found = False

    for student_info in student:
        if search_name.lower() == student_info["Name"].lower():
            student.remove(student_info)
            found = True
            break
    if not found:
            print("Student Not Found")

def count_student():
        print(f"Total of student!:{len(student)}")

def average_grade():
    total_grade = 0
    for students in student:
        total_grade += students["Grade"]
    average = total_grade / len(student)
    if len(student) == 0:
        print("No student Available")
    print(f"Average of Grades: {average}")
        

while True:
    print("==== Student Management System! ====")
    print("[1] Display Student")
    print("[2] Add Student")
    print("[3] Search Student")
    print("[4] Update Grade")
    print("[5] Remove Student")
    print("[6] Count Student")
    print("[7] Student Average")
    print("[8] EXIT!")
    choose = input("Choose number!")
    
    if choose == "1":
        display_student()
    elif choose == "2":
        add_student()
    elif choose == "3":
        search_student()
    elif choose == "4":
        update_grade()
    elif choose == "5":
        delete_student()
    elif choose == "6":
        count_student()
    elif choose == "7":
        average_grade()
    elif choose == "8":
        print("Thank you for using my SMS!")
        break
    else:
        print("Invalid choice!")




