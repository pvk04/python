from tkinter import *
import pymysql
from config import host, user, password, db_name
from main import root


#  Объявление функций

def registration():
    login = entry_login.get()
    password = entry_password.get()
    check = True
    print(login)
    print(password)

    if login == "" or password == "":
        error_label["text"] = 'Заполните все поля!'
        check = False
    elif " " in login:
        error_label["text"] = 'В логине не может быть пробелов!'
        check = False
    elif " " in password:
        error_label["text"] = 'В пароле не может быть пробелов!'
        check = False
    elif login != "" and password != "":
        cursor.execute("SELECT login FROM accounts;")
        logins = cursor.fetchall()
        for login_row in logins:
            print(login_row)
            if login_row["login"] == login:
                error_label["text"] = 'Такой логин занят!'
                check = False
    if check:
        cursor.execute(f"insert into accounts (login, password) values ('{str(login)}', '{str(password)}');")
        connection.commit()
        error_label["text"] = 'Вы зарегистрировались'


def login():
    login = entry_login.get()
    password = entry_password.get()
    print(login)
    print(password)

    if login == "" or password == "":
        error_label["text"] = 'Заполните все поля!'
    if login != "" and password != "":
        cursor.execute("SELECT * FROM accounts;")
        logins = cursor.fetchall()
        for login_row in logins:
            print(login_row)
            if login_row["login"] == login and login_row["password"] == password:
                print("Вход успешно выполнен...")
                root.deiconify()
                auth.destroy()
    try:
        error_label["text"] = 'Неверный логин или пароль'
    except Exception:
        pass

########################################################################################################################


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


# Окно авторизации
root.withdraw()
auth = Tk()
auth.geometry("400x200")
auth.title("Авторизация")
auth.resizable(width=False, height=False)
auth["bg"] = "white"

auth_lab1 = Label(auth, text="Войдите или зарегистрируйтесь", bg="white", font=("Courier", 12))
auth_lab1.grid(row=0, column=0, columnspan=4)

auth_lab2 = Label(auth, text="Логин", bg="white", font=("Courier", 10))
auth_lab2.grid(row=2, column=0)
entry_login = Entry(auth, bd=3)
entry_login.grid(row=2, column=1, columnspan=2, stick='we')

auth_lab3 = Label(auth, text="Пароль", bg="white", font=("Courier", 10))
auth_lab3.grid(row=5, column=0)
entry_password = Entry(auth, bd=3)
entry_password.grid(row=5, column=1, columnspan=2, stick='we')

error_label = Label(auth, text="", font=("Courier", 12), bg="white")
error_label.grid(row=6,column=1, columnspan=2)
login_btn = Button(auth, text="Вход", font=("Courier", 12), bg="blue", fg="yellow", command=login)
login_btn.grid(row=7, column=1, stick='w')
register_btn = Button(auth, text="Регистрация", font=("Courier", 12), bg="blue", fg="yellow", command=registration)
register_btn.grid(row=7, column=2)

auth.grid_columnconfigure(0, minsize=100)
auth.grid_columnconfigure(1, minsize=100)
auth.grid_columnconfigure(2, minsize=100)
auth.grid_columnconfigure(3, minsize=100)

auth.rowconfigure(1, minsize=20)
auth.rowconfigure(2, minsize=20)

auth.mainloop()
