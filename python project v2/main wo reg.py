from tkinter import *

# Root
def play():
    list = root.grid_slaves()
    for elem in list:
        elem.destroy()

    root["bg"] = "grey"

    text1 = Entry(root, width=4)
    text1.grid(row=0, column=0, padx=20)
    text1.bind('<KeyPress>', lambda x: char_limit(text1))

    text2 = Entry(root, width=4)
    text2.grid(row=0, column=1, padx=20, pady=5)
    text2.bind('<KeyPress>', lambda x: char_limit(text2))

    text3 = Entry(root, width=4)
    text3.grid(row=0, column=2, padx=20, pady=5)
    text3.bind('<KeyPress>', lambda x: char_limit(text3))

    text4 = Entry(root, width=4)
    text4.grid(row=0, column=3, padx=20, pady=5)
    text4.bind('<KeyPress>', lambda x: char_limit(text4))

    text5 = Entry(root, width=4)
    text5.grid(row=0, column=4, padx=20, pady=5)
    text5.bind('<KeyPress>', lambda x: char_limit(text5))

    buttonConfirm = Button(root, text="Проверить")
    buttonConfirm.grid(row=5, column=1, columnspan=3, stick='we')

    root.grid_rowconfigure(0, minsize=80)
    root.grid_rowconfigure(1, minsize=80)
    root.grid_rowconfigure(2, minsize=80)
    root.grid_rowconfigure(3, minsize=80)
    root.grid_rowconfigure(4, minsize=80)
    root.grid_rowconfigure(5, minsize=50)


def char_limit(entry):
    entry.delete('0', END)





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


root.mainloop()