print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "L":
    bill += 25
elif size == "M":
    bill += 20
elif size == "S":
    bill += 15
if pepperoni == "Y":
    if size == "L":
        bill += 3
    if size == "M":
        bill += 3
    if size == "S":
        bill += 1
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")