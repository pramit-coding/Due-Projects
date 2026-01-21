import tkinter as tk
import random


choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    
    computer_choice = random.choice(choices)

    
    if user_choice == computer_choice:
        result = "Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Better luck next time!"

    
    u_label.config(text=f"Your Choice: {user_choice}")
    c_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=result)


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")
root.resizable(False, False)


u_label = tk.Label(root, text="Your Choice: None", font=("Arial", 12))
u_label.pack(pady=10)

c_label = tk.Label(root, text="Computer's Choice: None", font=("Arial", 12))
c_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue")
result_label.pack(pady=10)


button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)


root.mainloop()

# I used AI help so I could understand the mechanics of the game(program)

