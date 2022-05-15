from tkinter import *
import random


class Play:
    def __init__(self, row_num):
        self.text1 = Entry(root, width=4)
        self.text1.bind('<KeyPress>', lambda x: Play.char_limit(self.text1))

        self.text2 = Entry(root, width=4)
        self.text2.bind('<KeyPress>', lambda x: Play.char_limit(self.text2))

        self.text3 = Entry(root, width=4)
        self.text3.bind('<KeyPress>', lambda x: Play.char_limit(self.text3))

        self.text4 = Entry(root, width=4)
        self.text4.bind('<KeyPress>', lambda x: Play.char_limit(self.text4))

        self.text5 = Entry(root, width=4)
        self.text5.bind('<KeyPress>', lambda x: Play.char_limit(self.text5))

        self.grid_elems = [self.text1, self.text2, self.text3, self.text4, self.text5]

        for i in range(len(self.grid_elems)):
            if i == 0:
                self.grid_elems[i].grid(row=row_num, column=i, padx=20)
            else:
                self.grid_elems[i].grid(row=row_num, column=i, padx=20, pady=5)

    @staticmethod
    def char_limit(entry):
        entry.delete('0', END)

    def return_word(self):
        l1 = self.text1.get()
        l2 = self.text2.get()
        l3 = self.text3.get()
        l4 = self.text4.get()
        l5 = self.text5.get()
        word = l1+l2+l3+l4+l5

        return word

    def disable(self):
        self.text1.config(state='disabled')
        self.text2.config(state='disabled')
        self.text3.config(state='disabled')
        self.text4.config(state='disabled')
        self.text5.config(state='disabled')

    def red_light(self):
        # self.grid_elems[num].config({"background": "Red"})
        # self.text1.configure(background='red')
        self.text1["fg"] = 'Red'

    def orange_light(self):
        pass


random_word = ""


# Root
def play():
    list = root.grid_slaves()
    for elem in list:
        elem.destroy()
    root["bg"] = "grey"


    words_file = open("words.txt", "r", encoding="utf-8")
    words = words_file.read().split(" ")
    global random_word
    random_word = words[random.randint(0, len(words) - 1)]
    print(random_word)


    attempt1 = Play(0)


    buttonConfirm = Button(root, text="Проверить", command=lambda: confirm_check(attempt1))
    buttonConfirm.grid(row=5, column=1, columnspan=3, stick='we')

    root.grid_rowconfigure(0, minsize=80)
    root.grid_rowconfigure(1, minsize=80)
    root.grid_rowconfigure(2, minsize=80)
    root.grid_rowconfigure(3, minsize=80)
    root.grid_rowconfigure(4, minsize=80)
    root.grid_rowconfigure(5, minsize=50)


def confirm_check(attempt):
    global random_word
    word1 = attempt.return_word().lower()

    words_file = open("words.txt", "r", encoding="utf-8")
    words = words_file.read().split(" ")

    for word_check in words:
        if word1 == word_check.lower():
            letters = list(word1)
            random_word_list = list(random_word.lower())
            for i in range(len(letters)):
                if letters[i] == random_word_list[i]:
                    print("red")
                    attempt.red_light()
            attempt.disable()







def open_leaderboard():
    pass


def open_rules():
    root.withdraw()
    rules = Toplevel(root)
    rules.geometry("500x450")
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
    button_back.pack(side=BOTTOM)


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
