import tkinter as tk
from _pyrepl.commands import delete
from tkinter import StringVar

root = tk.Tk()

root.title("Task Scheduler")

root.geometry("1000x750")

root.configure(bg="#F5F7FA")

# Title

task_label = tk.Label(
    root,
    font = ("Segoe UI", 22, "bold"),
    text = "Task Scheduler",
)
task_label.pack(pady=10)

# Subtitle

subtitle = tk.Label(
    root,
    font = ("Segoe UI", 16, "italic"),
    text = "For Your Daily Assistance",
)

subtitle.pack(pady=10)

# Task Input

input_frame = tk.Frame(
    root,
    bg="#F5F7FA"
)
input_frame.pack(pady=10)

Input_label = tk.Label(
    input_frame,
    text = "Enter the Task",
    font = ("Segoe UI", 12),
)
Input_label.pack(
    side = "left",
    padx = 5
)

task_entry = tk.Entry(
    input_frame,
    font = ("Segoe UI", 12),
    width = 50,
    bg = "#F5F7FA",
)

task_entry.pack(
    side = "left",
    padx = 5
)

# Priority List

priority_frame = tk.Frame(
    root,
    bg = "#F5F7FA"
)

priority_frame.pack(pady=10)

task_priority = tk.Label(
    priority_frame,
    text = "Priority",
    font = ("Segoe UI", 12),
)
task_priority.pack(pady=10)

priority_var = tk.StringVar()
priority_var.set("Medium")

priority_menu = tk.OptionMenu(
    priority_frame,
    priority_var,
    "Medium",
    "High",
    "Low",
)

priority_colors = {
    "High" : "😓",
    "Medium" : "😎",
    "Low" : "😴",
}

priority_menu.pack()

# Functions

def add_task():
    task = task_entry.get()

    priority = priority_var.get()

    emoji = priority_colors[priority]

    if task !="":
        task_entry.delete(
            0,
            tk.END
        )
        task_list.insert(
            tk.END,
            f"{priority_colors[priority]} {task}"
        )

def delete_task():
    selected_task = task_list.curselection()

    if selected_task:
        task_list.delete(selected_task)

# Buttons

button_frame = tk.Frame()
button_frame.pack(pady=10)

input_button = tk.Button(
    button_frame,
    command = add_task,
    font = ("Segoe UI", 12),
    text = "Input",
    bg = "Green",
    fg = "#F5F7FA",
    borderwidth = 12,
)
input_button.pack(
    side = "left",
    padx = 5
)

delete_button = tk.Button(
    button_frame,
    font = ("Segoe UI", 12),
    text = "Delete",
    command = delete_task,
    bg = "Red",
    fg = "#F5F7FA",
    borderwidth = 12,
)
delete_button.pack(
    side = "left",
    padx = 5
)
# Task List

task_list = tk.Listbox(
    root,
    font = ("Segoe UI", 16),
    width = 50,
    height = 10,
    bg = "#F5F7FA",
)

task_list.pack(pady=10)




root.mainloop()
