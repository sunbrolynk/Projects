print("Welcome to Is it Odd or Even!")
favorite_number = int(input("What is your favorite number?\n"))
#converted_number = int(favorite_number)
odd_even = favorite_number % 2

if odd_even == 0:
    print("Its even!")
else:
    print("It's Odd!")