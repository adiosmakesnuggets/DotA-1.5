import Hero


class Player:
    def __init__(self):
        self.name = "Nader"
        self.assigned_hero = None

    def assignHero(self, hero):
        self.assigned_hero = hero

    def getPlayerName(self):
        return self.name

    def getAssignedHero(self):
        return self.assigned_hero
