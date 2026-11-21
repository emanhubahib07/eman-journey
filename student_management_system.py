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





print("====== Student List ======")

display_student()
update_grade()
delete_student()
display_student()


