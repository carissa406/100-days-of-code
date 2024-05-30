class User:
    def __init__(self, user_id, username): #always need self parameter
        self.id = user_id
        self.username = username
        self.followers = 0 #default value, no need for it to be required when initializing the class
        self.following = 0

    def follow(self, user):
        user.followers += 1 #when a user follows another user, the users followers go up
        self.following += 1 #OUR following goes up by 1 cause we're following them

user_1 = User("001", "carissa")
user_2 = User('002', 'nicole')

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

#this is another way to do this if we didnt already declare that user required two attributes user_id and username
""" 
class User:
    pass
    
user_2 = User()
user_2.id = '002'
user_2.username = 'nicole' 
"""


