import Hero
import Player
from hero_data import *
# import Ability
radiant_unit_count = 1
dire_unit_count = 1
radiant_units = {}
dire_units = {}


def spawnHero(hero_name, team=None):  # spawnHero creates an object of type Hero using the pre-made hero attributes for each hero found in hero_data.py
    if not hero_name:
        print("No unit specified!")

    for hero, attributes in hero_data.items():
        if hero_name in attributes['code_names']:
            new_hero = Hero.Hero(**attributes)
            ability_data_key = attributes.get('code_names')[0]
            from ability_data import ability_data
            new_hero.addAbility(ability_data.get(ability_data_key))  # this is a clusterfuck. I will redo this later
            global radiant_unit_count, dire_unit_count, radiant_units, dire_units
            new_hero.setTeam(team)

            if not team:
                radiant_units[radiant_unit_count] = new_hero
                radiant_unit_count += 1
            elif team:
                dire_units[dire_unit_count] = new_hero
                dire_unit_count += 1
            new_hero.displayHeroInfo()

            return new_hero

    print(f"Couldn't find unit by that name ({hero_name})!")


def printUnits(team=None):
    global radiant_units, dire_units
    if not team:
        print("Radiant team:")
        for ID, hero in radiant_units.items():
            print(f"{ID})\t{hero.getHeroName()}, Level {hero.getHeroLevel()}")
    else:
        print("Dire team:")
        for ID, hero in dire_units.items():
            print(f"{ID})\t{hero.getHeroName()}, Level {hero.getHeroLevel()}")


if __name__ == "__main__":

    player1 = Player.Player()
    print(f"Welcome, {player1.getPlayerName()}!\nPlease choose a hero by typing the hero name. (No spaces allowed)")
    while True:
        choice = input()
        hero = spawnHero(choice.lower())
        if not hero:
            continue
        else:
            player1.assignHero(hero)
            player1_hero = player1.getAssignedHero()
            break
    print(f"{hero.getHeroAbility(0)}")
    while True:
        action = input()
        command = action.split()
        hero = player1.getAssignedHero()
        try:
            if command[0] == "hit" and command[1]:
                flag = 0
                for hero_name, hero_object in dire_units.items():
                    if command[1].lower() in hero_object.getCodeNames():
                        hero.useAttack(hero_object)
                        flag = 1
                        break
                if not flag:
                    print(f"Couldn't find unit by that name ({command[1]})!")

            elif command[0] == "cast" and command[1]:
                flag = 0
                for hero_name, hero_object in dire_units.items():
                    if command[2].lower() in hero_object.getCodeNames():
                        hero.useAbility(hero.getHeroAbility(int(command[1])), hero_object)
                        flag = 1
                        break
                if not flag:
                    print(f"Couldn't find unit by that name ({command[1]})!")

            elif command[0] == "-createhero":
                if command[1]:
                    try:
                        if command[2] == 'enemy' or command[2] == '1':
                            spawnHero(command[1].lower(), command[2])
                            printUnits(command[2])
                        else:
                            spawnHero(command[1].lower())
                            printUnits()
                    except IndexError:
                        spawnHero(command[1].lower())
                        printUnits()

            elif command[0] == "-lvlup" or command[0] == "-levelup":
                if int(command[1]) >= 0:
                    for i in range(0, int(command[1])):
                        hero.heroLevelUp()
                else:
                    print("Can't take away levels!")

            elif command[0] == ""

            else:
                print("Unknown command")

        except IndexError:
            print("No unit specified!")
