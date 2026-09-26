import tkinter as tk
from _pyrepl.commands import delete
from tkinter import StringVar

root = tk.Tk()

root.title("Task Scheduler")

root.geometry("900x700")

root.configure(bg="#F5F7FA")

# Title

task_label = tk.Label(
    root,
    text="Task Manager",
    font = ("Segoe UI", 22, "bold"),
)
task_label.pack(pady=10)

# Subtitle

subtitle = tk.Label(
    root,
    text="Manage your daily tasks",
    font = ("Segoe UI", 16, "italic"),
)

subtitle.pack(pady=5)

# Input Box

task_entry = tk.Entry(
    root,
    width = 50,
    font = ("Segoe UI", 13, "italic"),
)

task_entry.pack(pady=10)

# Task Listing

task_list = tk.Listbox(
    root,
    width = 70,
    height = 12,
    font = ("Segoe UI", 13, "bold"),
)

task_list.pack(pady=10)

# Logics

def add_task():
    task = task_entry.get()

    priority = priority_var.get()

    emoji = priority_colors[priority]

    if task != "":
        task_entry.delete(
            0,
            tk.END,
        )

        task_list.insert(
            tk.END,
            f"{priority_colors[priority]} | {task}"
        )

        task_entry.delete(
            0,
            tk.END
        )

def remove_task():
    selected_task = task_list.curselection()

    if selected_task:
        task_list.delete(selected_task)

# Priority
priority_label = tk.Label(
    root,
    text="Priority",
    font = ("Segoe UI", 12, "bold"),
 )
priority_label.pack(pady=10)

priority_var = tk.StringVar()
priority_var.set("Medium")

priority_menu = tk.OptionMenu(
    root,
    priority_var,
    "High",
    "Medium",
    "Low",
)

priority_colors={
    "High": "[High]",
    "Medium": "[Medium]",
    "Low": "[Low]"
}


priority_menu.pack()

# Adding Buttons

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(
    button_frame,
    text="Add Task",
    command=add_task,
    font = ("Segoe UI", 12, "bold"),
    bg = "#4CAF50",
    fg = "white",
    width = 12,
)

add_button.pack(
    side = "left",
    padx = 10
)

delete_button = tk.Button(
    button_frame,
    text="Delete Task",
    command=remove_task,
    bg="#E53935",
    fg="white",
    font = ("Segoe UI", 12, "bold"),


)
delete_button.pack(
    side = "left",
    padx = 10
)




root.mainloop()
