import pygame

from src.etc import spritesheet

"""
bean_image_loader.py

This file loads all 
the bean images
"""

sprite_sheet = None
grey_sprite_sheet = None

chili = (0, 0, 40, 40)
cool = (40, 0, 40, 40)
pickle = (80, 0, 40, 40)
strawberry = (120, 0, 40, 40)
lemon = (160, 0, 40, 40)
rainbow = (200, 0, 40, 40)
unicorn = (240, 0, 40, 40)
hedgehog = (280, 0, 40, 40)
poison = (320, 0, 40, 40)
carrot = (0, 40, 42, 46)
rabbit = (360, 0, 40, 40)
what = (42, 40, 40, 40)
chicken = (82, 40, 40, 40)
wizard = (122, 40, 44, 48)

beans = {}


def load_sprite_sheet():

    global sprite_sheet, grey_sprite_sheet, beans
    sprite_sheet = spritesheet.SpriteSheet("src/resources/beans.png")
    grey_sprite_sheet = spritesheet.SpriteSheet("src/resources/grey_beans.png")

    beans = {
        "chili": create_images(chili),
        "cool": create_images(cool),
        "pickle": create_images(pickle),
        "strawberry": create_images(strawberry),
        "lemon": create_images(lemon),
        "rainbow": create_images(rainbow),
        "unicorn": create_images(unicorn),
        "hedgehog": create_images(hedgehog),
        "poison": create_images(poison),
        "carrot": create_images(carrot),
        "rabbit": create_images(rabbit),
        "what": create_images(what),
        "chicken": create_images(chicken),
        "wizard": create_images(wizard)
    }


def create_images(image):

    images = dict()

    images["R"] = sprite_sheet.get_image(image[0],
                                         image[1],
                                         image[2],
                                         image[3])
    images["L"] = pygame.transform.flip(images["R"], True, False)

    images["GR"] = grey_sprite_sheet.get_image(image[0],
                                               image[1],
                                               image[2],
                                               image[3])
    images["GL"] = pygame.transform.flip(images["GR"], True, False)

    return images
