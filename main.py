# Case Study 42: Student Marks Matrix Analysis
marks = []

for student in range(3):
    row = []
    print(f"Enter marks for student {student + 1}:")
    for subject in range(3):
        score = float(input(f"  Subject {subject + 1}: "))
        if score < 0 or score > 100:
            print("Invalid mark. Enter marks from 0 to 100.")
            break
        row.append(score)
    if len(row) != 3:
        break
    marks.append(row)

if len(marks) == 3:
    totals = []
    print("\nSTUDENT RESULTS")
    for i in range(3):
        total = sum(marks[i])
        average = total / 3
        totals.append(total)
        print(f"Student {i + 1}: Total = {total:.2f}, Average = {average:.2f}")

    top_index = totals.index(max(totals))
    print(f"Highest total: Student {top_index + 1} ({max(totals):.2f})")
