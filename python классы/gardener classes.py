class Tomato:
    # Статическое поле класса, которое будет содержать все стадии созревания помидора
    states = {1: "Отсутствие", 2: "Цветение", 3: "Зеленый", 4: "Красный"}

    # Метод инициализации объекта класса
    def __init__(self, index):
        self._index = index
        self._stage = Tomato.states[1]

    # метод, который будет переводить томат на следующую стадию созревания
    def grow(self):
        if self._stage == self.states[1]:
            self._stage = self.states[2]
        elif self._stage == self.states[2]:
            self._stage = self.states[3]
        elif self._stage == self.states[3]:
            self._stage = self.states[4]
        else:
            return
        print(f"Томат теперь на стадии: {self._stage}")

    # метод, который будет проверять, что томат созрел (достиг последней стадии созревания)
    def is_ripe(self):
        if self._stage == self.states[4]:
            return True
        else:
            return False


class TomatoBush:
    def __init__(self, amount_tomatoes):
        self.tomatoes = []
        i = 0
        while i != amount_tomatoes:
            self.tomatoes.append(Tomato(i))
            i += 1

    # метод, который будет переводить все объекты из списка томатов на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # метод, который будет возвращать True, если все томаты из списка стали спелыми
    def all_are_ripe(self):
        zrelost = 0
        for tomato in self.tomatoes:
            if tomato.is_ripe():
                zrelost += 1
        if zrelost == len(self.tomatoes):
            return True

    # метод, который будет чистить список томатов после сбора урожая
    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, tomato_bush):
        self.name = name
        self.tomato_bush = tomato_bush

    # метод, который заставляет садовника работать, что позволяет растению становиться более зрелым
    def work(self):
        self.tomato_bush.grow_all()

    # метод, который проверяет, все ли плоды созрели.
    # Если все - садовник собирает урожай. Если нет - метод печатает предупреждение.
    def harvest(self):
        if self.tomato_bush.all_are_ripe():
            self.tomato_bush.give_away_all()
            print("Томаты собраны!")
        else:
            print("Томаты еще не созрели!")

    @staticmethod
    def knowledge_base():
        print("После высадки в грунт рассаду хорошо поливают и оставляют в покое примерно на неделю. "
              "В дальнейшем томаты поливают раз в 7 дней.")


if __name__ == "__main__":
    Gardener.knowledge_base()  # Вызовите справку по садоводству
    tomato_bush1 = TomatoBush(3)  # Создайте объект класса TomatoBush и Gardener
    alex = Gardener("alex", tomato_bush1)  # Создайте объект класса Gardener
    alex.work()  # Используя объект класса Gardener, поухаживайте за кустом с помидорами
    alex.harvest()  # Попробуйте собрать урожай
    alex.work()  # Если томаты еще не дозрели, продолжайте ухаживать за ними
    alex.work()
    alex.harvest()
    alex.work()
    alex.harvest()  # Соберите урожай
