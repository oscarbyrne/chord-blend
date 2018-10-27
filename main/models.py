from enum import Enum, auto

import pandas as pd


class Key():

    class Color(Enum):
        MAJOR = auto()
        MINOR = auto()

    profiles = {
        Color.MAJOR: pd.Series([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88]),
        Color.MINOR: pd.Series([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17]),
    }

    def __init__(self, tonic, color = Color.MAJOR):
        self.tonic = tonic
        self.color = color

    @property
    def profile(self):
        return self.profiles[self.color]

    def __repr__(self):
        return f'Key({self.tonic}, {self.color})'
