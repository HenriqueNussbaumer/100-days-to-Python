# BlackJack

import random


def deal():
    return random.choice(cards)


def ask():
    aux = input("Do you want to draw more cards? Type yes or \n")
    if aux == "yes":
        return True
    else:
        return False


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_hand = [deal(), deal()]
dealers_hand = [deal(), deal()]

play = True

while play:
    while sum(dealers_hand) < 17:
        dealers_hand.append(deal())
        if sum(dealers_hand) > 21 and 11 in dealers_hand:
            dealers_hand[dealers_hand.index(11)] = 1
    print(user_hand)
    print(dealers_hand[0])
    while ask():
        user_hand.append(deal())
        print(user_hand)
        if sum(user_hand) > 21 and 11 in user_hand:
            user_hand[user_hand.index(11)] = 1
        if sum(user_hand) > 21:
            break
    if sum(dealers_hand) > 21:
        print("You win!")
    elif sum(user_hand) > 21:
        print("You lose!")
    elif sum(user_hand) == sum(dealers_hand):
        print("It'sa draw!")
    elif sum(user_hand) > sum(dealers_hand):
        print("You win")
    else:
        print("You lose!")
    print(user_hand)
    print(dealers_hand)
    aux = input("Do you wanna keep playing? type yes or no\n")
    if aux == "no":
        play = False
        print("It's been a pleasure taking your money!")
        continue
    user_hand = [deal(), deal()]
    dealers_hand = [deal(), deal()]
