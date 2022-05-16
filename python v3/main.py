from tkinter import *
import pymysql
from config import host, user, password, db_name
import random

############################################# Functions ################################################################
attempts_num = 5


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
    elif len(login) < 6 or len(password) < 6:
        error_label["text"] = 'Логин и пароль должны быть длиннее 6 символов'
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
    root.title("Игра")
    list = root.grid_slaves()
    for elem in list:
        elem.destroy()
    root["bg"] = "grey"

    words_file = open("words.txt", "r", encoding="utf-8")
    words = words_file.read().split(" ")
    random_word = words[random.randint(0, len(words) - 1)]
    print(random_word)

    lab1 = Label(root, text="Введите слово:", font=("Montserrat", 11), bg='grey')
    lab1.grid(row=0, column=1, columnspan=2, sticky='ws')

    global attempts_num
    attempts_num = 5
    lab2 = Label(root, text=f"Попытки: {attempts_num}", font=("Montserrat", 11), bg='grey')
    lab2.grid(row=0, column=3, sticky='se')

    entry_word = Entry(root, font=("Montserrat", 14), justify=CENTER, bd=5)
    entry_word.bind('<KeyPress>', lambda x: char_limit(entry_word, '4'))
    entry_word.grid(row=1, column=1, columnspan=3, sticky='we')

    lab3 = Label(root, text="Найденные буквы:", font=("Montserrat", 11), bg='grey')
    lab3.grid(row=2, column=1, sticky='ws')

    frame_letters = Frame(root, bg='red', width=300, height=100)
    frame_letters.grid(row=3, rowspan=2, column=1, columnspan=3, sticky='wnes')

    frame_letters.grid_rowconfigure(0, minsize=60)
    frame_letters.grid_rowconfigure(1, minsize=60)
    frame_letters.grid_rowconfigure(2, minsize=60)
    frame_letters.grid_rowconfigure(3, minsize=60)
    frame_letters.grid_rowconfigure(4, minsize=60)

    button_try = Button(root, text="Проверить", font=("Montserrat", 12), command=lambda: check_word(entry_word, random_word, words, lab_err, lab2))
    button_try.grid(row=5, column=1, columnspan=3, sticky='we', pady=10)

    lab_err = Label(root, text="", bg='grey', fg='red', font=("Montserrat", 10))
    lab_err.grid(row=6, column=0, columnspan=5)

    root.grid_columnconfigure(0, minsize=90)
    root.grid_columnconfigure(1, minsize=90)
    root.grid_columnconfigure(2, minsize=90)
    root.grid_columnconfigure(3, minsize=90)
    root.grid_columnconfigure(4, minsize=90)


def char_limit(entry, count):
    entry.delete(count, END)


def check_word(entry, solve, arr, err, attempts_lab):
    global attempts_num
    users_word = entry.get().lower()
    solve = solve.lower()
    contains = False
    err["text"] = ""
    word_for_check = ""

    letters_contains = []

    if users_word == solve and attempts_num != 0:
        list = root.grid_slaves()
        for elem in list:
            elem.destroy()

        lab = Label(root, text="Вы угадали!", font=("Montserrat", 20))
        lab.grid(row=0, column=1, columnspan=3)

        lab1 = Label(root, text=f"Вы получаете: {attempts_num*10} очков", font=("Montserrat", 14))
        lab1.grid(row=1, column=1, columnspan=3, sticky='we')

        button_play_again = Button(root, text="Играть снова", font=("Montserrat", 14), command=play)
        button_play_again.grid(row=2, column=2, pady=10)

        button_menu = Button(root, text="Меню", font=("Montserrat", 14))
        button_menu.grid(row=3, column=2, pady=10)
    elif attempts_num == 0:
        pass
    else:
        for elem in arr:
            if users_word == elem.lower():
                contains = True
                word_for_check = elem.lower()
                print("true")
                break

    if contains:
        for let in range(len(solve)):
            if solve[let] == word_for_check[let]:
                letters_contains.append(solve[let])
        print(letters_contains)
        attempts_num -= 1
    else:
        err["text"] = "Такого слова нет в нашем словаре"


    attempts_lab["text"] = f"Попыток: {attempts_num}"

def open_leaderboard():
    pass


def open_rules():
    root.withdraw()
    rules = Toplevel(root)
    rules.title("Правила")
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    w = w // 2
    h = h // 2
    rules.geometry(f'500x450+{w - 250}+{h - 225}')
    rules.resizable(width=False, height=False)
    rules.title("Правила")

    rules_lab = Label(rules, font=("Montserrat", 14), wraplength=450)
    rules_lab["text"] = "Игра загадывает слово и вам нужно его отгадать. " \
                        "Вы должны ввести любое существующее слово из 5 букв. " \
                        "Если буквы из введенного слова есть в загаданном  слове и они находяться в этом же месте, " \
                        "то они подсветятся красным, если на другом месте - оранжевым. Если их нет," \
                        " то они не подсветятся"
    rules_lab.pack(side=TOP, pady=70)

    button_back = Button(rules, text="Назад", font=("Montserrat", 14), command=lambda: back(rules, root))
    button_back.pack(side=BOTTOM, pady=10)


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
root.title("Главное меню")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2  # середина экрана
h = h//2
root.geometry(f'500x450+{w-250}+{h-225}')
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


# Auth
auth = Toplevel(root)
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2
h = h//2
auth.geometry(f'400x200+{w-200}+{h-100}')
auth.title("Авторизация")
auth.resizable(width=False, height=False)
auth["bg"] = "white"

account_id = 0

auth_lab1 = Label(auth, text="Войдите или зарегистрируйтесь", bg="white", font=("Montserrat", 12))
auth_lab1.grid(row=0, column=0, columnspan=4)

auth_lab2 = Label(auth, text="Логин", bg="white", font=("Montserrat", 10))
auth_lab2.grid(row=2, column=0)
entry_login = Entry(auth, bd=3)
entry_login.bind('<KeyPress>', lambda x: char_limit(entry_login, '14'))
entry_login.grid(row=2, column=1, columnspan=2, stick='we')

auth_lab3 = Label(auth, text="Пароль", bg="white", font=("Montserrat", 10))
auth_lab3.grid(row=5, column=0)
entry_password = Entry(auth, bd=3)
entry_password.bind('<KeyPress>', lambda x: char_limit(entry_password, '14'))
entry_password.grid(row=5, column=1, columnspan=2, stick='we')

error_label = Label(auth, text="", font=("Montserrat", 12), bg="white", wraplength=240)
error_label.grid(row=6,column=1, columnspan=2)
login_btn = Button(auth, text="Вход", font=("Montserrat", 12), bg="blue", fg="yellow", command=login)
login_btn.grid(row=7, column=1, stick='w')
register_btn = Button(auth, text="Регистрация", font=("Montserrat", 12), bg="blue", fg="yellow", command=registration)
register_btn.grid(row=7, column=2)

auth.grid_columnconfigure(0, minsize=100)
auth.grid_columnconfigure(1, minsize=100)
auth.grid_columnconfigure(2, minsize=100)
auth.grid_columnconfigure(3, minsize=100)

auth.rowconfigure(1, minsize=20)
auth.rowconfigure(2, minsize=20)

root.withdraw()
root.mainloop()
