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



root.mainloop()
