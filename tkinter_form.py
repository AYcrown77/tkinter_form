"""
Create a tkinter GUI form that collects user information such as name,email and age.
Include validation for email field to ensure that it follows basic email format
Show user info when Submit Button is clicked
"""
#import Tkinter module
import tkinter as tk
from tkinter import messagebox

def form_submit():
    #Get user information
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()

    #Check for empty fields
    if not name or not email or not age:
        messagebox.showerror("Error","Fields can not be empty")
    #Validate the email format
    elif '@' not in email and '.' not in email:
        messagebox.showerror("Error","Invalid Email Adreess")
    #Display user information
    else:
        information = f"Name: {name}\nEmail: {email}\nAge: {age}"
        messagebox.showinfo("User Information",information)

#Gui Part
window = tk.Tk()
window.title("User Entry Form")
window.geometry('400x240')

#Show the label and entry field
name_label= tk.Label(window, text="Name:",font=('times new roman',20,'bold'))
name_label.grid(row =0, column=0)
name_entry = tk.Entry(window)
name_entry.grid(row=0,column=1,pady=15,padx=10)

email_label = tk.Label(window, text="Email:",font=('times new roman',20,'bold'))
email_label.grid(row=1,column=0)
email_entry = tk.Entry(window)
email_entry.grid(row=1,column=1,pady=15,padx=10)

age_label = tk.Label(window, text="Age:",font=('times new roman',20,'bold'))
age_label.grid(row =2,column=0)
age_entry = tk.Entry(window)
age_entry.grid(row=2,column=1,pady=15,padx=10)

button = tk.Button(window, text = "Submit",font=('times new roman',20,'bold'),command=form_submit)
button.grid(row=3,column=1,)

window.mainloop()
