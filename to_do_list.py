import tkinter as tk
from tkinter import messagebox
import os

TASKS_FILE = "tasks.txt"


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            for line in f:
                task = line.strip()
                if task:
                    listbox.insert("end", task)

def save_tasks():
    with open(TASKS_FILE, "w") as f:
        tasks = listbox.get(0, "end")
        for task in tasks:
            f.write(task + "\n")

def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert("end", task)
        entry.delete(0, "end")
        save_tasks()
    else:
        messagebox.showerror("Error", "Task cannot be empty.")

def update_task():
    try:
        selected_index = listbox.curselection()[0]
        new_task = entry.get().strip()
        if new_task:
            listbox.delete(selected_index)
            listbox.insert(selected_index, new_task)
            entry.delete(0, "end")
            save_tasks()
        else:
            messagebox.showerror("Error", "Updated task cannot be empty.")
    except IndexError:
        messagebox.showerror("Error", "Please select a task to update.")

def remove_task():
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
        save_tasks()
    except IndexError:
        messagebox.showerror("Error", "Please select a task to remove.")

def mark_complete():
    try:
        selected_index = listbox.curselection()[0]
        task = listbox.get(selected_index)
        if not task.startswith("[Done] "):
            listbox.delete(selected_index)
            listbox.insert(selected_index, "[Done] " + task)
            save_tasks()
    except IndexError:
        messagebox.showerror("Error", "Please select a task to mark complete.")

def clear_tasks():
    if messagebox.askyesno("Confirm", "Delete all tasks?"):
        listbox.delete(0, "end")
        save_tasks()


root = tk.Tk()
root.title("To-Do List")
root.geometry("450x400")

# Entry field
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Buttons
frame = tk.Frame(root)
frame.pack(pady=5)

add_btn = tk.Button(frame, text="Add Task", command=add_task)
add_btn.grid(row=0, column=0, padx=5)

update_btn = tk.Button(frame, text="Update Task", command=update_task)
update_btn.grid(row=0, column=1, padx=5)

remove_btn = tk.Button(frame, text="Remove Task", command=remove_task)
remove_btn.grid(row=0, column=2, padx=5)

done_btn = tk.Button(frame, text="Mark Complete", command=mark_complete)
done_btn.grid(row=0, column=3, padx=5)

clear_btn = tk.Button(frame, text="Clear All", command=clear_tasks)
clear_btn.grid(row=0, column=4, padx=5)


listbox = tk.Listbox(root, width=60, height=15, selectmode="single")
listbox.pack(pady=10)

# Load tasks from file
load_tasks()

root.mainloop()
