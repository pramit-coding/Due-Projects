import tkinter as tk
import random


choices = ["Rock", "Paper", "Scissors"]

def show_random_choice():
   
    label.config(text=random.choice(choices))


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x200")


label = tk.Label(root, text="", font=("Arial", 20))
label.pack(pady=40)


show_random_choice()

root.after(1000, lambda: update_loop())

def update_loop():
    show_random_choice()
    root.after(1000, update_loop) 

root.mainloop()


#I am not quite sure how to use denomination in this projecct because there is no value/cuirrency


