"""
entity_meta.py

This file holds information about
all of the different beans, eg
their max hp, moves, starting damage.
"""

entity_data = {
    "chili": {"max_hp": 100, "moves": [1, 0], "attack": 10, "energy": 100, "display_name": "Chili Bean"},
    "cool": {"max_hp": 100, "moves": [0, 2], "attack": 10, "energy": 100, "display_name": "Cool Bean"},
    "pickle": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Pickle Bean"},
    "strawberry": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Strawberry Bean"},
    "lemon": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Lemon Bean"},
    "rainbow": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Rainbow Bean"},
    "unicorn": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Unicorn Bean"},
    "hedgehog": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Hedgehog Bean"},
    "poison": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Poison Bean"},
    "carrot": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Carrot Bean"},
    "rabbit": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Rabbit Bean"},
    "what": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "What Beam"},
    "chicken": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Chicken Bean"},
    "wizard": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Wizard Bean"},
    "old_villager": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Old Bean"},
    "tim": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Tim"}
}

item_effects = {
    "EnlightenmentPotion": "",
    "HealthPotion": "self.player.meta.heal(40)"
}
