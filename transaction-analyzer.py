data = [
  (749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")
]

def print_transactions(transactions):
  for act in transactions:
    amount, statement = act
    print(f"${amount} - {statement}")

def print_summary(transactions):
  deposits = [act[0] for act in transactions if act[0]>=0]
  total_deposited = sum(deposits)
  print(total_deposited)

  withdrawals = [act[0] for act in transactions if act[0]<0]
  total_withdrawn = sum(withdrawals)
  print(total_withdrawn)

  balance = float(total_deposited)+float(total_withdrawn)
  print(f"{balance:.2f}")
  

def analyze_transactions(transactions):
  transactions.sort()
  largest_withdrawal = transactions[0]
  largest_deposit = transactions[-1]
  print(largest_withdrawal, largest_deposit)

  deposits = [act[0] for act in transactions if act[0]>=0]
  total_deposit = sum(deposits)
  average_deposit = total_deposit / len(deposits) if deposits else 0
  print(f"Average deposit: {average_deposit:.2f}")

  withdrawals = [act[0] for act in transactions if act[0]<0]
  total_withdrawals = sum(withdrawals)
  average_withdrawal = total_withdrawals / len(withdrawals) if withdrawals else 0
  print(f"Average withdrawal: {average_withdrawal:.2f}")

while True:
  choice = input("Would you like to print, analyze or stop?")
  if choice == "print":
    print_summary(data)
  elif choice == "analyze":
    analyze_transactions(data)
  elif choice == "stop":
    print("You have cancelled your session.")
    break
  else:
    print("Invalid choice")
