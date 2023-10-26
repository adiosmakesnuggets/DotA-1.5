from Hero import *

PA = {'hero_name': "Phantom Assassin", 'category': "agi", 'base_dmg': 32, 'dmg_deviation': 2, 'base_hp': 120,
      'base_mana': 75, 'base_armor': 1, 'strength': 19, 'agility': 21, 'intelligence': 15, 'str_gain': 2.0,
      'agi_gain': 3.2, 'int_gain': 1.4}

CM = {'hero_name': "Crystal Maiden", 'category': "int", 'base_dmg': 30, 'dmg_deviation': 6, 'base_hp': 120,
      'base_mana': 75, 'base_armor': 0, 'strength': 17, 'agility': 16, 'intelligence': 18, 'str_gain': 2.2,
      'agi_gain': 1.6, 'int_gain': 3.3}

Pudge = {'hero_name': "Pudge", 'category': "str", 'base_dmg': 45, 'dmg_deviation': 6, 'base_hp': 120, 'base_mana': 75,
         'base_armor': -1, 'strength': 25, 'agility': 14, 'intelligence': 16, 'str_gain': 3.0, 'agi_gain': 1.4,
         'int_gain': 1.8}

Invoker = {'hero_name': "Invoker", 'category': "uni", 'base_dmg': 16, 'dmg_deviation': 8, 'base_hp': 120,
           'base_mana': 75, 'base_armor': -1, 'strength': 19, 'agility': 14, 'intelligence': 19, 'str_gain': 2.4,
           'agi_gain': 1.8, 'int_gain': 4.0}

IO = {'hero_name': "IO", 'category': "uni", 'base_dmg': 16, 'dmg_deviation': 6, 'base_hp': 120, 'base_mana': 75,
      'base_armor': 1, 'strength': 17, 'agility': 14, 'intelligence': 23, 'str_gain': 2.7, 'agi_gain': 1.6,
      'int_gain': 1.7}

Lifestealer = {'hero_name': "Lifestealer", 'category': "str", 'base_dmg': 25, 'dmg_deviation': 6, 'base_hp': 120,
               'base_mana': 75, 'base_armor': 1, 'strength': 25, 'agility': 19, 'intelligence': 15, 'str_gain': 2.4,
               'agi_gain': 2.6, 'int_gain': 1.8}

hero_data = {
    "phantom_assassin": Hero(**PA),

    "phantom": PA,

    "assassin": PA,

    "crystal_maiden": CM,

    "crystal": CM,

    "maiden": CM,

    "pudge": Pudge,

    "invoker": Invoker,

    "io": IO,

    "wisp": IO,

    "lifestealer": Lifestealer,

}
