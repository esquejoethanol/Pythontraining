import tkinter as tk

def open_new_window():
    # Create a new window
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    # Add a label in the new window
    label = tk.Label(new_window, text="This is a new window!")
    label.pack(pady=20)  # Add some padding around the label


    close_button = tk.Button(new_window, text="Close", command=new_window.destroy)
    close_button.pack(pady=10)

# Create the main window
root = tk.Tk()
root.title("Main Window")
root.geometry("600x400")

# Load the image (make sure to use a GIF or PPM/PGM image)
background_image = tk.PhotoImage(file="C:\\Users\\me\\Downloads\\bg.gif")  # Replace with your GIF image path

# Create a label to hold the background image
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)  # Make the label fill the entire window

# Create a button that opens a new window
open_button = tk.Button(root, text="Open New Window", command=open_new_window)
open_button.pack(pady=20)  # Add some padding around the button

# Start the Tkinter event loop
root.mainloop()