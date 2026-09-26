import tkinter as tk

root = tk.Tk()

root.title("Task Scheduler")

root.geometry("600x400")

# Title

title_label = tk.Label(
    root,
    text="Task Scheduler",
    font=("Times new Roman", 20, "bold")
)

title_label.pack(pady=10)

# Task Input

task_input = tk.Entry(
    root,
    font=("Times new Roman", 20, "bold"),
    width = 40
)

task_input.pack(pady=10)

# Task List

task_list = tk.Listbox(
    root,
    font=("Times new Roman", 20, "bold"),
    width = 40,
    height = 10

)

task_list.pack(pady=10)


root.mainloop()
