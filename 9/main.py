#from replit import clear
#HINT: You can call clear() to clear the output in the console.
#since I'm not using replit I searched an alternative:
import os
#os.system('cls')
import art

print(art.logo)

begin = True
bids = []
while begin == True:
    print("Welcome to the secret auction program.")
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    bids.append({"name":name,
                 "bid":bid})

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.: ")

    if more_bidders == "no":
        highest_bid = 0
        for entry in bids:
            if entry["bid"] > highest_bid:
                highest_bid = entry["bid"]
                winner = entry["name"]
        begin = False
        os.system('cls')
        print(f"The winner is {winner} with a bid of ${highest_bid}")
    else:
        os.system('cls')
