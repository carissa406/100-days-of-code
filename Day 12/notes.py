enemies = 1
#shouldn't do this... just RETURN enemies instead
def increase_enemies():
    global enemies #have to say this so that the code below works
    enemies+=1 #cannot just use this bc it doesnt know that the variable enemies exists outside the scope
    print(enemies)

#global constants
#naming convention - all uppercase
URL = "google.com"