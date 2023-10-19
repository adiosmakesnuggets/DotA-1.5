import random
# from colorama import Fore, Back, Style

HP_PER_STR = 22
HP_REGEN_PER_STR = 0.1
MANA_PER_INT = 12
MANA_REGEN_PER_INT = 0.05
ARMOR_PER_AGI = 1 / 6
MAGIC_RESIST_BASE = 0.25
PHYS_RESIST_MULTIPLIER = 0.06
MAGIC_RESIST_PER_INT = 0.001


class Hero:
    def __init__(self, hero_name, code_names, category, base_dmg, dmg_deviation, base_hp, base_mana, base_armor, strength, agility,
                 intelligence, str_gain, agi_gain, int_gain):
        self.hero_name = hero_name
        self.code_names = []
        for i in code_names:
            self.code_names.append(i)
        self.category = category
        self.level = 1
        self.base_dmg = base_dmg
        self.dmg_deviation = dmg_deviation
        self.base_hp = base_hp
        self.max_hp = strength * HP_PER_STR + base_hp
        self.hp = self.max_hp
        self.hp_regen = strength * HP_REGEN_PER_STR
        self.base_mana = base_mana
        self.max_mana = intelligence * MANA_PER_INT + base_mana
        self.mana = self.max_mana
        self.mana_regen = intelligence * 0.05
        self.base_armor = base_armor
        self.armor = agility * ARMOR_PER_AGI + base_armor
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.str_gain = str_gain
        self.agi_gain = agi_gain
        self.int_gain = int_gain
        self.evasion = 0
        self.crit_chance = 0
        self.physical_resist = self.calculatePhysicalResist()
        self.magical_resist = self.calculateMagicalResist()
        self.dmg = self.calculateDmg()
        self.team = 0
        self.aghanims_scepter = False
        self.aghanims_shard = False
        self.mastery_points = 1
        self.abilities = []
        self.hero_modifiers = []
        self.dead = False

    def __del__(self):
        print(f"{self.getHeroName()} removed.")

    def getHeroName(self):
        return self.hero_name

    def getCodeNames(self):
        return self.code_names

    def isDead(self):
        return self.dead

    def getHeroDmg(self):
        return self.dmg + random.randint(0, self.dmg_deviation)

    def getPhysicalResist(self):
        return self.physical_resist

    def getHeroHP(self):
        return self.hp

    def getHeroMaxHP(self):
        return self.max_hp

    def getHeroMana(self):
        return self.mana

    def getHeroMaxMana(self):
        return self.max_hp

    def getHeroLevel(self):
        return self.level

    def getHeroAbility(self, index):
        return self.abilities[index]

    def getMasteryPoints(self):
        return self.mastery_points

    def setHeroMana(self, value):
        if (self.mana - value) < 0:
            self.mana = 0
        else:
            self.mana -= value

    def setTeam(self, team):
        self.team = team

    def killHero(self):
        self.dead = True

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
        if self.isDead():
            print(f"{self.getHeroName()} is already dead, man!")
        elif (self.hp - damage) <= 0:
            self.hp = 0
            self.killHero()
            print(f"Hero {self.getHeroName()} is now at {self.getHeroHP():.0f} HP!")
            print(f"{self.getHeroName()} is slain!")
        else:
            self.hp -= damage
            print(f"Hero {self.getHeroName()} is now at {self.getHeroHP():.0f} HP!")

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
        target.takeDmg(self.getHeroDmg() * target.getPhysicalResist())

    def levelUpAbility(self, ability):
        self.mastery_points -= 1
        ability.abilityLevelUp()

    def useAbility(self, ability, target):
        ability.execute(self, target)

    def addAbility(self, ability):
        self.abilities.append(ability)

    def heroLevelUp(self):
        print(f"{self.getHeroName()} levelled up!")
        if self.level >= 30:
            return 0
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
        print(f"{self.hero_name}\t Level {self.getHeroLevel()}")
        print(f"Strength: {self.strength:.1f}")
        print(f"Agility: {self.agility:.1f}")
        print(f"Intelligence: {self.intelligence:.1f}")
        print(f"Damage: {self.dmg:.2f}")
        print(f"HP: {self.hp:.0f}")
        print(f"Mana: {self.mana:.0f}")
        print(f"Armor: {self.armor:.1f}")
        print(f"Magical Resist: {1 - self.magical_resist:.2f}\n")
