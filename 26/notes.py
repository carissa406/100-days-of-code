# #list comprehension
# #new_list = [do_something_to_each_item_in_list for item in list]
# #one line of code to do something to each item in list to make a new list 

# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
# print(new_numbers)

# #each letter in the name is a separate string in a list
# name = "angela"
# new_letters = [letter for letter in name]
# print(new_letters)

# new_range = [n*2 for n in range(1,5)]
# print(new_range)

# #conditional list comprehension
# #new_list = [new_item for item in list if test]

# names = ["Alex", "Carissa", "Beth"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)

# uppercase_long_names = [name.upper() for name in names if len(name) > 5]
# print(uppercase_long_names)

# #dictionary comprehension
# #new_dict = {new_key:new_value for item in list}
# #new_dict = {new_key:new_value for (key,value) in dict.items() if test}
# import random
# #give random score to each name in list, put in dictionary
# names = ["Alex", "Carissa", "Beth"]
# student_scores = {student:random.randint(1, 100) for student in names}
# print(student_scores)

# passed_students = {student:score for (student,score) in student_scores.items() if score >= 80}
# print(passed_students)

# #iterate over pandas dataframe
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#loop through data frame
#rows, each student, each score
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)

# new_dictionary = {new_key:new_value} for (index, row) in df.itterows()}