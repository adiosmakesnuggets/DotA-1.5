# Phantom Assassin, CM, pudge, IO, invoker, lifestealer
# import random

class Ability:
    def __init__(self, ability_name, ability_max_level, ability_base_dmg, ability_modifier, ability_dmg_type, mana_cost, max_cooldown, is_passive, is_dispellable):
        self.ability_name = ability_name
        self.ability_max_level = ability_max_level

        self.ability_base_dmg = []
        for i in ability_base_dmg:
            self.ability_base_dmg.append(i)

        self.ability_modifier = []
        for i in ability_modifier:
            self.ability_modifier.append(i)

        self.ability_dmg_type = ability_dmg_type
        self.ability_level = -1
        self.xp = 0
        self.max_cooldown = max_cooldown
        self.cooldown = 0

        self.mana_cost = []
        for i in mana_cost:
            self.mana_cost.append(i)

        self.is_available = True
        self.is_passive = is_passive
        self.is_dispellable = is_dispellable

    def getAbilityManaCost(self):
        try:
            return self.mana_cost[self.getAbilityLevel()]
        except IndexError:
            return self.mana_cost[self.getAbilityMaxLevel()]

    def getAbilityMaxLevel(self):
        return self.ability_max_level

    def getAbilityDmgType(self):
        return self.ability_dmg_type

    def getAbilityLevel(self):
        return self.ability_level

    def getAbilityName(self):
        return self.ability_name


    def isAvailable(self):
        if self.getAbilityLevel() == -1:
            print("Ability not learned.")
            return 0
        elif not self.is_available:
            print(f"{self.ability_name} is on cooldown!")
            return 0
        else:
            return 1

    def abilityLevelUp(self):
        if self.getAbilityLevel() >= self.getAbilityMaxLevel():
            print("Cannot level up ability.")
            return
        self.ability_level += 1

    def execute(self, caster, target):
        if self.getAbilityLevel() == -1:
            print("Ability not learned!")
            return 0
        if self.isAvailable():
            print(f"{caster.getHeroName()} casts {self.getAbilityName()} on {target.getHeroName()}!")
            caster.setHeroMana(self.getAbilityManaCost())
            print(f"{caster.getHeroName()} is now {caster.getHeroMana()}")


class StiflingDagger(Ability):
    def __init__(self):
        super().__init__("Stifling Dagger", 4, [65, 70, 75, 80], [0.25, 0.4, 0.55, 0.7], "Physical", [30], 6, False, "Yes")

    def execute(self, caster, target):
        if super().execute(caster, target):
            target.takeDmg(self.ability_base_dmg[self.getAbilityLevel()] + self.ability_modifier[self.getAbilityLevel()] * caster.getHeroDmg())
        else:
            pass

# class CoupdeGrace(Ability):
    # def __init__(self):
        # super().__init__("Coup de Grâce", 3, [0], [2, 3.25, 4.5], "Physical", 0, 0, True, "No")
