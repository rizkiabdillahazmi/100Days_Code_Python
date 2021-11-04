print("Welcome to Tip Calculator.")

total_bill = float(input("What was the total bill? $"))
percentage = int(input(
    "What percentage tip would you like to give? 10, 12, or 15? "))
split_bill = int(input("How many people to split the bill ? "))

pay = (total_bill/split_bill)*(1+percentage/100)
# pay = (total_bill*percentage/100+total_bill)/split_bill

print(f"Each person sholud pay: ${round(pay, 2)}")
