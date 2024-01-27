import tkinter as tk

def on_button_click():
    label.config(text="Hello, " + entry.get())

# Create the main window
window = tk.Tk()
window.title("Simple GUI Example")

# Create widgets
label = tk.Label(window, text="Enter your name:")
entry = tk.Entry(window)
button = tk.Button(window, text="Click me!", command=on_button_click)

# Pack widgets to arrange them in the window
label.pack()
entry.pack()
button.pack()

# Start the main event loop
window.mainloop()