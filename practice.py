import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Main Window")  # Set the title of the main window
root.geometry("300x200")  # Set the size of the main window (width x height)

# Create a button that opens a new window
open_button = tk.Button(root, text="Open New Window", command=open_new_window)
open_button.pack(pady=20)  # Add some padding around the button

def open_new_window():
    # Create a new window
    new_window = tk.Toplevel(root)
    new_window.title("New Window")  # Set the title of the new window
    new_window.geometry("200x100")  # Set the size of the new window (width x height)

    # Add a label in the new window
    label = tk.Label(new_window, text="This is a new window!")
    label.pack(pady=20)  # Add some padding around the label

    # Add a button to close the new window
    close_button = tk.Button(new_window, text="Close", command=new_window.destroy)
    close_button.pack(pady=10)  # Add some padding around the button

# Start the Tkinter event loop
root.mainloop()
