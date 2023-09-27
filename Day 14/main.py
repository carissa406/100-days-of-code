import game_data
import art
import random
import os

winning = True
current_score = 0

compare = random.choices(game_data.data, k=2)
a = compare[0]
b = compare[1]

while winning == True:
    print(art.logo)

    if a['follower_count'] > b['follower_count']:
        highest = 'A'
    else:
        highest = 'B'

    print(f"Current score is: {current_score}")
    print(f"Compare A: {a['name']}, a {a['description']} from {a['country']}.")
    print(art.vs)
    print(f"Against B: {b['name']}, a {b['description']} from {b['country']}.")

    guess = input("Who has more followers? Tyle 'A' or 'B': ")

    if guess == highest:
        current_score += 1
        a = b
        b = random.choice(game_data.data)
        os.system('cls')
    else: 
        print("You got it wrong.")
        print(f"Current score is: {current_score}")
        winning = False