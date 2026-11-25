# Case Study 13: ATM Transaction Sequence Simulation
balance = float(input("Enter opening balance: "))
n = int(input("Enter number of transactions: "))
accepted = 0

if balance < 0 or n < 0:
    print("Invalid opening balance or transaction count.")
else:
    for i in range(n):
        kind = input(f"Transaction {i + 1} (D for deposit, W for withdrawal): ").upper()
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Rejected: amount must be positive.")
        elif kind == "D":
            balance += amount
            accepted += 1
            print("Deposit successful.")
        elif kind == "W" and amount <= balance:
            balance -= amount
            accepted += 1
            print("Withdrawal successful.")
        elif kind == "W":
            print("Rejected: insufficient balance.")
        else:
            print("Rejected: invalid transaction type.")

    print(f"Final balance: Rs. {balance:.2f}")
    print(f"Accepted transactions: {accepted}")
