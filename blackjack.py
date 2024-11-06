import art

import random



#####################################################_Global Variables_#################################################



##cards to play with.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



########################################################_Functions_#####################################################



##functions for mathematical operations
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2



##function to deal a card
def deal_card(number_of_cards):
    return random.sample(cards, number_of_cards)



##function to ask user to play & test input is valid, and ask again if not
def get_yes_no():
    while True:
        response = input("Would you like to play a game of Blackjack? 'yes' or 'no': ").strip().lower()
        if response in ["yes", "no"]:
            return response
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")



##function to calculate current total of all cards in list
def calculate_score(list):
    score = sum(list())
    if score == 21:
        return 0
    else:
        return score



##function to ask for hit or pass
def hit_or_pass():
    hit = input("Type 'y' to hit, type 'n' to pass.")
    if hit in ["y", "n"]:
        return hit
    else:
        hit = input("Type 'y' to hit, type 'n' to pass.")

####################################################_Code Start_########################################################


## call function and set initial variable
play_a_game = get_yes_no()


##Start game if user asks
while play_a_game == "yes":


    ##print logo
    print(art.logo)


    ##set/refresh internal variables
    player_hand = []
    npc_hand = []
    player_score = 0
    npc_score = 0
    winner = ""


    ##deal first hand
    player_hand.append(deal_card(2))
    npc_hand.append(deal_card(2))


    ##calculate current scores
    player_score = calculate_score(player_hand)
    npc_score = calculate_score(npc_hand)
    if player_score == 0 or npc_score == 0:
        if player_score == 0:
            print(f"Your final hand: {player_hand}, final score: {player_score}")
            print(f"Computer's final hand: {npc_hand}, final score: {npc_score}")
            print("You Win!")
        else:
            print(f"Your final hand: {player_hand}, final score: {player_score}")
            print(f"Computer's final hand: {npc_hand}, final score: {npc_score}")
            print("The computer wins.")
    elif player_score > 21 or npc_score > 21:
        if player_score > 21:
            print(f"Your final hand: {player_hand}, final score: {player_score}")
            print(f"Computer's final hand: {npc_hand}, final score: {npc_score}")
            print("The computer wins.")
        else:
            print(f"Your final hand: {player_hand}, final score: {player_score}")
            print(f"Computer's final hand: {npc_hand}, final score: {npc_score}")
            print("You Win!")
    else:
        print(f"Your Cards: {player_hand}, current score: {player_score}")
        print(f"Computer's 1st card: {npc_hand[0]}")


    ##print current hands, and the player score



    ##play on, or tally score, based on input
    if hit == 'y':
        # add additional cards to the player hands
        player_hand += deal_card(1)
        npc_hand += deal_card(1)
    else:
        print(f"Your final hand: {player_hand}, current score: {player_score}")
        print(f"Computer's final hand: {npc_hand}")
        print(f"")