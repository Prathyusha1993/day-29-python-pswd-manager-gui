from tkinter import *
from tkinter import messagebox
from random import choice, randint,shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web_entry = website_input.get()
    email_entry = email_input.get()
    password_entry = password_input.get()

    if len(web_entry) == 0 or len(password_entry) == 0:
        messagebox.showinfo(title='Oops', message='Please enter all the fields.')
    else:
        is_ok = messagebox.askokcancel(title=web_entry, message=f'These are the details entered: \n Email: {email_entry} '
                                                    f'\nPassword: {password_entry} \n IS it ok to save?')
        if is_ok:
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

password_button = Button(text='Generate Password',command=password_generator)
password_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)







window.mainloop()