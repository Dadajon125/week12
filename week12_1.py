data = """Lunch,12.50
Coffee,5.00
Office Supplies,23.75
Taxi,10.00
Coffee,8.25
Dinner,50.00"""

with open("expenses.txt", "w") as f:
    f.write(data)

sum_expenses = 0.0
num_transactions = 0


with open("expenses.txt" , "r") as f:
    for line in f:
        category, amount = line.strip(). split(",")
        sum_expenses += float(amount)
        num_transactions += 1
avg_expense = sum_expenses / num_transactions

print("--- expense report ---")
print(f"total transactions: {num_transactions}")
print(f"total spent: ${sum_expenses:.2f}")
print(f"average expense: ${avg_expense:.2f}")

     