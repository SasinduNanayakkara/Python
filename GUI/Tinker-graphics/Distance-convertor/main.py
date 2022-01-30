from tkinter import *


def miles_to_km():
    miles = float(mile_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}") # print the value


window = Tk() # create object

window.title("Miles to Kilo convertor") # add a title
window.config(padx=20, pady=20) # set the position
mile_input = Entry(width=7) # get the input
mile_input.grid(column=1, row=0) # set the position

mile_label = Label(text="Miles") # display text
mile_label.grid(column=2, row=0) # set the position

is_equal_to_label = Label(text="is equal to ") # display text
is_equal_to_label.grid(column=0, row=1) # set the position

kilometer_result_label = Label(text="0") # display text
kilometer_result_label.grid(column=1, row=1) # set the position

kilometer_label = Label(text="km") # display text
kilometer_label.grid(column=2, row=1) # set the position

calculate_button = Button(text="Calculate", command=miles_to_km) # add a button
calculate_button.grid(column=1, row=2) # set the position

window.mainloop()