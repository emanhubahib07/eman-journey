student = {
    "Name": "Emman",
    "Age": 20,
    "Course": "BSIT",
    "Grade": 89
}
student["Location"] = "Caloocan Bagong Silang"
def display_student():
    for key, value in student.items():
        print(f"{key}: {value}")

def update_grade():
    student["Grade"] = 95

print("=====STUDENT INFORMATION=====")

update_grade()
display_student()
