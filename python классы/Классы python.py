class Human:
    # Статические поля
    default_name = "None"
    default_age = 18

    def __init__(self, name=default_name, age=default_age):
        # Динамические поля
        # Публичные свойства
        self.name = name
        self.age = age

        # Приватные свойства
        self.__money = 0
        self.__house = None

    def info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("House: ", self.__house)
        print("Money: ", self.__money)

    @staticmethod
    def default_info():
        print(f"Default name: {Human.default_name}")
        print(f"Default age: {Human.default_age}")

    def __make_deal(self, house, house_price):
        self.__house = house
        self.__money -= house_price

    def earn_money(self, amount_money):
        self.__money += amount_money

    def buy_house(self, house, discount):
        price = house.final_price(discount)

        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print("You don't have enough money")


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100

        return final_price


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(40, price)


if __name__ == "__main__":
    # Тесты
    Human.default_info()  # Вызовите справочный метод default_info() для класса Human
    alex = Human("Alex", 17)  # Создайте объект класса Human
    alex.info()  # Выведите справочную информацию о созданном объекте (вызовите метод info()).
    little_house = SmallHouse(1500000)  # Создайте объект класса SmallHouse
    alex.buy_house(little_house, 0)  # Попробуйте купить созданный дом, убедитесь в получении предупреждения.
    alex.earn_money(1500000)  # Поправьте финансовое положение объекта - вызовите метод earn_money()
    alex.buy_house(little_house, 0)  # Снова попробуйте купить дом
    alex.info()  # Посмотрите, как изменилось состояние объекта класса Human
