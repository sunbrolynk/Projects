import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]


player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))
computer_choice = random.choice(choices)


print(player_choice)

if player_choice == 0:
    print(rock)
    if computer_choice == rock:
        print(rock)
        print("It's a tie!")
    if computer_choice == paper:
        print(paper)
        print("Paper covers rock, you lose.")
    if computer_choice == scissors:
        print(scissors)
        print("Rock smashes scissors, you win!")
elif player_choice == 1:
    print(paper)
    if computer_choice == rock:
        print(rock)
        print("Paper covers rock, you win!")
    if computer_choice == paper:
        print(paper)
        print("It's a tie!")
    if computer_choice == scissors:
        print(scissors)
        print("Rock smashes scissors, you win!")
elif player_choice == 2:
    print(scissors)
    if computer_choice == rock:
        print(rock)
        print("Rock smashes scissors, you lose.")
    if computer_choice == paper:
        print(paper)
        print("Scissors cut paper, you win!")
    if computer_choice == scissors:
        print(scissors)
        print("It's a tie!")