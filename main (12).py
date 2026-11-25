# Case Study 15: Smart Parking Fee Management
vehicle = input("Enter vehicle type (car/bike): ").strip().lower()
hours = float(input("Enter parking duration in hours: "))

if hours <= 0:
    print("Invalid parking duration.")
elif vehicle == "car":
    rate = 30
    print(f"Parking fee: Rs. {rate * hours:.2f}")
elif vehicle == "bike":
    rate = 15
    print(f"Parking fee: Rs. {rate * hours:.2f}")
else:
    print("Invalid vehicle type. Enter car or bike.")
