print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
perc = int(input("What percentage of tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_per_person = round(((perc/100) * bill)/people + (bill/people), 2)

print(f"Each person should pay: ${total_per_person}")

