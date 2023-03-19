from numpy import float_power
from typing import List
from helpers import powii, powfi, powff

class exponensial:
    exponensial_values: List[int]
    def __init__(self, exponensial_values:  List[int]):
        self.exponensial_values = exponensial_values

    def input(self):
        print("Funkcja wykładnicza ma postać f(x)=a^x+b")
        self.exponensial_values[0] = float(input("Podaj wartość a: "))
        self.exponensial_values[1] = float(input("Podaj wartość b: "))

    def value(self, x) -> float:

        if isinstance(self.exponensial_values[0], int):
            if isinstance(x, int):
                return powii(self.exponensial_values[0], x) + self.exponensial_values[1]
            else:
                return powff(self.exponensial_values[0], x) + self.exponensial_values[1]
        else:
            if isinstance(x, float):
                return powff(self.exponensial_values[0], x) + self.exponensial_values[1]
            else:
                return powfi(self.exponensial_values[0], x) + self.exponensial_values[1]
        