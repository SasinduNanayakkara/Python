import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv") # get the data from the csv file



# loop through the alphabet data and create new dictionary assigning letter and code
word_dict = {row.letter: row.code for (index, row) in alphabet.iterrows()}


def generate_phonetic():
    word = input("Enter a word : ").upper() # get the input as uppercase word

    try:
        result = [word_dict[letter] for letter in word] # loop through the input and find the match letters and get the relevent code and assign to a list
    except KeyError:
        print("Sorry, only letters in the alphabet")
        generate_phonetic()
    else:
        print(result) # print the list

generate_phonetic()