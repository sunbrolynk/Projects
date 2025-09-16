print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
tip_percentage = tip / 100
tip_multiplier = tip_percentage + 1
people = int(input("How many people to split the bill? "))
print("Each person should pay: $" + str(round(int(bill / people) * tip_multiplier, 2)))
