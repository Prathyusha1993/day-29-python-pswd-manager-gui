from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web_entry = website_input.get()
    email_entry = email_input.get()
    password_entry = password_input.get()

    with open('data.txt', 'a') as f:
        f.write(f'{web_entry} | {email_entry} | {password_entry}\n')
        website_input.delete(0, END)
        password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager Using GUI')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
my_logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=my_logo)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, 'prathyusha@gmail.com')

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

password_button = Button(text='Generate Password')
password_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)







window.mainloop()