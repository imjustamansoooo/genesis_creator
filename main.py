import random
from human import Human, SuperHuman

family = []
heros = []

user_available_options = ['y', 'n']
endgame = False

def create_hero():
    return SuperHuman()


def create_person():
    return Human()


def display_heros():
    print(f"Total Supers: {SuperHuman.population}")
    for idx, hero in enumerate(heros):
        print(f'Super: {idx + 1} \t Super Hero Name: {hero.name} \tPower: {hero.power}')


def display_family():
    print(f'Total Population: {Human.population}')
    for idx, person in enumerate(family):
        print(f'Person: {idx + 1} \tName: {person.name} \tGender: {person.gender}')


while not endgame:
    if Human.population == 0:
        message = 'Do you want to create a human? (Y/N) '
    else:
        message = 'Do you want to create another human? (Y/N) '

    choice = input(message).lower()[:1]
    if choice not in user_available_options:
        print('Please select one of the available options, and try again.\n')

    else:
        if choice == 'y':
            if random.randint(1, 50) % 5 == 0:
                heros.append(create_hero())
                display_heros()
            else:
                family.append(create_person())
                display_family()

            print()
        else:
            print("Thank you for playing 'World Creator'!\n")
            display_family()
            display_heros()
            endgame = True
