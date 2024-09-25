import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)  # Add task to the listbox
        entry.delete(0, tk.END)       # Clear the entry field
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to remove the selected task
def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

# Function to mark task as checked/unchecked
def toggle_task():
    try:
        selected_task_index = listbox.curselection()[0]
        current_task = listbox.get(selected_task_index)

        # Toggle the checked state by modifying the task string
        if current_task.startswith("[✔] "):
            new_task = current_task.replace("[✔] ", "")
        else:
            new_task = "[✔] " + current_task

        listbox.delete(selected_task_index)
        listbox.insert(selected_task_index, new_task)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to check/uncheck.")

# Function to delete all checked tasks
def delete_checked_tasks():
    tasks_to_delete = []
    
    for i in range(listbox.size()):
        if listbox.get(i).startswith("[✔] "):
            tasks_to_delete.append(i)
    
    for index in reversed(tasks_to_delete):
        listbox.delete(index)
    
    if not tasks_to_delete:
        messagebox.showinfo("Info", "No checked tasks to delete.")

# GUI Setup
def setup_gui():
    root = tk.Tk()
    root.title("To-Do List")
    root.geometry("400x500")
    root.configure(bg="#f0f0f0")

    # Task Entry Field
    global entry
    entry = tk.Entry(root, font=("Arial", 14), width=25)
    entry.pack(pady=10)

    # Add Task Button
    add_button = tk.Button(root, text="Add Task", width=15, font=("Arial", 12), bg="#99ff99", command=add_task)
    add_button.pack(pady=10)

    # Task List (Listbox)
    global listbox
    listbox = tk.Listbox(root, font=("Arial", 14), width=30, height=10, bg="#ffffff", bd=2)
    listbox.pack(pady=20)

    # Remove Task Button
    remove_button = tk.Button(root, text="Remove Task", width=15, font=("Arial", 12), bg="#ff9999", command=remove_task)
    remove_button.pack(pady=5)

    # Check/Uncheck Task Button
    check_button = tk.Button(root, text="Check/Uncheck Task", width=15, font=("Arial", 12), bg="#99ccff", command=toggle_task)
    check_button.pack(pady=5)

    # Delete Checked Tasks Button
    delete_button = tk.Button(root, text="Delete Checked", width=15, font=("Arial", 12), bg="#ff6666", fg="white", command=delete_checked_tasks)
    delete_button.pack(pady=5)

    root.mainloop()

# Run the To-Do List app
setup_gui()
