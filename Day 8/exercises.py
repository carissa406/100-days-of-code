# Exercise 1
#TODO-1 Create a function called greet(), 
#write 3 print statements inside the function
#call the greet() function and run code

""" def greet():
    print("hello")
    print("python")
    print("world")
greet() """

""" def greet_with_name(name):
    print(f"hello {name}")
greet_with_name("Carissa") """

""" #functions with more than one argument
def greet_with(name, location):
    print(f"hey there {name}")
    print(F"what's it like in {location}")
#call with positional argument
greet_with("Delilah", "New York City")

#call functions with keyword arguments
greet_with(location = "Seattle", name = "Carissa") """

#TODO-2 Prime Number Generator
#Write your code below this line 👇

""" def prime_checker(number):
    count = 0
    for i in range (1, number+1):
        if number % i == 0:
            count +=1
    if count > 2 or count == 1:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n) """