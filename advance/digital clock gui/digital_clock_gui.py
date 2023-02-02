# Start with importing the libraries.
from tkinter import Label, Tk

import time

# Define the title and size of our application.
app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("420x150")
# Set the function to False(0, 0) if you want a fixed window size.
app_window.resizable(1, 1)

# Define the font of the time and its colour.
# Set the border width and the background colour of the digital clock.
text_font = ("Boulder", 68, 'bold')
background = "#0d1117"
foreground = "#58a6ff"
border_width = 25

# Combine all the elements to define the label of the clock application.
label = Label(app_window, font = text_font, bg = background, fg = foreground, bd = border_width)
label.grid(row = 0, column = 1)

# Define the main function of our digital clock.
# Set the text of the label as the realtime.
def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text = time_live)
    label.after(200, digital_clock)

digital_clock()

app_window.mainloop()