import rawdata
import random

class Human:
    population = 0

    def __init__(self):
        self.gender = random.choice(rawdata.gender)
        self.name = random.choice(rawdata.name[self.gender])
        Human.population += 1


class SuperHuman(Human):
    population = 0
    super.__init__()
    def __init__(self):
        pass
