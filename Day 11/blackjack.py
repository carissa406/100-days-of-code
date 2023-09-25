import art
import random

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt


def calculate_score(list):
    score = 0
    for i in list:
        score = score + i
    if 11 in player_hand and player_score > 21:
        player_hand.remove(11)
        player_hand.append(1)
        return calculate_score(player_hand)
    return score

print(art.logo)
#initial start of the game
computer_hand = random.choices(cards, k=2)
player_hand = random.choices(cards, k=2)
computer_score = calculate_score(computer_hand)
player_score = calculate_score(player_hand)

print(f"Your cards: {player_hand}, current score: {calculate_score(player_hand)}")
print(f"Computer's first card: {computer_hand[0]}")

if computer_score == 21:
    print("You lose")
elif player_score == 21:
    print("You win!")
else:
    choice = input("Type 'y' to get another card, type 'n' to pass: ")
    should_continue = True

    while should_continue:
        if choice == 'y':
            new_card = random.choice(cards)
            player_hand.append(new_card)
            print(f"Your cards: {player_hand}, current score: {calculate_score(player_hand)}")
            print(f"Computer's first card: {computer_hand[0]}")
            player_score = calculate_score(player_hand)
            if player_score > 21:
                should_continue = False
            else:
                choice = input("Type 'y' to get another card, type 'n' to pass: ")
        if choice == 'n':
            should_continue = False

    while computer_score <= 16:
        new_card = random.choice(cards)
        computer_hand.append(new_card)
        computer_score = calculate_score(computer_hand)

    if player_score > 21:
        print("You lost!")
    elif computer_score == 21 and player_score == 21:
        print("It was a tie!")
    elif computer_score == 21:
        print("You lost!")
    elif player_score == 21:
        print("You won!")
    elif player_score > computer_score:
        print("You won!")
    elif computer_score > player_score:
        print("You lost!")
