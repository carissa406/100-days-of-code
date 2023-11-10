#try - might cause error
#except - do this if error
#else - if no errors
#finally - do no matter what

try:
    file = open('Day 30/a_file.txt')
    a_dictionary = {"key": "value"}
    print(a_dictionary["asdsdad"])
except FileNotFoundError as error_msg:
    print(error_msg)
    file = open('Day 30/a_file.txt', 'w')
    file.write("something")
except KeyError as error_message: 
    #get error message that was generated
    print(f"{error_message} doesn't exist")
else:
    content = file.read()
    print(content)
finally:
    # file.close()
    # print("file was closed")
    # print("ssss")
    raise TypeError("This is an error I made up")

# try:
#     file = open('Day 30/a_file.txt')
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["asdsdad"])
# except FileNotFoundError:
#     file = open('Day 30/a_file', 'w')
#     file.write("something")
# except KeyError as error_message: 
#     print(f"{error_message} doesn't exist")


# height = some input
# weight = some input

#if height > 3:
    #raise ValueError("Human height should not be over 3 meters")

# bmi = weight / height ** 2
# print(bmi)