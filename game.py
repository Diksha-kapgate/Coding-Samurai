from tkinter import *
import random
from PIL import Image, ImageTk  # For handling .jpg images

ng = Tk()
ng.title('Guessing Numbers')
ng.geometry('550x370')

# Load the background image
background_image = Image.open("guess.jpg")  # Replace with your image file path
background_photo = ImageTk.PhotoImage(background_image)

# Add a canvas to display the background
canvas = Canvas(ng, width=1000, height=800)
canvas.pack(fill="both", expand=True)

# Add the image to the canvas
canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Generate a random number and set up game variables
ranNum = random.randint(0, 10)
chance = 3
var = IntVar()
disp = StringVar()


# Function to check the guessed number
def check_guess():
    global ranNum
    global chance
    usr_ip = var.get()
    if chance > 0:
        if usr_ip == ranNum:
            msg = f'Congratulations You Won! {ranNum} You Guessed the right answer.'
            
        elif usr_ip > ranNum:
            chance -= 1
            msg = f'{usr_ip} is greater. You have {chance} attempt left.'
        elif usr_ip < ranNum:
            chance -= 1
            msg = f'{usr_ip} is smaller. You have {chance} attempt left.'
        else:
            msg = 'Something Went Wrong!'

    else:
        msg = f'You Lost! you have {chance} attempt left.'

    disp.set(msg)

# Add game widgets on top of the canvas
title_label = Label(
    ng,
    text='Number Guessing Game',
    
    font=('sans-serif', 13),
    bg='#B0E0E6'
)
canvas.create_window(273, 30, window=title_label)  # Centered on canvas 

entry = Entry(
    ng,
    textvariable=var,
    font=('sans-serif', 12)
)
canvas.create_window(273, 120, window=entry)

submit_button = Button(
    ng,
    text='Submit',
    font=('sans-serif', 12),
    command=check_guess
)
canvas.create_window(273, 180, window=submit_button)


result_label = Label(
    ng,
    textvariable=disp,
    font=('sans-serif', 10),
    bg='#5671A6'
)
canvas.create_window(273, 250, window=result_label)

ng.mainloop()













