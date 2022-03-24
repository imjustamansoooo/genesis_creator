import rawdata
import random

class Human:
    population = 0

    def __init__(self):
        self.gender = random.choice(list(rawdata.name.keys()))
        self.name = random.choice(rawdata.name[self.gender])
        Human.population += 1


class SuperHuman(Human):
    population = 0
    def __init__(self):
        super().__init__()
        self.name = random.choice(list(rawdata.powers.keys()))
        self.power = random.choice(rawdata.powers[self.name])
        SuperHuman.population += 1
