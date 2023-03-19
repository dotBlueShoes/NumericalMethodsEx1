from typing import List

from trigonometric import trigonometric
from exponensial import exponensial
from polynomial import polynomial

text_select_upper_function: str = "Wybierz funkcję nadrzędną (1.Wielomian, 2.Trygonometryczna, 3.Wykładnicza): "
text_select_lower_function: str = "Wybierz funkcję (1.Wielomian, 2.Trygonometryczna, 3.Wykładnicza, 4.Złożona): "

class combination:
    def __init__(self,function1_type:int,function2_type:int):
        lista: List[int] = [1, 1]
        function1_type =function1_type
        match function1_type:
            case 1:
                print("Wybrano funckje typu wielomian.")
                self.function1 = polynomial(lista)
            case 2:
                print("Wybrano funckje typu trygonometryczna.")
                self.function1 = trigonometric(1)
            case 3:
                print("Wybrano funckje typu wykładnicza.")
                self.function1 = exponensial(1)
            case other:
                return

        function2_type = function2_type
        match function2_type:
            case 1:
                print("Wybrano funckje typu wielomian.")
                self.function2 = polynomial(lista)
            case 2:
                print("Wybrano funckje typu trygonometryczna.")
                self.function2 = trigonometric(1)
            case 3:
                print("Wybrano funckje typu wykładnicza.")
                self.function2 = exponensial(1)
            case 4:
                print("Wybrano funckje typu złożona.")
                self.function2 = combination(2,2)
            case other:
                return
    def input(self):
        lista: List[int] = [1, 1]
        self.function1_type = int(input(text_select_upper_function))
        match self.function1_type:
            case 1:
                print("Wybrano funckje typu wielomian.")
                self.function1 = polynomial(lista)
            case 2:
                print("Wybrano funckje typu trygonometryczna.")
                self.function1 = trigonometric(1)
            case 3:
                print("Wybrano funckje typu wykładnicza.")
                self.function1 = exponensial(1)
            case other:
                return
        self.function2_type = int(input(text_select_lower_function))
        match self.function2_type:
            case 1:
                print("Wybrano funckje typu wielomian.")
                self.function2 = polynomial(lista)
            case 2:
                print("Wybrano funckje typu trygonometryczna.")
                self.function2 = trigonometric(1)
            case 3:
                print("Wybrano funckje typu wykładnicza.")
                self.function2 = exponensial(1)
            case 4:
                print("Wybrano funckje typu złożona.")
                self.function2 = combination(2, 2)
            case other:
                return
        self.function1.input()
        self.function2.input()

    def value(self,x) -> float:
        return self.function1.value(self.function2.value(x))