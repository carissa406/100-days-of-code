from art import logo
import random
print(logo)

print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
goal = random.randint(1,100)

def guessing_game(attempts):
    goal_reached = False
    while attempts > 0 and goal_reached == False:
        print(f"You have {attempts} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        if guess == goal:
            print(f"You guessed it right! The number was: {goal}")
            goal_reached = True
        elif guess > goal:
            print("Too high.\n Guess Again.")
            attempts -= 1
        elif guess < goal:
            print("Too low. \n Guess Again.")
            attempts -= 1
        else:
            print("You didn't type a valid number...\n Guess Again.")

if difficulty == "easy":
    attempts = 10
    guessing_game(attempts)
elif difficulty == "hard":
    attempts = 5
    guessing_game(attempts)

    