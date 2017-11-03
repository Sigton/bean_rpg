from src.etc import spritesheet

"""
bean_image_loader.py

This file loads all 
the bean images
"""

sprite_sheet = None

red = lambda: sprite_sheet.get_image(0, 0, 60, 60)
blue = lambda: sprite_sheet.get_image(60, 0, 60, 60)
green = lambda: sprite_sheet.get_image(100, 0, 60, 60)
pink = lambda: sprite_sheet.get_image(140, 0, 60, 60)
yellow = lambda: sprite_sheet.get_image(180, 0, 60, 60)


def load_sprite_sheet():

    global sprite_sheet
    sprite_sheet = spritesheet.SpriteSheet("src/resources/beans.png")
