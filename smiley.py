from vendor.sense_hat import SenseHat


class Smiley:
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (43, 58, 146)
    YELLOW = (255, 255, 0)
    BLANK = (0, 0, 0)

    def __init__(self, complexion=YELLOW):
        self.window_name = f"{self.__class__.__name__} Smiley"
        # We have encapsulated the SenseHat object
        self.sense_hat = SenseHat(window_name=self.window_name)

        self.__complexion = complexion

        X = self.complexion
        O = self.BLANK
        self.pixels = [
            O, X, X, X, X, X, X, O,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            O, X, X, X, X, X, X, O,
        ]

    @property
    def complexion(self):
        return self.__complexion

    def dim_display(self, dimmed=True):
        """
        Set the SenseHat's light intensity to low (True) or high (False)
        :param dimmed: Dim the display if True, otherwise don't dim
        """
        self.sense_hat.low_light = dimmed

    def show(self):
        """
        Show the smiley on the screen.
        """
        self.sense_hat.set_pixels(self.pixels)
