import random

HP_PER_STR = 22
MANA_PER_INT = 12
ARMOR_PER_AGI = 1 / 6
MAGIC_RESIST_BASE = 0.25
PHYS_RESIST_MULTIPLIER = 0.06
MAGIC_RESIST_PER_INT = 0.001


class Hero:
    def __init__(self, hero_name, category, base_dmg, dmg_deviation, base_hp, base_mana, base_armor, strength, agility,
                 intelligence, str_gain, agi_gain, int_gain):
        self.hero_name = hero_name
        self.category = category
        self.level = 1
        self.base_dmg = base_dmg
        self.dmg_deviation = dmg_deviation
        self.base_hp = base_hp
        self.hp = strength * HP_PER_STR + base_hp
        self.base_mana = base_mana
        self.mana = intelligence * MANA_PER_INT + base_mana
        self.base_armor = base_armor
        self.armor = agility * ARMOR_PER_AGI + base_armor
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.str_gain = str_gain
        self.agi_gain = agi_gain
        self.int_gain = int_gain
        self.evasion = 0
        self.physical_resist = self.calculatePhysicalResist()
        self.magical_resist = self.calculateMagicalResist()
        self.dmg = self.calculateDmg()
        self.team = 0
        self.aghanims_scepter = False
        self.aghanims_shard = False
        self.mastery_points = 0
        self.abilities = []
        self.dead = False

    def getHeroName(self):
        return self.hero_name

    def getHeroDmg(self):
        return self.dmg + random.randint(0, self.dmg_deviation)

    def getMasteryPoints(self):
        return self.mastery_points
    def calculateDmg(self):
        if self.category.lower() == "str" or self.category.lower() == "strength":
            self.dmg = self.base_dmg + self.strength
            return self.dmg

        elif self.category.lower() == "agi" or self.category.lower() == "agility":
            self.dmg = self.base_dmg + self.agility
            return self.dmg

        elif self.category.lower() == "int" or self.category.lower() == "intelligence":
            self.dmg = self.base_dmg + self.intelligence
            return self.dmg

        elif self.category.lower() == "uni" or self.category.lower() == "universal":
            self.dmg = self.base_dmg + (self.strength + self.agility + self.intelligence) * 0.7
            return self.dmg

    def takeDmg(self, damage):
        if (self.hp - damage) <= 0:
            self.hp = 0
            self.dead = True
            print(f"{self.getHeroName()} is dead!")
        else:
            self.hp -= damage

    def calculatePhysicalResist(self):
        self.physical_resist = 1 - (
                    PHYS_RESIST_MULTIPLIER * self.armor / (1 + PHYS_RESIST_MULTIPLIER * abs(self.armor)))
        return self.physical_resist

    def calculateMagicalResist(self):
        self.magical_resist = (1 - (MAGIC_RESIST_BASE + self.intelligence * MAGIC_RESIST_PER_INT))
        return self.magical_resist

    def isEnemy(self, target):
        return self.team != target.team

    def isAlly(self, target):
        return self.team == target.team

    def useAttack(self, target):
        target.takeDmg(self.getHeroDmg()*target.calculatePhysicalResist())

    def levelUpAbility(self, ability):
        self.mastery_points -= 1
        ability.abilityLevelUp()

    def useAbility(self, ability, target):
        ability.execute(self, target)

    def addAbility(self, ability):
        self.abilities.append(ability)

    def heroLevelUp(self):
        if self.level >= 30:
            print("Hero is now at max level!")
            return
        self.level += 1
        self.mastery_points += 1
        self.strength += self.str_gain
        self.agility += self.agi_gain
        self.intelligence += self.int_gain
        self.hp += self.str_gain * HP_PER_STR
        self.mana += self.int_gain * MANA_PER_INT
        self.armor += self.agi_gain * ARMOR_PER_AGI
        self.dmg = self.calculateDmg()
        self.physical_resist = self.calculatePhysicalResist()
        self.magical_resist = self.calculateMagicalResist()

    def maxLevel(self):
        if self.level >= 30:
            print("Hero is already at max level!")
            return
        lvlsRemaining = 30 - self.level
        for i in range(0, lvlsRemaining):
            self.heroLevelUp()

    def displayHeroInfo(self):
        print(f"{self.hero_name}")
        print(f"Category: {self.category}")
        print(f"Level: {self.level}")
        print(f"Damage: {self.dmg:.2f}")
        print(f"HP: {self.hp:.0f}")
        print(f"Mana: {self.mana:.0f}")
        print(f"Armor: {self.armor:.1f}")
        print(f"Strength: {self.strength:.1f}")
        print(f"Agility: {self.agility:.1f}")
        print(f"Intelligence: {self.intelligence:.1f}")
        print(f"Magical Resist: {1 - self.magical_resist:.2f}")
