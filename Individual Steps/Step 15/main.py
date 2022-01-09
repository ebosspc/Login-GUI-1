#####-Imports-#####
# Import tkinter library for api
import tkinter as tk


#####-Main Window-#####
root = tk.Tk()
root.wm_geometry("200x100")

# Set the title
root.title('Authorization')

# Create empty frame with a grid
frame_login = tk.Frame(root)
frame_login.grid()

# Create a Username widget
lbl_username = tk.Label(frame_login, text='Username:', font='Courier')
lbl_username.pack()

# Create a Password widget
lbl_password = tk.Label(frame_login, text='Password:', font='Courier')
lbl_password.pack()

# Keep the window persistent
root.mainloop()
