****/

# Title

title_label = tk.Label(
    root,
    text="Task Manager",
    font=("Segoe UI", 22, "bold")
)

title_label.pack(pady=10)

# Subtitle

subtitle = tk.Label(
    root,
    text="Manage your daily tasks efficiently",
    font=("Segoe UI", 14, "italic")
)

subtitle.pack(pady=10)

# Task Input

task_input = tk.Entry(
    root,
    font=("Segoe UI", 19, "bold"),
    width = 40
)

task_input.pack(pady=10)

# Task List

task_list = tk.Listbox(
    root,
    height = 6,
    width=50,
    font=("Segoe UI", 16, "bold"),

)

task_list.pack(pady=10)

# Logic Add

def add_task():
    task = task_input.get()

    if task != "":
        task_list.insert(
            tk.END,
            task
        )
        task_input.delete(
            0,
            tk.END,
        )

# Adding Button

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(
    button_frame,
    text="Add Task",
    font=("Segoe UI", 16, "bold"),
    command=add_task
)

add_button.pack(
    side="left",
    padx =10
)

#Deleting Tasks

def delete_task():
    selected_task = task_list.curselection()

    if selected_task:
        task_list.delete(selected_task)

delete_button = tk.Button(
    button_frame,
    text="Delete Task",
    font=("Segoe UI", 16, "bold"),
    command=delete_task
)

delete_button.pack(
    side="left",
    padx =10
)

/***
