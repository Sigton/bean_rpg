"""
icons.py

This file defines class for various
small icons that appear about the place
"""


class Icon:

    def __init__(self, image, x, y, flash=False, flash_threshold=0):

        self.image = image

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.flash = flash
        self.flash_threshold = flash_threshold
        self.flash_counter = 0

        self.visible = True

    def update(self):

        self.flash_counter += 1

        if self.flash_counter > self.flash_threshold:
            self.flash_counter = 0
            self.visible = False if self.visible else True

    def draw(self, display):

        if self.visible:
            display.blit(self.image, (self.rect.x, self.rect.y))
