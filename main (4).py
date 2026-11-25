# Case Study 12: Attendance Recovery Computation
total = int(input("Enter total classes conducted: "))
attended = int(input("Enter classes attended: "))
target = float(input("Enter target attendance percentage: "))

if total <= 0 or attended < 0 or attended > total or not 0 < target <= 100:
    print("Invalid input. Please check the values.")
else:
    current = attended / total * 100
    required = 0

    while (attended + required) / (total + required) * 100 < target:
        required += 1

    print(f"Current attendance: {current:.2f}%")
    print(f"Minimum additional classes to attend: {required}")
    print(f"Attendance after attending them: "
          f"{(attended + required) / (total + required) * 100:.2f}%")
