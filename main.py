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

with open("Data.json", 'r') as file:
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
    window.geometry("200x300")
    window.title("To Do list")

    for task_id, task_description in data["Accounts"][account]["Tasks"].items():
        label = tk.Label(window, text=f"You have to do: {task_description}.")
        label.pack()

    # Start the main event loop for the ToDoList window
    window.mainloop()

# Start the login screen
LoginScreen()
