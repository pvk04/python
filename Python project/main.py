from tkinter import *
import pymysql
from config import host, user, password, db_name


# MYSQL

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Successfully connected...")

    try:
        cursor = connection.cursor()
        print("Cursor created...")
    except Exception as ex:
        print("Failet to create cursor...")
        print(ex)
except Exception as ex:
    print("Connection failed...")
    print(ex)

########################################################################################################################

def registration():
    login = entry_login.get()
    password = entry_password.get()
    print(login)
    print(password)

    if login == "":
        entry_login.delete(0, 'end')
        entry_login.insert(0, 'Поле не может быть пустым!')
    if password == "":
        entry_password.delete(0, 'end')
        entry_password.insert(0, 'Поле не может быть пустым!')
    if login != "" and password != "":
        cursor.execute("SELECT login FROM accounts;")
        logins = cursor.fetchall()
        for login_row in logins:
            print(login_row)
            if login_row["login"] == login:
                entry_login.delete(0, 'end')
                entry_login.insert(0, 'Такой логин занят!')
        if " " in login:
            entry_login.delete(0, 'end')
            entry_login.insert(0, 'В логине не может быть пробелов!')
        if " " in password:
            entry_password.delete(0, 'end')
            entry_password.insert(0, 'В пароле не может быть пробелов!')
        if " " not in login and " " not in password:
            cursor.execute(f"insert into accounts (login, password) values ('{str(login)}', '{str(password)}');")
            connection.commit()

def login():
    login = entry_login.get()
    password = entry_password.get()
    print(login)
    print(password)

    if login == "":
        entry_login.delete(0, 'end')
        entry_login.insert(0, 'Поле не может быть пустым!')
    if password == "":
        entry_password.delete(0, 'end')
        entry_password.insert(0, 'Поле не может быть пустым!')
    if login != "" and password != "":
        cursor.execute("SELECT * FROM accounts;")
        logins = cursor.fetchall()
        for login_row in logins:
            print(login_row)
            if login_row["login"] == login and login_row["password"] == password:
                print("Вход успешно выполнен...")
                break  # вход в основное приложение
            else:
                print("Неправильный логин или пароль")
########################################################################################################################

# Окно авторизации

auth = Tk()
auth.geometry("420x200")
auth.title("Авторизация")
auth.resizable(width=False, height=False)
auth["bg"] = "white"

auth_lab1 = Label(auth, text="Для продолжения необходимо авторизоваться", bg="white", font=("Courier", 12)).pack(side=TOP)

auth_lab2 = Label(auth, text="Логин", bg="white", font=("Courier", 10)).pack(side=TOP)
entry_login = Entry(auth, width=40, bd=3)
entry_login.pack()

auth_lab3 = Label(auth, text="Пароль", bg="white", font=("Courier", 10)).pack(side=TOP)
entry_password = Entry(auth, width=40, bd=3)
entry_password.pack()

login_btn = Button(auth, text="Вход", font=("Courier", 12), bg="blue", fg="yellow", command=login).pack()
register_btn = Button(auth, text="Регистрация", font=("Courier", 12), bg="blue", fg="yellow", command=registration).pack()


auth.mainloop()
