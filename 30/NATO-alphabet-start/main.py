student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

#TODO 1. Create a dictionary in this format:
df = pandas.read_csv("Day 26/NATO-alphabet-start/nato_phonetic_alphabet.csv")
for (index, row) in df.iterrows():
    nato_dict = {row.letter:row.code for (index,row) in df.iterrows()}
#print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Please enter a word to translate to NATO: ").upper()
legal = True
while legal:
    try:
        output_list = [nato_dict[letter] for letter in word]
        print(output_list)
        legal = False
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        word = input("Please enter a word to translate to NATO: ").upper()
