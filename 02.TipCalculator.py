# BILL CALCULATOR

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage of tip would you like to give? 10,12 or 15? "))
tip_amount = bill*(tip/100)
new_bill = bill+tip_amount
split = int(input("How many people to split the bill? "))
each = round(new_bill/split, 2)
print(f"Each person should pay: ${each}")
