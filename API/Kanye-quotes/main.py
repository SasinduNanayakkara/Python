# import libraries
from tkinter import *
import requests


def get_quote():
    response = requests.get("https://api.kanye.rest") # connect with the api
    response.raise_for_status() # check the connectivity
    data = response.json() # convert data into json format
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote) # display the quote
    # print(data)


window = Tk() # create an object
window.title("Kanye Says...") # set the title
window.config(padx=50, pady=50)  # set the window

canvas = Canvas(width=300, height=414) # create canvas object
background_img = PhotoImage(file="background.png") # assign a image
canvas.create_image(150, 207, image=background_img) # add image to the canvas
# set up state statement
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0) # set the position

kanye_img = PhotoImage(file="kanye.png") # assign a image
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote) # create a button with an image
kanye_button.grid(row=1, column=0) # set the position



window.mainloop()