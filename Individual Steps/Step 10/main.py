#####-Imports-#####
# Import tkinter library for api
import tkinter as tk


#####-Main Window-#####
root = tk.Tk()
root.wm_geometry("600x300")

# Set the title
root.title('Authorization')

# Create empty frame
frame_login = tk.Frame(root)

# Create grid
frame_login.grid()

# Create a label widget
lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()

# Keep the window persistent
root.mainloop()
