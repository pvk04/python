from tkinter import *
import pymysql
from config import host, user, password, db_name


############################################# Functions ################################################################

# Auth
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
    global account_id
    login = entry_login.get()
    password = entry_password.get()

    if login == "" or password == "":
        error_label["text"] = 'Заполните все поля!'
    if login != "" and password != "":
        cursor.execute("SELECT * FROM accounts;")
        logins = cursor.fetchall()
        for login_row in logins:
            if login_row["login"] == login and login_row["password"] == password:
                account_id = login_row["idaccounts"]
                root.deiconify()
                auth.destroy()
                return
    try:
        error_label["text"] = 'Неверный логин или пароль'
    except Exception:
        pass


# Root
def play():
    root.withdraw()
    play_win = Toplevel(root)
    play_win.geometry("500x450")
    play_win.resizable(width=False, height=False)
    play_win.title("Игра")

    lvl_request = "SELECT text FROM level, "


def open_leaderboard():
    pass


def open_rules():
    root.withdraw()
    rules = Toplevel(root)
    rules.geometry("500x450")
    rules.resizable(width=False, height=False)
    rules.title("Правила")

    rules_lab = Label(rules, font=("Montserrat", 14), wraplength=450)
    rules_lab["text"] = "Вам дается задача и вы должны ее решить и вписать ответ в окно. Если ответ верный, " \
                        "вам зачисляются очки. Если неверный, вы переходите к следующей задаче."
    rules_lab.pack(side=TOP, pady=70)

    button_back = Button(rules, text="Назад", font=("Montserrat", 14), command=lambda: back(rules, root))
    button_back.pack(side=BOTTOM, pady=70)


def open_stat():
    pass


def back(window, global_win):
    window.destroy()
    global_win.deiconify()


################################################### MYSQL ##############################################################


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


##################################################### GUI ##############################################################


# GUI

root = Tk()
root.title("Приложение")
root.geometry("500x450")
root.resizable(width=False, height=False)
root["bg"] = "white"

menu_lab = Label(root, text="МЕНЮ", bg="white", font=("Montserrat", 20))
menu_lab.grid(row=0, column=1, columnspan=3, stick='we')

button_play = Button(root, text="Играть", font=("Montserrat", 14), command=play)
button_play.grid(row=1, column=1, columnspan=3, stick='we')

button_stat = Button(root, text="Статистика", font=("Montserrat", 14))
button_stat.grid(row=2, column=1, columnspan=3, stick='we')

button_leaderboard = Button(root, text="Таблица лидеров", font=("Montserrat", 14))
button_leaderboard.grid(row=3, column=1, columnspan=3, stick='we')

button_rules = Button(root, text="Правила", font=("Montserrat", 14), command=open_rules)
button_rules.grid(row=4, column=1, columnspan=3, stick='we')


root.grid_columnconfigure(0, minsize=100)
root.grid_columnconfigure(1, minsize=100)
root.grid_columnconfigure(2, minsize=100)
root.grid_columnconfigure(3, minsize=100)
root.grid_columnconfigure(4, minsize=100)

root.rowconfigure(0, minsize=100)
root.rowconfigure(1, minsize=60)
root.rowconfigure(2, minsize=60)
root.rowconfigure(3, minsize=60)
root.rowconfigure(4, minsize=60)



# Authentification

auth = Toplevel(root)
auth.geometry("400x200")
auth.title("Авторизация")
auth.resizable(width=False, height=False)
auth["bg"] = "white"

account_id = 0

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

root.withdraw()
root.mainloop()
