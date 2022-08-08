#setup
import random
#import replit
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

#Calculate score
def sum_lst(cards_lst):
    #BlackJack
    if sum(cards_lst)==21 and len(cards_lst)==2:
        return 0
    elif 11 in cards_lst and sum(cards_lst)>21:
        cards_lst.remove(11)
        cards_lst.append(1)
        return sum(cards_lst)
    else:
        return sum(cards_lst)

#deal cards
def dealer(cards_lst):
    if len(cards_lst)<2:
        for i in range(2):
            cards_lst.append(random.choice(cards))
    else:
        cards_lst.append(random.choice(cards))
    return cards_lst

#compare results
def compare_lst(cards_lst1,cards_lst2):
    score1=sum_lst(cards_lst1)
    score2=sum_lst(cards_lst2)
    print(f"Your final hands: {cards_lst1}, final score: {score1}")
    print(f"Computer's final hands: {cards_lst2}, final score: {score2}")
    if score1==0:
        print("BlackJack")
    elif (score1>21 and score2>21) or score1==score2:
        print("Draw")
    elif score1>21 or (score1<score2 and score2<=21):
        print("Computer wins!")
    elif score2>21 or (score1>score2 and score1<=21):
        print("You win!")

#display cards
def display(cards_lst1,cards_lst2):
    score1 = sum_lst(cards_lst1)
    print(f"Your cards: {cards_lst1}, current score: {score1}.")
    print(f"Computer's first card: {cards_lst2[0]}.")

#body
should_continue_game=input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
while should_continue_game=='y':
    #clear()
    print(logo)
    human_card = []
    computer_card = []
    should_add_card = 'y'
    while should_add_card=='y':
        dealer(human_card)
        dealer(computer_card)
        display(human_card, computer_card)
        if sum_lst(human_card)>21 or sum_lst(human_card)==0 or sum_lst(computer_card)==0:
            compare_lst(human_card, computer_card)
            break
        else:
            should_add_card = input("Type 'y' to get another card, type 'n' to pass: ")

    if should_add_card=='n':
        while sum_lst(computer_card)!=0 and sum_lst(computer_card)<17:
            dealer(computer_card)
        display(human_card, computer_card)
        compare_lst(human_card, computer_card)
    should_continue_game=input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")