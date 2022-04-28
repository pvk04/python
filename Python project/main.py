from tkinter import *

# Окно авторизации
auth = Tk()
auth.geometry("420x200")
auth.title("Авторизация")
auth.resizable(width=False, height=False)
auth["bg"] = "white"

auth_lab1 = Label(auth, text="Для продолжения необходимо авторизоваться", bg="white", font=("Courier", 12)).pack(side=TOP)

auth_lab2 = Label(auth, text="Логин", bg="white", font=("Courier", 12)).pack(side=TOP)
entry_login = Entry(auth, width=40, bd=3).pack()

auth_lab3 = Label(auth, text="Пароль", bg="white", font=("Courier", 12)).pack(side=TOP)
entry_password = Entry(auth, width=40, bd=3).pack()

login_btn = Button(auth, text="Вход", font=("Courier", 12), bg="blue", fg="yellow").pack()
register_btn = Button(auth, text="Регистрация", font=("Courier", 12), bg="blue", fg="yellow").pack()


auth.mainloop()
