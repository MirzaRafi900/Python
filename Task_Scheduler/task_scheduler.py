import tkinter as tk
import sqlite3
from _pyrepl.commands import delete
from asyncio import tasks
from tkinter import StringVar
from tkinter import messagebox

root = tk.Tk()

conn = sqlite3.connect("task.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    priority INTEGER NOT NULL

)
""")
conn.commit()

root.title("Task Scheduler")

root.eval('tk::PlaceWindow . centre')

root.geometry("900x700")

root.configure(bg="#F5F7FA")

root.resizable(False, False)

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
    text = "Stay organized, Stay Focused",
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

    if task == "":
        messagebox.showwarning(
            "Input Error",
            "Please Enter the Task"
        )
        return

    priority = priority_var.get()
    emoji = priority_colors[priority]

    task_list.insert(
        tk.END,
        f"{priority_colors[priority]} {task}"
    )
    update_task_count()

def delete_task():
    selected_task = task_list.curselection()

    if selected_task:
        task_list.delete(selected_task)
        update_task_count()

def update_task_count():
    count = task_list.size()
    task_count.config(
        text = f"Task Count: {count}"
    )


# Buttons

button_frame = tk.Frame()
button_frame.pack(pady=10)

input_button = tk.Button(
    button_frame,
    command = add_task,
    font = ("Segoe UI", 12),
    text = "➕ Add Task",
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
    text = "🗑️ Delete Task",
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

task_heading = tk.Label(
    root,
    font = ("Segoe UI", 12, "bold"),
    text = "Today's Tasks",
    bg = "#F5F7FA",
)
task_heading.pack(pady=5)
task_list = tk.Listbox(
    root,
    font = ("Segoe UI", 16),
    width = 50,
    height = 8,
    bg = "#F5F7FA",
)

task_list.pack(pady=10)

# Task Count

task_count = tk.Label(
    root,
    text = "Task Count",
    font = ("Segoe UI", 10),
    fg = "Grey",
    bg = "#F5F7FA",
)

task_count.pack()

def update_task_count():
    count = task_list.size()
    task_count.config(
        text = f"Task Count: {count}"
    )




root.mainloop()
