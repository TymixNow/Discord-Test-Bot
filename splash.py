import random


class Splash:
    def __init__(self, spl : list[str]):
        self.spl = spl
    def __call__(self, name : str):
        return random.choice(self.spl) % name