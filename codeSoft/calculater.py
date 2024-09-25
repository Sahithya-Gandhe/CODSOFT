import tkinter as tk

# Function to handle button clicks and display the value
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

# Function to calculate the result
def calculate():
    try:
        current = entry.get()
        result = eval(current)  # Evaluate the expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the display
def clear_display():
    entry.delete(0, tk.END)

# Create the GUI window
def create_calculator_gui():
    root = tk.Tk()
    root.title("Simple Calculator")
    root.geometry("400x500")
    root.configure(bg='#f0f0f0')

    global entry
    entry = tk.Entry(root, font=("Arial", 20), bd=8, insertwidth=2, width=14, borderwidth=4, justify='right')
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

    # Define button colors
    button_color = "#99ccff"
    operator_color = "#ff9999"
    clear_color = "#ff6666"
    
    # Button layout
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 3),
    ]

    # Create number and operator buttons
    for (text, row, col) in buttons:
        bg_color = operator_color if text in ['/', '*', '-', '+'] else button_color
        tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), bg=bg_color,
                  command=lambda t=text: button_click(t)).grid(row=row, column=col, padx=5, pady=5)

    # Clear and Equal buttons
    tk.Button(root, text="C", padx=20, pady=20, font=("Arial", 14), bg=clear_color, command=clear_display).grid(row=4, column=2, padx=5, pady=5)
    tk.Button(root, text="=", padx=20, pady=20, font=("Arial", 14), bg=operator_color, command=calculate).grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

    root.mainloop()

# Run the calculator
create_calculator_gui()
