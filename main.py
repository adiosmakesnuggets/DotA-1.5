import Player
from hero_data import *
from ability_data import *
from colorama import Fore
radiant_unit_count = 1
dire_unit_count = 1
radiant_units = {}
dire_units = {}


def checkHero(selected_hero, ID):
    if ID.isnumeric():
        edited_ID = int(ID)
        if selected_hero.getTeam() == "radiant":
            if dire_units.get(edited_ID):
                dire_hero = dire_units.get(edited_ID)
                return dire_hero
            else:
                print(f"Couldn't find unit!")
        elif selected_hero.getTeam() == "dire":
            if radiant_units.get(edited_ID):
                radiant_hero = radiant_units.get(edited_ID)
                return radiant_hero
            else:
                print(f"Couldn't find unit!")
    else:
        print(f"Use numbers to select heroes retard!")
        return None


def spawnHero(hero_name, team=None):  # spawnHero creates an object of type Hero using the pre-made hero attributes for each hero found in hero_data.py
    new_hero = Hero(**hero_data.get(hero_name))
    if new_hero:
        global radiant_unit_count, dire_unit_count, radiant_units, dire_units
        new_hero.setTeam(team)
        if team:
            dire_units[dire_unit_count] = new_hero
            dire_unit_count += 1
        else:
            radiant_units[radiant_unit_count] = new_hero
            radiant_unit_count += 1
        ability_data_key = ability_data.get(new_hero.getHeroName())
        new_hero.addAbility(ability_data_key)
        new_hero.displayHeroInfo()
    else:
        print(f"Couldn't find unit by that name ({hero_name})!")
    return new_hero


def printUnits(team=None):  # prints all heroes in both radiant and dire teams, respectively
    global radiant_units, dire_units
    if not team:
        print(f"{Fore.GREEN}Radiant Team:{Fore.RESET}")
        for ID, radiant_hero in radiant_units.items():
            print(f"{ID})\t{radiant_hero.getHeroName()}, Level {radiant_hero.getHeroLevel()}")
    else:
        print(f"{Fore.RED}Dire Team:{Fore.RESET}")
        for ID, dire_hero in dire_units.items():
            print(f"{ID})\t{dire_hero.getHeroName()}, Level {dire_hero.getHeroLevel()}")


if __name__ == "__main__":  # the main game location

    player1 = Player.Player()
    print(f"Welcome, {player1.getPlayerName()}!\nPlease choose a hero by typing the hero name. (No spaces allowed)")
    while True:
        choice = input()
        hero = spawnHero(choice.lower())
        if not hero:
            continue
        else:
            player1.assignHero(hero)
            break
    #   test = player1.getAssignedHero()
    #   print(test.getHeroName())
    #   dire_units[1] = test
    #   some_hero = checkHero(test, 1)
    #   print(some_hero)
    #   test.useAttack(some_hero)
    while True:
        action = input()
        command = action.split()
        player1_hero = player1.getAssignedHero()
        try:
            if command[0] == "hit" and command[1]:
                target_hero = checkHero(player1_hero, command[1])
                if target_hero:
                    player1_hero.useAttack(target_hero)

            elif command[0] == "cast" and command[1]:
                target_hero = checkHero(player1_hero, command[1])
                if target_hero:
                    hero.useAbility(hero.getHeroAbility(int(command[1])), target_hero)

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
                    print(f"{hero.getHeroName()} levelled up! Now level {hero.getHeroLevel()}")
                else:
                    print("Can't take away levels!")

            elif command[0] == "-lvlmax":
                hero.maxLevel()

            elif command[0] == "exit":
                exit()

            else:
                print("Unknown command")

        except IndexError:
            print("No input specified!")
