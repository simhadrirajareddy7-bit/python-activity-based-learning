# Case Study 17: Student Performance Trend Analysis
marks = []

for i in range(3):
    score = float(input(f"Enter exam {i + 1} marks (0-100): "))
    if score < 0 or score > 100:
        print("Invalid marks. Enter values from 0 to 100.")
        break
    marks.append(score)

if len(marks) == 3:
    change = marks[2] - marks[0]
    print(f"Highest mark: {max(marks):.2f}")
    if change > 0:
        print(f"Improvement: {change:.2f} marks")
    elif change < 0:
        print(f"Decline: {abs(change):.2f} marks")
    else:
        print("No change between the first and third exams.")
