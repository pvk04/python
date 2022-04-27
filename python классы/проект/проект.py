from tkinter import *


# Создание классов для кнопок
class App:
    value = str("")
    res_counter = 0  # Вспомогательный счетчик

    def __init__(self, title_name, window_size, bg):
        self.root = Tk()
        self.root.title(title_name)
        self.root.geometry(window_size)
        self.root.resizable(width=False, height=False)
        self.root["bg"] = bg

    @staticmethod
    def create_button(frame, button_text, bg1, width1, height1, command1):
        return Button(frame, text=button_text, bg=bg1, width=width1, height=height1, command=command1)


# Создаем функции для кнопок с цифрами
def but1_click():
    global value
    global res_counter

    if res_counter == 0:
        value += "1"
    else:
        value = "1"
        res_counter = 0

    global ent
    ent["text"] = value


def but2_click():
    global value

    global res_counter

    if res_counter == 0:
        value += "2"
    else:
        value = "2"
        res_counter = 0

    global ent
    ent["text"] = value


def but3_click():
    global value
    global res_counter

    if res_counter == 0:
        value += "3"
    else:
        value = "3"
        res_counter = 0

    global ent
    ent["text"] = value


def but4_click():
    global value
    global res_counter

    if res_counter == 0:
        value += "4"
    else:
        value = "4"
        res_counter = 0

    global ent
    ent["text"] = value


def but5_click():
    global value
    global res_counter

    if res_counter == 0:
        value += "5"
    else:
        value = "5"
        res_counter = 0

    global ent
    ent["text"] = value


def but6_click():
    global value
    global res_counter

    if res_counter == 0:
        value += "6"
    else:
        value = "6"
        res_counter = 0

    global ent
    ent["text"] = value


def but7_click():
    global value
    global res_counter

    if res_counter == 0:
        value += "7"
    else:
        value = "7"
        res_counter = 0

    global ent
    ent["text"] = value


def but8_click():
    global value
    global res_counter

    if res_counter == 0:
        value += "8"
    else:
        value = "8"
        res_counter = 0

    global ent
    ent["text"] = value


def but9_click():
    global value
    global res_counter

    if res_counter == 0:
        value += "9"
    else:
        value = "9"
        res_counter = 0

    global ent
    ent["text"] = value


def but0_click():
    global value
    global res_counter

    if res_counter == 0:
        value += "0"
    else:
        value = "0"
        res_counter = 0

    global ent
    ent["text"] = value


# Функция для кнопки очистки
def del_click():
    global value
    value = ""
    global ent
    ent["text"] = value


# Функция для кнопки результат
def result():
    global value
    global ent
    global res_counter

    res_counter = 1

    try:
        res = 1
        for i in range(1, int(value)+1):
            res *= i

        value = str(res)
        ent["text"] = str(value)
    except Exception:
        ent["text"] = str("Введите значение")

if __name__ == "__main__":
    # Создание интерфейса окна
    app = App("Калькулятор факториалов", "500x450", "white")


    key = Frame(app.root, width=500, height=440, bg="white")  # Фрейм для кнопок

    header = Frame(app.root, width=24, height=20, bg="white")  # Хэдер
    lab1 = Label(header, text="Введите число для вычисления факториала:", width=200, bg='white', font=("Courier", 12))  # Надпись в хэдере

    ent = Label(app.root, width=28, bg='light blue', font=("Courier", 20))  # Вывод

    # Создание кнопок и их расположение в окне
    buttons_text = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "!", "Del"]
    functions = {0: but1_click, 1: but2_click, 2: but3_click, 3: but4_click, 4: but5_click,
                 5: but6_click, 6: but7_click, 7: but8_click, 8: but9_click, 9: but0_click, 10: result, 11: del_click}

    buttons_array = []

    position_x = [50, 185, 320, 50, 185, 320, 50, 185, 320, 185, 320, 50]
    position_y = [15, 15, 15, 100, 100, 100, 185, 185, 185, 270, 270, 270]

    for i in range(len(buttons_text)):
        buttons_array.append(App.create_button(key, buttons_text[i], "white", 15, 4, functions[i]))
        buttons_array[i].place(x=position_x[i], y=position_y[i])

    # Расоложение в окне
    header.pack(side=TOP)
    lab1.pack(side=LEFT)
    ent.pack()
    key.place(x=0, y=62)

    app.root.mainloop()
