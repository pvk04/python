class Alphabet:
    # Метод инициализации объекта класса
    def __init__(self, language, letters):
        self.language = language
        self.letters = letters

    # метод, который выведет в консоль буквы алфавита
    def print_letters(self):
        print(self.letters)

    #  метод, который вернет количество букв в алфавите
    def count_letters(self):
        letters = self.letters.split(" ")
        return len(letters)


# Создаем класс EngAlphabet путем наследования от класса Alphabet
class EnglishAlphabet(Alphabet):
    def __init__(self):
        super().__init__("English", "a b c d e f g h i j k l m n o p q r s t u v w x y z")
        self.__letters_num = 26

    # метод, который будет принимать букву и определять, относится ли эта буква к английскому алфавиту.
    def is_en(self, letter):
        letters = self.letters.split(" ")
        for let in letters:
            if letter.lower() == let:
                return print("It is an English letter!")
        return print("It's not an english letter")

    # Переопределяем метод count_letters() - в текущем классе он будет возвращать значение свойства __letters_num.
    def count_letters(self):
        print(self.__letters_num)

    # статический метод, который будет возвращать пример текста на английском языке.
    @staticmethod
    def example():
        print("Finding somewhere affordable to live in Britain is hard. Some parts of the country are cheaper than"
              " others, of course, but the cost of renting a home is horrendous, especially in London and the South. "
              "Normally, the only answer is to share a house or a flat: you get a room of your own, but you have to "
              "share the kitchen and bathroom. In cities like Oxford and Cambridge, where rooms are scarce, prices "
              "will make your eyes water: more than £500 a month. In London, they’re even higher – not far off £700.")


if __name__ == "__main__":
    eng = EnglishAlphabet()  # Создайте объект класса EngAlphabet
    print(eng.letters)  # Напечатайте буквы алфавита для этого объекта
    eng.count_letters()  # Выведите количество букв в алфавите
    eng.is_en("F")  # Проверьте, относится ли буква F к английскому алфавиту
    eng.is_en("Щ")  # Проверьте, относится ли буква Щ к английскому алфавиту
    eng.example()  # Выведите пример текста на английском языке
