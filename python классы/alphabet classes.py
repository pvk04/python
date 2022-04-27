class Alphabet:
    def __init__(self, language, letters):
        self.language = language
        self.letters = letters

    def print_letters(self):
        print(self.letters)

    def count_letters(self):
        letters = self.letters.split(" ")

        return len(letters)


class EnglishAlphabet(Alphabet):
    def __init__(self):
        super().__init__("English", "a b c d e f g h i j k l m n o p q r s t u v w x y z")
        self.__letters_num = 26

    def is_en(self, letter):
        letters = self.letters.split(" ")
        for let in letters:
            if letter.lower() == let:
                return print("It is an English letter!")
        return print("It's not an english letter")

    def count_letters(self):
        print(self.__letters_num)

    @staticmethod
    def example():
        print("Finding somewhere affordable to live in Britain is hard. Some parts of the country are cheaper than"
              " others, of course, but the cost of renting a home is horrendous, especially in London and the South. "
              "Normally, the only answer is to share a house or a flat: you get a room of your own, but you have to "
              "share the kitchen and bathroom. In cities like Oxford and Cambridge, where rooms are scarce, prices "
              "will make your eyes water: more than £500 a month. In London, they’re even higher – not far off £700.")


if __name__ == "__main__":
    eng = EnglishAlphabet()
    print(eng.letters)
    eng.count_letters()
    eng.is_en("F")
    eng.is_en("Щ")
    eng.example()
