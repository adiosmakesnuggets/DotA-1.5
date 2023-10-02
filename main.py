import Hero
import Player
# import Ability

heroes = []


def spawnHero(hero_name):
    from hero_data import hero_data
    if hero_name in hero_data:
        hero_attributes = hero_data[hero_name]
        new_hero = Hero.Hero(**hero_attributes)
        heroes.append(new_hero)
        print(f"{new_hero.getHeroName()} has been spawned!\n")
        new_hero.displayHeroInfo()
        return new_hero
    elif not hero_name:
        print("No unit specified")
        return None
    else:
        print(f"Couldn't find unit by that name ({hero_name})!")
        return None


if __name__ == "__main__":

    player1 = Player.Player()
    choice = input(f"Welcome, {player1.getPlayerName()}!\nPlease choose a hero by typing the hero name. (No spaces allowed)\n")
    player1.assignHero(spawnHero(choice.lower()))
    while True:
        action = input()
        action_split = action.split()
        try:
            if action_split[0] == "-createhero":
                if action_split[1]:
                    hero = spawnHero(action_split[1])
            else:
                print("Unknown command")
        except:
            print("No command specified")

        #elif action_split[0] == "lvlmax":

