# Phantom Assassin, CM, pudge, IO, invoker, lifestealer
# import random

class Ability:
    def __init__(self, spell_name, spell_base_dmg, spell_modifier, spell_dmg_type, mana_cost, cooldown, is_passive, is_dispellable):
        self.spell_name = spell_name
        self.spell_base_dmg = spell_base_dmg[0]
        self.spell_modifier = spell_modifier[0]
        self.spell_dmg_type = spell_dmg_type
        self.spell_level = 0
        self.cooldown = cooldown
        self.mana_cost = mana_cost
        self.is_available = True
        self.is_passive = is_passive
        self.is_dispellable = is_dispellable

    def getSpellDmgType(self):
        return self.spell_dmg_type

    def getSpellName(self):
        return self.spell_name

    def isAvailable(self):
        if self.spell_level and self.is_available:
            return 1
        else:
            print(f"{self.spell_name} is on cooldown.")
            return 0

    def abilityLevelUp(self):
        if self.spell_level >= 4:
            print("Cannot level up spell.")
        self.spell_level += 1
    def execute(self, caster, target):
        if self.isAvailable():
            print(f"{caster.getHeroName()} casts {self.getSpellName()} on {target.getHeroName()}!")


class StiflingDagger(Ability):
    def __init__(self):
        super().__init__("Stifling Dagger", [65, 70, 75, 80], [0.25, 0.4, 0.55, 0.7], "Physical", 30, 6, False, "Yes")

    def execute(self, caster, target):
        super().execute(caster, target)
        target.takeDmg(self.spell_base_dmg + caster.getHeroDmg())


class CoupdeGrace(Ability):
    def __init__(self):
        super().__init__("Coup de Grâce", [0], [2, 3.25, 4.5], "Physical", 0, 0, True, "No")
