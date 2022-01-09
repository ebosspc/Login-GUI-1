#####-Imports-#####
# Import tkinter library for api
import tkinter as tk


#####-Main Window-#####
root = tk.Tk()
root.wm_geometry("600x300")

# Set the title
root.title('Authorization')

# Create empty frame with a grid
frame_login = tk.Frame(root)
frame_login.grid()

# Create a Username widget
lbl_username = tk.Label(frame_login, text='Username:', font='Courier')
lbl_username.pack()

# Add username input field for the user
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

# Create a Password widget
lbl_password = tk.Label(frame_login, text='Password:', font='Courier')
lbl_password.pack()

# Add a password input field for the user
ent_password = tk.Entry(frame_login, bd=3, show='*')
ent_password.pack(pady=5)

# Add a button that a user can click to enter their details and login
button_login = tk.Button(frame_login, text='Login')
button_login.pack()

# Keep the window persistent
root.mainloop()
