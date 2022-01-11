#####-Imports-#####
# Import tkinter library for api
import tkinter as tk


#####-Main Window-#####
# Create a 420x420 window for the gui
root = tk.Tk()
root.wm_geometry("420x420")

# Set the title
root.title('Multicolored GUI')

# Create the blue frame
blue_frame = tk.Frame(root, height=210, width=275, background='blue')
blue_frame.grid(row=0, column=0, sticky='news')

# Create the green frame
green_frame = tk.Frame(root, height=210, width=145, background='green')
green_frame.grid(row=0, column=1, sticky='news')

# Create the red frame
red_frame = tk.Frame(root, height=210, width=275, background='red')
red_frame.grid(row=1, column=0, sticky='news')

# Create the yellow frame
green_frame = tk.Frame(root, height=210, width=145, background='yellow')
green_frame.grid(row=1, column=1, sticky='news')

# Keep the window persistent
root.mainloop()
