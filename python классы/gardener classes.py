class Tomato:
    states = {1: "Отсутствие", 2: "Цветение", 3: "Зеленый", 4: "Красный"}

    def __init__(self, index):
        self._index = index
        self._stage = Tomato.states[1]

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

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        zrelost = 0
        for tomato in self.tomatoes:
            if tomato.is_ripe():
                zrelost += 1
        if zrelost == len(self.tomatoes):
            return True

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, tomato_bush):
        self.name = name
        self.tomato_bush = tomato_bush

    def work(self):
        self.tomato_bush.grow_all()

    def harvest(self):
        if self.tomato_bush.all_are_ripe():
            self.tomato_bush.give_away_all()
            print("Томаты собраны!")
        else:
            print("Томаты еще не созрели!")


if __name__ == "__main__":
    tomato_bush1 = TomatoBush(3)
    alex = Gardener("alex", tomato_bush1)

    alex.work()
    alex.harvest()
    alex.work()
    alex.work()
    alex.harvest()
    alex.work()
    alex.harvest()
