import tkinter as tk
import json

account = 0

def on_button_click(Username, Password, window):
    global account

    for acc, account_data in data["Accounts"].items():
        if account_data["Username"] == Username.get() and account_data["Password"] == Password.get():
            account = acc
        window.destroy()
        ToDoList()

def Add_task(task_entry, window):
    new_task_description = task_entry.get()

    # Add the new task to the data
    task_id = str(len(data["Accounts"][account]["Tasks"]) + 1)
    data["Accounts"][account]["Tasks"][task_id] = new_task_description

    # Write the updated data back to the file
    with open("data.json", "w") as file:
        json.dump(data, file, indent=2)

    # Refresh the ToDoList window to display the updated tasks
    window.destroy()
    ToDoList()

with open("data.json", 'r') as file:
    data = json.load(file)

def LoginScreen():
    # Create the main window
    window = tk.Tk()
    window.title("Login")
    window.geometry("200x300")

    # Create widgets
    label = tk.Label(window, text="Username: ")
    Username = tk.Entry(window)
    label2 = tk.Label(window, text="Password: ")
    Password = tk.Entry(window, show="*")
    button = tk.Button(window, text="Submit", command=lambda: on_button_click(Username, Password, window))

    # Pack widgets to arrange them in the window
    label.pack()
    Username.pack()
    label2.pack()
    Password.pack()
    button.pack()

    # Start the main event loop
    window.mainloop()

def ToDoList():
    window = tk.Tk()
    window.geometry("200x400")
    window.title("To Do list")

    tasks_frame = tk.Frame(window)
    tasks_frame.pack()

    for task_id, task_description in data["Accounts"][account]["Tasks"].items():
        label = tk.Label(tasks_frame, text=f"You have to do: {task_description}.")
        label.pack()

    AddTask = tk.Entry(window)
    AddTaskButton = tk.Button(window, text="Add Task", command=lambda: Add_task(AddTask, window))

    # Pack the new widgets
    AddTask.pack()
    AddTaskButton.pack()

    # Start the main event loop for the ToDoList window
    window.mainloop()

# Start the login screen
LoginScreen()
