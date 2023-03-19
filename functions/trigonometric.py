import math

text_select_trygonomic_function: str = "Wybierz funkcję trygonometryczną (1.Sinus, 2.Cosinus, 3.Tanges 4.Cotanges): "

class trigonometric:
    function_type:int = 0
    def __init__(self, type):
        self.function_type:int=type

    def input(self):
        while self.function_type < 1 or self.function_type > 4:
            self.function_type = int(input(text_select_trygonomic_function))

    def value(self,x) -> float:
        match self.function_type:
            case 1:
                return math.sin(x)
            case 2:
                return math.cos(x)
            case 3:
                return math.tan(x)
            case 4:
                return math.cos(x)/math.sin(x)