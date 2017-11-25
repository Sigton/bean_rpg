"""
tile_types.py

This defines how the player
interacts with the tiles in
the game.
"""

solid_tiles = [
    "0017",
    "0018",
    "0019",
    "0020",
    "0021",
    "0022",
    "0023",
    "0024",
    "0025",
    "0026",
    "0027",
    "0028",
    "0029",
    "0030"
]

animated_tiles = [
    "0030"
]

shadowed_decs = [
    "0031",
    "0040"
]

shadow_height_ratios = {
    "duel_player": 0.8,
    "duel_enemy": 0.8,
    "0031": 0.85,
    "0040": 0.6
}

shadow_width_ratios = {
    "duel_player": 0.2,
    "duel_enemy": 0.2
}

shadow_width_to_parent_ratios = {
    "duel_player": 1.2,
    "duel_enemy": 1.2
}

shadow_x_offset = {
    "duel_player": -35,
    "duel_enemy": -10
}