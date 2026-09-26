import tkinter as tk
from _pyrepl.commands import delete
from tkinter import StringVar

root = tk.Tk()

root.title("Task Scheduler")

root.geometry("1920x1080")

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
    "Low"
)

priority_colors = {
    "High" : "[High]",
    "Medium" : "[Medium]",
    "Low" : "[Low]",
}

priority_menu.pack()

# Task List

task_list = tk.Listbox(
    root,
    font = ("Segoe UI", 16),
    width = 70,
    height = 20,
    bg = "#F5F7FA",
)

task_list.pack(pady=10)



root.mainloop()
