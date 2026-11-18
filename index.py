students = ["Emman", "John", "Carmen"]
grades = [90, 85, 95]

print("===== STUDENT GRADE SYSTEM =====")

for i in range(len(students)):
    print(f"Student: {students[i]}")
    print(f"Grade: {grades[i]}")
    
    if grades[i] >= 90:
        print("Remarks: Excellent")
    elif grades[i] >= 75:
        print("Remarks: Passed")
    else:
        print("Failed")
    

print("===== SUMMARY =====")
print(f"Total of students: {len(students)}")


    
    
