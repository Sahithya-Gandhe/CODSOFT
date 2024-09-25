import random
import tkinter as tk
from tkinter import messagebox

# Function to determine the winner
def check_winner(user_choice):
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
    else:
        result = "You lose!"

    result_message = f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}"
    messagebox.showinfo("Result", result_message)

# GUI setup
def setup_gui():
    root = tk.Tk()
    root.title("Rock, Paper, Scissors")
    root.geometry("400x400")
    root.configure(bg='#f0f0f0')

    # Header Label
    label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 20, "bold"), bg='#f0f0f0', fg="#333")
    label.pack(pady=20)

    # Instruction Label
    tk.Label(root, text="Choose your move:", font=("Arial", 14), bg='#f0f0f0', fg="#333").pack(pady=10)

    # Color palette for buttons
    button_color = {'Rock': '#ff9999', 'Paper': '#99ccff', 'Scissors': '#99ff99'}

    # Buttons for Rock, Paper, Scissors
    tk.Button(root, text="Rock", width=15, height=2, font=("Arial", 12), bg=button_color['Rock'],
              command=lambda: check_winner("Rock")).pack(pady=10)
    tk.Button(root, text="Paper", width=15, height=2, font=("Arial", 12), bg=button_color['Paper'],
              command=lambda: check_winner("Paper")).pack(pady=10)
    tk.Button(root, text="Scissors", width=15, height=2, font=("Arial", 12), bg=button_color['Scissors'],
              command=lambda: check_winner("Scissors")).pack(pady=10)

    # Exit button
    tk.Button(root, text="Exit", width=15, height=2, font=("Arial", 12), bg='#ff6666', fg="white",
              command=root.quit).pack(pady=20)

    # Start the main event loop
    root.mainloop()

# Run the game
setup_gui()
