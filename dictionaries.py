#dictionary
student = {
    "Name": "Emman",
    "Age": 20,
    "Course": "BSIT",
    "Grade": 92
}

student["Grade"] = 95
student["Address"] = "Caloocan Bagong Silang"

print("=======Student Details=======")

for key, value in student.items():
    print(f"{key}: {value}")