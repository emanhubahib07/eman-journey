def calculate_average(math, english, science, tle, history):
    return (math + english + science + tle + history) / 5
result = calculate_average(95, 85, 90, 80, 87)
print(f"Your Average is {result}")

def check_result(average):
    if average >= 90:
        return "Excellent"
    elif average >= 75:
        return "Passed!"
    else:
        return "Failed!"
remarks = check_result(result)
print(remarks)