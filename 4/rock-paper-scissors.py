choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.")

import random
computer_choice = random.randint(0,2)

rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

list = [rock, paper, scissors]

choice = int(choice)
computer_choice = int(computer_choice)

print(list[choice])
print(list[computer_choice])

if choice == computer_choice:
    print("It was a draw.")
elif (choice == 0 and computer_choice == 1) or (choice == 1 and computer_choice == 2) or (choice == 2 and computer_choice == 0):
    print("You win")
else: 
    print("You lost")