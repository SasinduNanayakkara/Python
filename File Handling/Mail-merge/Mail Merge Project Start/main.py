PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as name_file:  # read the file
    names = name_file.readlines() # assign values as list

with open("./Input/Letters/starting_letter.txt") as letter_file: # read the file
    letter = letter_file.read() # assign value to the variable

    for name in names:
        stripped_name = name.strip() # reduce the spaces
        new_letter = letter.replace(PLACEHOLDER, stripped_name) # replace the '[name]' to relevant name
        # create a new file in given location
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter) # add the text to the letter
