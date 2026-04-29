from smiley import Smiley
from blinkable import Blinkable
import time

class Angry(Smiley, Blinkable):
    def __init__(self):
        super().__init__(complexion=Smiley.RED)

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Draws the mouth feature on a smiley
        """
        mouth = [41,34,27,28,37,46]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        eyes = [9, 14]
        for pixel in eyes:
            if wide_open:
                eyes = self.BLANK
            else:
                eyes = self.complexion
            self.pixels[pixel] = eyes

    def blink(self):
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(0.5)
        self.draw_eyes(wide_open=True)
        self.show()