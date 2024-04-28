import tkinter as tk
from tkinter import simpledialog
from pymongo import MongoClient

# Connect to the MongoDB database
client = MongoClient('mongodb+srv://prathameshgarade:masaladosa@ads.ddoy7h9.mongodb.net/?retryWrites=true&w=majority&appName=ADS')
db = client['ADS']
collection = db['tempokpo']

# Create a function to insert a new user
def insert_user():
    name = entry_name.get()
    id = entry_id.get()
    password = entry_password.get()
    phone_no = entry_phone_no.get()
    user = {'name': name, 'id': id, 'password': password, 'phone_no': phone_no}
    collection.insert_one(user)
    label_success.config(text='User inserted successfully')

# Create a function to update a user
def update_user():
    # Get the ID from the user
    id = simpledialog.askstring("Update User", "Enter User ID:")

    if not id:
        # If the ID is not provided, display an error message
        label_error.config(text='Please provide an ID')
        return

    # Check if the ID exists in the database
    filter = {'id': id}
    user = collection.find_one(filter)

    if user:
        # If the ID exists, open a new window to update the user data
        update_window = tk.Toplevel(root)

        # Create labels and entry fields for the user data
        label_name = tk.Label(update_window, text='Name')
        label_name.grid(row=0, column=0)
        entry_name = tk.Entry(update_window)
        entry_name.grid(row=0, column=1)
        entry_name.insert(0, user['name'])

        label_phone_no = tk.Label(update_window, text='Phone No.')
        label_phone_no.grid(row=1, column=0)
        entry_phone_no = tk.Entry(update_window)
        entry_phone_no.grid(row=1, column=1)
        entry_phone_no.insert(0, user['phone_no'])

        label_password = tk.Label(update_window, text='Password')
        label_password.grid(row=2, column=0)
        entry_password = tk.Entry(update_window)
        entry_password.grid(row=2, column=1)
        entry_password.insert(0, user['password'])

        # Create a button to save the updated user data
        button_save = tk.Button(update_window, text='Save', command=lambda: save_updated_user(id, entry_name.get(), entry_phone_no.get(), entry_password.get(), update_window))
        button_save.grid(row=3, column=0)

        # Center the window on the screen
        update_window.geometry('+{}+{}'.format(root.winfo_rootx() + 50, root.winfo_rooty() + 50))

    else:
        # If the ID does not exist, display an error message
        label_error.config(text='ID not found')

# Create a function to save the updated user data
def save_updated_user(id, name, phone_no, password, update_window):
    # Update the user data in the database
    filter = {'id': id}
    update = {'$set': {'name': name, 'phone_no': phone_no, 'password': password}}
    collection.update_one(filter, update)

    # Close the update window
    update_window.destroy()

    # Display a success message
    label_success.config(text='User updated successfully')

# Create a function to delete a user
def delete_user():
    # Get the ID from the user
    id = simpledialog.askstring("Delete User", "Enter User ID:")

    if not id:
        # If the ID is not provided, display an error message
        label_error.config(text='Please provide an ID')
        return

    # Check if the ID exists in the database
    filter = {'id': id}
    user = collection.find_one(filter)

    if user:
        # If the ID exists, delete the user
        collection.delete_one(filter)
        label_success.config(text='User deleted successfully')
    else:
        # If the ID does not exist, display an error message
        label_error.config(text='ID not found')

# Create the Tkinter app
root = tk.Tk()
root.title('MongoDB User Management')

# Create form to insert a new user
label_name = tk.Label(root, text='Name')
label_name.grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

label_id = tk.Label(root, text='ID')
label_id.grid(row=1, column=0)
entry_id = tk.Entry(root)
entry_id.grid(row=1, column=1)

label_password = tk.Label(root, text='Password')
label_password.grid(row=2, column=0)
entry_password = tk.Entry(root)
entry_password.grid(row=2, column=1)
 
label_phone_no = tk.Label(root, text='Phone No.')
label_phone_no.grid(row=3, column=0)
entry_phone_no = tk.Entry(root)
entry_phone_no.grid(row=3, column=1)

button_insert = tk.Button(root, text='Insert', command=insert_user)
button_insert.grid(row=4, column=0)

label_success = tk.Label(root, text='')
label_success.grid(row=5, column=0)

button_update = tk.Button(root, text='Update', command=update_user)
button_update.grid(row=4, column=1)

button_delete = tk.Button(root, text='Delete', command=delete_user)
button_delete.grid(row=4, column=2)

label_error = tk.Label(root, text='')
label_error.grid(row=5, column=1)

root.mainloop()
