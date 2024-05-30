#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#to avoid a unicode error
#get list of all the names
with open(r"Day 24\Mail Merge Project Start\Input\Names\invited_names.txt") as file:
    names = file.read().splitlines()

#get the contents of the starting letter
with open(r"Day 24\Mail Merge Project Start\Input\Letters\starting_letter.txt") as file:
    contents = file.read()

#write a new file for each name with the contents of the starting letter in it
for name in names:
    with open(f"Day 24\Mail Merge Project Start\Output\ReadyToSend\letter_for_{name}", mode ='w') as file:
        new_letter = contents
        file.write(new_letter.replace("[name]", name))
        