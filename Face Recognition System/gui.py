import tensorflow as tf
from tensorflow import keras
import numpy as np
from keras.models import load_model
import numpy as np
import cv2
import os
from tkinter import *
from datacollect import click
from test import main


root= Tk()
root.geometry("800x430")
root.title("Face Recognision")

bg = PhotoImage(file = "backimg.png")
  
# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)

label2 = Label( root, text = "Welcome to Face Recognision Project",
               bg = "#88cffa")
label2.pack(padx=100,pady = 20)

button = Button(root,text="For Creating your dataset of your face",command=click,font=("Comic Sans",15),fg="#00FF00",bg="black",activeforeground="#00FF00",
                activebackground="black",state=ACTIVE)

button.pack(padx=100,pady=25)

button2 = Button(root,text="Click Here! If you want to know that which celebrity you look like",command=main,font=("Comic Sans",15),fg="#00FF00",bg="black",activeforeground="#00FF00",
                activebackground="black",state=ACTIVE)

button2.pack(padx=100, pady=30)

exit_button = Button(root, text="Exit", command=root.destroy,font=("Comic Sans",15),fg="#00FF00",bg="black",activeforeground="#00FF00",
                activebackground="black",state=ACTIVE)
exit_button.pack(padx=100, pady=35)

root.mainloop()