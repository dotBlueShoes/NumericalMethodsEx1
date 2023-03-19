from typing import List

class polynomial:
    polynomial_values: List[int]
    def __init__(self, polynomial_values):
        self.polynomial_values=polynomial_values

    def input(self) -> List[int]:
        input_number = int(input("Wprowadz stopien wielomianu: ")) + 1
        self.polynomial_values = [0] * input_number
        for i in range(input_number - 1, 0 - 1, -1):
            print("Wprowadz wartosc " + str(i) + " skladnika wielomianu: ")
            self.polynomial_values[input_number - 1 - i] = int(input())


    def value(self, x_value) -> float:
        sum:float = 0
        last_elem: int = len(self.polynomial_values) - 1

        for i in range(0,last_elem):
            sum = (sum + self.polynomial_values[i]) * x_value
        sum += self.polynomial_values[last_elem]
        return sum