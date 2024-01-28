import tkinter as tk
import json


class Task:

  def __init__(self, window, task_id, description, on_remove):
    self.task_id = task_id
    self.description = description

    self.checkbox_var = tk.BooleanVar()
    self.checkbox = tk.Checkbutton(window, variable=self.checkbox_var)
    self.label = tk.Label(window, text=f"You have to do: {self.description}.")

    self.checkbox.pack()
    self.label.pack()

    self.checkbox_var.trace_add('write', on_remove)

  def remove(self):
    self.checkbox_var.set(False)
    self.checkbox.destroy()
    self.label.destroy()


def on_button_click(username, password, window, data):
  account = ""
  for acc, account_data in data["Accounts"].items():
    if account_data["Username"] == username.get(
    ) and account_data["Password"] == password.get():
      account = acc
      window.destroy()
      ToDoList(account, data)


def register(username, password, window, data):
  if username.get() in data["Accounts"]:
    print("Username already taken. Choose a different username.")
  else:
    new_account_id = str(len(data["Accounts"]) + 1)
    data["Accounts"][new_account_id] = {
        "Username": username.get(),
        "Password": password.get(),
        "Tasks": {}
    }

    with open("data.json", "w") as file:
      json.dump(data, file, indent=2)

    print("Account registered successfully.")
    window.destroy()
    ToDoList(new_account_id, data)


def add_task(task_entry, window, account, data):
  new_task_description = task_entry.get().strip()

  if new_task_description:
    task_id = str(len(data["Accounts"][account]["Tasks"]) + 1)
    data["Accounts"][account]["Tasks"][task_id] = new_task_description

    with open("data.json", "w") as file:
      json.dump(data, file, indent=2)

    window.destroy()
    ToDoList(account, data)
  else:
    print("Please enter a task before adding.")


def remove_selected_tasks(tasks_frame, account, data):
  to_remove = []
  for task in tasks_frame:
    if task.checkbox_var.get():
      del data["Accounts"][account]["Tasks"][task.task_id]
      to_remove.append(task)

  with open("data.json", "w") as file:
    json.dump(data, file, indent=2)

  for task in to_remove:
    task.remove()

  tasks_frame[:] = [task for task in tasks_frame if task not in to_remove]


def logout(window):
  window.destroy()
  login_screen(data)


def ToDoList(account, data):
  window = tk.Tk()
  window.geometry("300x400")
  window.title("To Do List")

  tasks_frame = []

  for task_id, task_description in data["Accounts"][account]["Tasks"].items():
    task = Task(window, task_id, task_description,
                lambda *_: remove_selected_tasks(tasks_frame, account, data))
    tasks_frame.append(task)

  add_task_entry = tk.Entry(window)
  add_task_button = tk.Button(
      window,
      text="Add Task",
      command=lambda: add_task(add_task_entry, window, account, data))
  logout_button = tk.Button(window,
                            text="Logout",
                            command=lambda: logout(window))

  add_task_entry.pack()
  add_task_button.pack()
  logout_button.pack()

  window.mainloop()


def login_screen(data):
  window = tk.Tk()
  window.title("Login")
  window.geometry("200x300")

  label = tk.Label(window, text="Username: ")
  username = tk.Entry(window)
  label2 = tk.Label(window, text="Password: ")
  password = tk.Entry(window, show="*")
  login_button = tk.Button(
      window,
      text="Login",
      command=lambda: on_button_click(username, password, window, data))
  register_button = tk.Button(
      window,
      text="Register",
      command=lambda: register(username, password, window, data))

  label.pack(pady=5)
  username.pack(pady=5)
  label2.pack(pady=5)
  password.pack(pady=5)
  login_button.pack(pady=10)
  register_button.pack(pady=5)

  window.mainloop()


# Load data from JSON file
with open("data.json", 'r') as file:
  data = json.load(file)

# Start the login screen
login_screen(data)
