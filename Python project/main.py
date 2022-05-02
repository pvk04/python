from tkinter import *


# Functions
def play():
    root.withdraw()
    play_win = Toplevel(root)
    play_win.geometry("500x450")
    play_win.resizable(width=False, height=False)
    play_win.title("Игра")


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

########################################################################################################################


# Menu window
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


# root.mainloop()  # Не забыть убрать эту строчку
