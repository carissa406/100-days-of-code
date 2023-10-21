with open("afile.txt") as file:
    contents = file.read()
    print(contents)

with open("afile.txt", mode ='w') as file: #mode='a' to append a new line of text, default is mode r read, if file does not exist it will create it for us
    file.write("\nnew text.")

#relative file path
#absolute file path