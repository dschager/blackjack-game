# Daniel Schager
# Black Jack Card Game
# 4/18/2022


import math
import random

deck_dict = {
    '2': [2,8],
    '3': [3,8],
    '4': [4,8],
    '5': [5,8],
    '6': [6,8],
    '7': [7,8],
    '8': [8,8],
    '9': [9,8],
    '10': [10,8],
    'J': [10,8],
    'Q': [10,8],
    'K': [10,8],
    'A': [11,8,1]
    }

deck_identifier = ['2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    'J',
    'Q',
    'K',
    'A']
                   
def random_cards(x):
    global deck_identifier
    global deck_dict
    decklist = []
    while len(decklist) < x:
        number = random.randint(0,12)
        randomcard = deck_identifier[number]
        if deck_dict[randomcard][1] > 0:
            decklist.append(randomcard)
            deck_dict[randomcard][1] = deck_dict[randomcard][1]-1
        elif deck_dict[randomcard][1] == 0:
            decklist = decklist
    return decklist,deck_dict

def print_card(card1,card2):
    x = "            "
    b = "          "
    c = " "
    d = "         "
    if card2 == 0:
        card2 = " "
    if card1 == "10":
        print(" ______________",c,"  ______________\n|",
              x,"|",c,"|",x,"|\n|",
              card1,d,"|",c,"|",card2,b,"|\n|",
              x,"|",c,"|",x,"|\n|",
              x,"|",c,"|",x,"|\n|",
              x,"|",c,"|",x,"|\n|",
              x,"|",c,"|",x,"|\n|",
              x,"|",c,"|",x,"|\n|",
              d,card1,"|",c,"|",b,card2,"|\n|",
              x,"|",c,"|",x,"|\n'--------------'",c,"'--------------'")
        
    elif card2 == "10":
        print(" ______________",c,"  ______________\n|",
              x,"|",c,"|",x,"|\n|",
              card1,b,"|",c,"|",card2,d,"|\n|",
              x,"|",c,"|",x,"|\n|",
              x,"|",c,"|",x,"|\n|",
              x,"|",c,"|",x,"|\n|",
              x,"|",c,"|",x,"|\n|",
              x,"|",c,"|",x,"|\n|",
              b,card1,"|",c,"|",d,card2,"|\n|",
              x,"|",c,"|",x,"|\n'--------------'",c,"'--------------'")
        
    elif card2 == 0:
        print(" ______________",c,"  ______________\n|",
              x,"|",c,"|",x,"|\n|",
              card1,b,"|",c,"|",x,"|\n|",
              x,"|",c,"|",x,"|\n|",
              x,"|",c,"|",x,"|\n|",
              x,"|",c,"|",x,"|\n|",
              x,"|",c,"|",x,"|\n|",
              x,"|",c,"|",x,"|\n|",
              b,card1,"|",c,"|",x,"|\n|",
              x,"|",c,"|",x,"|\n'--------------'",c,"'--------------'")
        
    else:
        print(" ______________",c,"  ______________\n|",
              x,"|",c,"|",x,"|\n|",
              card1,b,"|",c,"|",card2,b,"|\n|",
              x,"|",c,"|",x,"|\n|",
              x,"|",c,"|",x,"|\n|",
              x,"|",c,"|",x,"|\n|",
              x,"|",c,"|",x,"|\n|",
              x,"|",c,"|",x,"|\n|",
              b,card1,"|",c,"|",b,card2,"|\n|",
              x,"|",c,"|",x,"|\n'--------------'",c,"'--------------'")

def print_one_card(card):
    x = "            "
    b = "          "
    c = " "
    d = "         "
    if card == "10":
        print(" ______________\n|",
              x,"|\n|",
              card,d,"|\n|",
              x,"|\n|",
              x,"|\n|",
              x,"|\n|",
              x,"|\n|",
              x,"|\n|",
              d,card,"|\n|",
              x,"|\n'--------------'")
        
    else:
        print(" ______________\n|",
              x,"|\n|",
              card,b,"|\n|",
              x,"|\n|",
              x,"|\n|",
              x,"|\n|",
              x,"|\n|",
              x,"|\n|",
              b,card,"|\n|",
              x,"|\n'--------------'")

def check_ace(your_card1, your_card2, dealer_card1, dealer_card2):
    if your_card1

def situational(decklist,bet_size,balance):
    global deck_dict
    your_card1 = decklist[0]
    your_card2 = decklist[2]
    dealer_card1 = decklist[1]
    dealer_card2 = decklist[3]
    your_total = deck_dict[your_card1][0] + deck_dict[your_card2][0]
    your_ace_total = (deck_dict[your_card1][0] + deck_dict[your_card2][0]) - 10
    dealer_total = deck_dict[dealer_card1][0] + deck_dict[dealer_card2][0]
    if your_total == 21:
        print("Black Jack!")
        balance += bet_size
        return balance
    while your_total <= 21:
        if (your_card1 == 'A') or (your_card2 == 'A'):
            print("\nYou have", your_total, "or", your_ace_total)
        else:
            print("\nYou have", your_total)
        if int(bet_size)*2 <= balance and your_total <= 15:
            decision = input("\nHit(H), Stand(S), or Double(D)?\n")
            if decision == "D":
                bet_size += bet_size
                new_your_card,deck_dict = random_cards(1)
                print_one_card(new_your_card[0])
                your_total = deck_dict[new_your_card[0]][0] + your_total
                new_your_total = your_total
                your_total = 30
                
        else:
            decision = input("\nHit(H) or Stand(S)?\n")
        if decision == "H":
            new_your_card,deck_dict = random_cards(1)
            print_one_card(new_your_card[0])
            your_total = deck_dict[new_your_card[0]][0] + your_total
            new_your_total = your_total
        elif decision == "S":
            new_your_total = your_total
            your_total = 30
    if new_your_total > 21:
        print("You Lose")
        balance = balance - bet_size
        return balance
    print("\nDealer's Hand")
    print_card(dealer_card1,dealer_card2)
    if dealer_total > new_your_total and dealer_total <= 21:
        print("You lose")
        balance = balance - bet_size
        return balance
    elif dealer_total < new_your_total:
        while dealer_total < new_your_total:
            new_your_card,deck_dict = random_cards(1)
            print("\nDealer Hits\n")
            print_one_card(new_your_card[0])
            dealer_total = deck_dict[new_your_card[0]][0] + dealer_total
        if dealer_total > new_your_total and dealer_total <= 21:
            print("You lose")
            balance = balance - bet_size
        elif dealer_total > 21:
            print("You win")
            balance += bet_size
        elif dealer_total == new_your_total:
            print("Push")
            
    return balance
        

def integer_check(string):
    try:
        string = int(string)
        return string
    except:
        string = "Q"
        return string

    

print("Hello welcome to the Python Black Jack table")
starting_up = input("Enter 'i' for imformation regarding odds and format of the code, else press ENTER to continue\n")
if starting_up == "i":
    print("This game is played with 2 decks of cards, which allows the program to imitate a casino's playstyle. The potential cards in the deck chosen are at random. The first card is dealt to the player, the second to the dealer, and so on. The blank card presented by the dealer contains the value of the fourth randomly chosen card from the deck. Once a card is played, one of the 8 cards in the deck (dictionary) is removed.\n")
    
balance = input("Enter your starting buy-in amount: ")
while balance != "Q":
    balance = integer_check(balance)
    if balance == "Q":
        print("Incorrect format")
        balance = input("Enter your starting buy-in amount: ")
    else:
        print("You have","$"+str(balance))
        deck_total = 0     
        for i in deck_identifier:
            deck_total += deck_dict[i][1]
        if deck_total < 10:
            print("\nShuffling Deck\n")
            for i in deck_identifier:
                deck_dict[i][1] = 8
        balance = integer_check(balance)
        #hands = input("Enter the number of hands you'd like to play")
        bet_size = input("Place bet size: ")
        bet_size = integer_check(bet_size)
        if bet_size == "Q":
            print("Incorrect format")
        elif bet_size <= balance:
            pointless = input("\nPress ENTER to deal the cards\n")
            decklist,deck_dict = random_cards(4)
            print_card(decklist[1],0)
            print("Dealers Hand\n")
            print_card(decklist[0],decklist[2])
            print("Your Hand\n")
            balance = situational(decklist,bet_size,balance)
            if balance == 0:
                asking_balance = input("Would you like to add money? (Y) or (N): ")
                if asking_balance == "Y" or asking_balance == "y":
                    balance = input("Enter amount: ")
                elif asking_balance == "N" or asking_balance == "n":
                    print("Goodbye")
                    break


# Areas for improvement:
                # Allow player to split
                # Make Aces work as either 1 or 11
                # Double Ace
