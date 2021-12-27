# import packages
from tkinter import *
import pandas
import random
# global variables
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# exception handling
try:
    data = pandas.read_csv("data/words_to_learn.csv") # check the data file is exists
except FileNotFoundError: # it not exist
    original_data = pandas.read_csv("data/Sinhala_words.csv")  # read the words data file
    to_learn = original_data.to_dict(orient="records") # add the dat to a dictionary
else:
    to_learn = data.to_dict(orient="records") # if data file exists add the data into dictionary


# display the next card
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer) # remove the timer
    current_card = random.choice(to_learn) # choose a word from the dictionary randomly
    canvas.itemconfig(card_title, text="Sinhala", fill="black") # change the words and font colors
    canvas.itemconfig(card_word, text=current_card["Sinhala"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img) # change the background
    flip_timer = window.after(3000, func=flip_card) # flip the card


# display the other side of the card
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white") # change the text and font colors
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img) # change the background image

# create known word list
def is_known():
    to_learn.remove(current_card) # remove the relevant word from the dictionary
    data = pandas.DataFrame(to_learn) # add the word to the data variable
    data.to_csv("data/words_to_learn.csv", index=False)  # the word to the csv file
    next_card() # call the next card

# window setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card) # set card flip timer

# setup the window body
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png") # add images
card_front = canvas.create_image(400, 263, image=card_front_img) # set the images
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2) # set the positions
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic")) # create text
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, command=next_card) # create button and call the function
unknown_button.grid(row=1, column=0) # set the position

check_img = PhotoImage(file="images/right.png")
known_button = Button(image=check_img, highlightthickness=0, command=is_known) # create button and call the function
known_button.grid(row=1, column=1)


next_card() # show the next card
window.mainloop() # display the window until close
