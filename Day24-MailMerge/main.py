with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()

with open("./Input/Names/invited_names.txt") as file:
    names = file.read().split("\n")

for name in names:
    new_file = "./Output/ReadyToSend/"+ name + ".txt"
    with open(new_file, mode="w") as file:
        file.write(letter.replace("[name]", name))
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp