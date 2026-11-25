# Case Study 19: Multi-Product Shopping Budget Constraint
budget = float(input("Enter your shopping budget: "))
total = 0
items = []

for i in range(3):
    name = input(f"Enter product {i + 1} name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    if price <= 0 or quantity <= 0:
        print("Invalid price or quantity. Item not added.")
    else:
        cost = price * quantity
        items.append((name, cost))
        total += cost

print("\nSHOPPING BILL")
for name, cost in items:
    print(f"{name}: Rs. {cost:.2f}")
print(f"Total: Rs. {total:.2f}")

if total <= budget:
    print(f"Within budget. Remaining: Rs. {budget - total:.2f}")
else:
    print(f"Over budget by: Rs. {total - budget:.2f}")
