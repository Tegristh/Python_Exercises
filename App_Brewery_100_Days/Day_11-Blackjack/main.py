
import random
from replit import clear # Shows an error on this import because we are not in replit.com
from art import logo


def deal_card():
    """Return a random card in the card list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def first_round():
    """return the start hand of card for player and computer"""
    player = []
    computer = []
    player.append(deal_card())
    player.append(deal_card())
    computer.append(deal_card())
    computer.append(deal_card())
    return player, computer


def count_score(hand):
    """return the score of the cards hand, replace as value (11 by 1) if needed"""
    if sum(hand) > 21 and hand.count(11) > 0:
        hand[hand.index(11)] = 1
        count_score(hand)
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    return sum(hand)


def compare(user, computer):
    """return results"""
    if user == computer:
        return f"It's a Draw ( computer: {computer}, user: {user}"
    elif computer == 0:
        return "Computer has a blackjack, user loose"
    elif user == 0:
        return "User has a blackjack and win"
    elif user > 21:
        return "User exceed 21 and loose"
    elif computer > 21:
        return "Computer exceed 21, user win"
    elif user > computer:
        return f"User : {user}, computer: {computer}, User win"
    else:
        return f"User : {user}, computer: {computer}, User loose"


def game():
    print(logo)
    player_hand, computer_hand = first_round()
    computer_turn = False
    while not computer_turn:
        player_score = count_score(player_hand)
        computer_score = count_score(computer_hand)
        print(
            f"player: {player_score}, computer's first card: {computer_hand[0]}")
        if computer_score == 0 or player_score == 0 or player_score > 21:
            computer_turn = True
        else:
            if input("Do you want another card? 'yes' or 'no': ") == "yes":
                player_hand.append(deal_card())
            else:
                computer_turn = True

    while count_score(computer_hand) < 17 and count_score(computer_hand) != 0:
        computer_hand.append(deal_card())
        computer_score = count_score(computer_hand)
    print(compare(player_score, computer_score))


game_continue = True

while game_continue:
    clear() #Wont work out of replit.com
    game()
    if input("Do you want another game? 'yes' or 'no': ") == "no":
        game_continue = False
