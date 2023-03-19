import matplotlib.pyplot as plt
import math
import numpy
import statistics as st
from typing import List

import bisection_method
import newtons_method

"""class Kwiat:
    sepal_length = float
    sepal_width = float
    petal_length = float
    petal_width = float

    def print_stat(self):
        print(f"{self.sepal_length}; {self.sepal_width}; {self.petal_length}; {self.petal_width}")


def tab1(nazwa: str, liczba: int, cala_liczba: int):
    procent = round(liczba / cala_liczba * 100, 1)
    print(f"{nazwa}: liczebność: {liczba}({procent}%)")


def tab2(lista1, lista2, lista3, liczebnosc):
    sepal_length = []
    sepal_width = []
    petal_length = []
    petal_width = []
    for kwiat in lista1:
        sepal_length.append(kwiat.sepal_length)
        sepal_width.append(kwiat.sepal_width)
        petal_length.append(kwiat.petal_length)
        petal_width.append(kwiat.petal_width)
    for kwiat in lista2:
        sepal_length.append(kwiat.sepal_length)
        sepal_width.append(kwiat.sepal_width)
        petal_length.append(kwiat.petal_length)
        petal_width.append(kwiat.petal_width)
    for kwiat in lista3:
        sepal_length.append(kwiat.sepal_length)
        sepal_width.append(kwiat.sepal_width)
        petal_length.append(kwiat.petal_length)
        petal_width.append(kwiat.petal_width)

    wyswietl("Długość działki kielicha (cm)", sepal_length, liczebnosc)
    wyswietl("Szerokość działki kielicha (cm)", sepal_width, liczebnosc)
    wyswietl("Długość płatka (cm)", petal_length, liczebnosc)
    wyswietl("Szerokość płatka (cm)", petal_width, liczebnosc)


def wyswietl(nazwa, tab, licz):
    print(
        f"{nazwa}: Minimum:{min(tab)} średnia:{srednia(tab, licz)} (±{odchylenie(tab, licz)}) Mediana:{round(st.median(tab), 2)} ({kwartyl_dolny(tab, licz)}-{kwartyl_gorny(tab, licz)}) Maksimum:{max(tab)}")


def srednia(tablica, liczebnosc):
    return round(sum(tablica) / liczebnosc, 2)


def odchylenie(tablica, liczebnosc):
    suma = 0
    for wartosc in tablica:
        suma = suma + (wartosc - srednia(tablica, liczebnosc)) ** 2
    return round(numpy.sqrt(suma / liczebnosc), 2)


def kwartyl_dolny(tablica, liczenosc):
    tablica.sort()
    return tablica[int((liczenosc - 1) / 4)]


def kwartyl_gorny(tablica, liczenosc):
    tablica.sort()
    return tablica[int(((liczenosc - 1) * 3) / 4)]


def wykresy(lista1, lista2, lista3):
    sepal_length = []
    sepal_width = []
    petal_length = []
    petal_width = []
    for kwiat in lista1:
        sepal_length.append(kwiat.sepal_length)
        sepal_width.append(kwiat.sepal_width)
        petal_length.append(kwiat.petal_length)
        petal_width.append(kwiat.petal_width)
    for kwiat in lista2:
        sepal_length.append(kwiat.sepal_length)
        sepal_width.append(kwiat.sepal_width)
        petal_length.append(kwiat.petal_length)
        petal_width.append(kwiat.petal_width)
    for kwiat in lista3:
        sepal_length.append(kwiat.sepal_length)
        sepal_width.append(kwiat.sepal_width)
        petal_length.append(kwiat.petal_length)
        petal_width.append(kwiat.petal_width)
    histogram("Długość działki kielicha", sepal_length)
    histogram("Szerokość działki kielicha", sepal_width)
    histogram("Długość płatka", petal_length)
    histogram("Szerokość płatka", petal_width)


def histogram(nazwa, tab):
    nniz = 0
    if (min(tab) < int(min(tab)) + 0.5):
        nniz = int(min(tab))
    else:
        nniz = int(min(tab)) + 0.5
    nmaks = 0
    if (max(tab) < int(max(tab)) + 0.5):
        nmaks = int(max(tab)) + 1
    else:
        nmaks = int(max(tab)) + 1.5

    bins = numpy.arange(nniz, nmaks, 0.5)
    plt.hist(tab, bins=bins, edgecolor='black')
    plt.title(nazwa)
    plt.ylabel("Liczebność")
    plt.xlabel("Długość (cm)")
    plt.show()


def wyk_pudelkowy(lista1, lista2, lista3):
    sepal_length_s = []
    sepal_length_ve = []
    sepal_length_vi = []

    sepal_width_s = []
    sepal_width_ve = []
    sepal_width_vi = []

    petal_length_s = []
    petal_length_ve = []
    petal_length_vi = []

    petal_width_s = []
    petal_width_ve = []
    petal_width_vi = []
    for kwiat in lista1:
        sepal_length_s.append(kwiat.sepal_length)
        sepal_width_s.append(kwiat.sepal_width)
        petal_length_s.append(kwiat.petal_length)
        petal_width_s.append(kwiat.petal_width)
    for kwiat in lista2:
        sepal_length_ve.append(kwiat.sepal_length)
        sepal_width_ve.append(kwiat.sepal_width)
        petal_length_ve.append(kwiat.petal_length)
        petal_width_ve.append(kwiat.petal_width)
    for kwiat in lista3:
        sepal_length_vi.append(kwiat.sepal_length)
        sepal_width_vi.append(kwiat.sepal_width)
        petal_length_vi.append(kwiat.petal_length)
        petal_width_vi.append(kwiat.petal_width)
    plt.boxplot([sepal_length_s, sepal_length_ve, sepal_length_vi], labels=['setosa', 'versicolor', 'virginica'])
    plt.ylabel('Długość (cm)')
    plt.show()
    plt.boxplot([sepal_width_s, sepal_width_ve, sepal_width_vi], labels=['setosa', 'versicolor', 'virginica'])
    plt.ylabel('Szerokość (cm)')
    plt.show()
    plt.boxplot([petal_length_s, petal_length_ve, petal_length_vi], labels=['setosa', 'versicolor', 'virginica'])
    plt.ylabel('Długość (cm)')
    plt.show()
    plt.boxplot([petal_width_s, petal_width_ve, petal_width_vi], labels=['setosa', 'versicolor', 'virginica'])
    plt.ylabel('Szerokość (cm)')
    plt.show()"""


def exponential_fuction():
    print("Funkcja wykładnicza ma postać f(x)=a*e^(bx)")
    a = input("Podaj wartość a:")
    b = input("Podaj wartość b:")


def value_exponential_fuction(a, b, x):
    e = numpy.e
    return a * (e ** (b * x))


def mabs(x):
    if x < 0:
        return x*(-1)
    else:
        return x


def factorial(x):
    value = 1
    for i in x:
        value = value * i
    return value

# Celem zadania pierwszego jest zaimplementowanie i porównanie ze sobą dwóch metod rozwiązywania
#  (znajdowania miejsca zerowego) równań nieliniowych. 
# Implementacja Metody Bisekcji oraz Metoda Stycznych.
#
# 1. Osiągnięcie zadanej dokładności obliczeń (wariant A lub B powyżej); 
# 2. Wykonanie określonej przez użytkownika liczby iteracji.
#
# Program ma mieć wbudowane kilka różnych funkcji nieliniowych: wielomian, trygonometryczną, wykładniczą i ich złożenia. 
# Użytkownik wybiera jedną z funkcji, określa przedział na którym poszukiwane jest miejsce zerowe oraz wybiera 
# kryterium zatrzymania algorytmu: 
#   a) spełnienie warunku nałożonego na dokładność [|x(i) − x(i−1)| < ε]
#   b) osiągnięcie zadanej liczby iteracji.
#
# Następnie użytkownik wprowadza ε (w przypadku wybrania pierwszego kryterium) lub 
#  liczbę iteracji (w przypadku wyboru drugiego kryterium). 
#
# Program wykonuje obliczenia przy użyciu obu metod (bisekcja oraz jeden z przydzielonych wariantów), 
#  wyświetla wyniki i rysuje wykres wybranej funkcji na zadanym przedziale, 
#  zaznaczając rozwiązania na wykresie. 
#
# Program ma sprawdzać poprawność założenia o przeciwnych znakach funkcji na krańcach badanego przedziału. 
# Nie trzeba sprawdzać prawdziwości założeń o stałym znaku pochodnych na przedziale. 
# W przypadku metody stycznych dozwolone jest zakodowanie wartości pochodnej na sztywno, nie trzeba jej liczyć numerycznie.

# Wielomian
# W(x) = 1x^4 + 1x^3 + 1x^2 + 1x + 1 

# Note! float in python is same as C double type !

# TEXTS
text_section_begin: str = "Podaj wartość reprezentującą początek przedziału: "
text_section_end: str = "Podaj wartość reprezentującą koniec przedziału: "
text_select_criterion: str = "Wybierz kryterium (1.Spełnienie warunku epsilon  2.Liczba Iteracji): "
text_select_upper_function: str = "Wybierz funkcję nadrzędną (1.Wielomian, 2.Trygonometryczna, 3.Wykładnicza): "
text_select_function: str = "Wybierz funkcję (1.Wielomian, 2.Trygonometryczna, 3.Wykładnicza, 4.Złożona): "
text_select_trygonomic_function: str = "Wybierz funkcję trygonometryczną (1.Sinus, 2.Cosinus, 3.Tanges 4.Cotanges): "
text_error_wrong_input: str = "Wprowadzono błędny znak nie odpowiadający poleceniu!"


class polynomial:
    def __int__(self):
        pass
    def value(self) -> float:
        pass

class exponensial:
    a = float
    b = float
    def __init__(self):
        print("Funkcja wykładnicza ma postać f(x)=a*e^(bx)")
        self.a = input("Podaj wartość a:")
        self.b = input("Podaj wartość b:")
    def value(self,x) -> float:
        e = numpy.e
        return self.a * (e ** (self.b * x))

class trygonometric:
    def __init__(self):
        self.function_type:int=0
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

class combination:
    def __init__(self):
        function1_type = int(input(text_select_upper_function))
        match function1_type:
            case 1:
                print("Wybrano funckje typu wielomian.")
                self.function1 = polynomial()
            case 2:
                print("Wybrano funckje typu trygonometryczna.")
                self.function1 = trygonometric()
            case 3:
                print("Wybrano funckje typu wykładnicza.")
                self.function1 = exponensial()
            case other:
                return

        function2_type = int(input(text_select_function))
        match function2_type:
            case 1:
                print("Wybrano funckje typu wielomian.")
                self.function2 = polynomial()
            case 2:
                print("Wybrano funckje typu trygonometryczna.")
                self.function2 = trygonometric()
            case 3:
                print("Wybrano funckje typu wykładnicza.")
                self.function2 = exponensial()
            case 4:
                print("Wybrano funckje typu złożona.")
                self.function2 = combination()
            case other:
                return

    def value(self,x) -> float:
        return self.function1.value(self.function2.value(x))

def polynomial_iteration_search(section_start: float, section_end: float, iteration_number: float):
    polynomial_values: List[int]
    input_number: int = 0

    print("Początek: " + str(section_start) + ", koniec: " + str(section_end))

    # INPUT POLYNOMIAL 
    print("Wprowadz stopien wielomianu: ")
    input_number = int(input()) + 1         # get polygonal rank - length of the array. +1 because 0 - miejsce zerowe.
    polynomial_values = [0] * input_number  # initialize array with 0's.

    # Get a, b, c, d, ... values.
    #for i in range(0, input_number):
    for i in range(input_number - 1, 0 - 1, -1):
        print("Wprowadz wartosc " + str(i) + " skladnika wielomianu: ")
        polynomial_values[input_number - 1 - i] = int(input())

    # Get x value
    print("Wprowadz wartosc x: ")
    input_number = int(input())

    # BISECTION METHOD
    bisection_iterations: int = bisection_method.polynomial_iteration(iteration_number, polynomial_values, section_start, section_end)
    print("besection: " + str(bisection_iterations))

    derivative_values: List[int] = [3, 0, -2] #[1, 0, -2, -5]
    newton_iterations: int = newtons_method.polynomial_iteration(iteration_number, input_number, polynomial_values, derivative_values)
    print("newton: " + str(newton_iterations))


def trigonometric_iteration_search(section_start: float, section_end: float, iteration_number: float):
    pass


def exponensial_iteration_search(section_start: float, section_end: float, iteration_number: float):
    pass


def combination_iteration_search(section_start: float, section_end: float, iteration_number: float):
    pass


def polynomial_epsilon_search(section_start: float, section_end: float, epsilon_number: int):
    polynomial_values: List[int]
    input_number: int = 0

    print("Początek: " + str(section_start) + ", koniec: " + str(section_end))


    # INPUT POLYNOMIAL 
    print("Wprowadz stopien wielomianu: ")
    input_number = int(input()) + 1         # get polygonal rank - length of the array. +1 because 0 - miejsce zerowe.
    polynomial_values = [0] * input_number  # initialize array with 0's.

    # Get a, b, c, d, ... values.
    #for i in range(0, input_number):
    for i in range(input_number - 1, 0 - 1, -1):
        print("Wprowadz wartosc " + str(i) + " skladnika wielomianu: ")
        polynomial_values[input_number - 1 - i] = int(input())

    # Get x value
    print("Wprowadz wartosc x: ")
    input_number = int(input())


    # BISECTION METHOD
    bisection_iterations: int = bisection_method.polynomial_epsilon(epsilon_number, polynomial_values, section_start, section_end)
    print("bisection: " + str(bisection_iterations))

    derivative_values: List[int] = [3, 0, -2] #[1, 0, -2, -5]
    newton_iterations: int = newtons_method.polynomial_epsilon(epsilon_number, input_number, polynomial_values, derivative_values)
    print("newton: " + str(newton_iterations))


def trigonometric_epsilon_search(section_start: float, section_end: float, epsilon_number: int):
    pass


def exponensial_epsilon_search(section_start: float, section_end: float, epsilon_number: int):
    pass


def combination_epsilon_search(section_start: float, section_end: float, epsilon_number: int):
    pass


def main():
    # 1. Wybór funkcji
    # 2. Wybiera przedział A-B
    # 3. Wybiera kryterium a, b

    section_start: float = 0
    section_end: float = 0
    function_type: int = 0

    function_type = int(input(text_select_function))
    match function_type:
        case 1:
            print("Wybrano funckje typu wielomian.")
        case 2:
            print("Wybrano funckje typu trygonometryczna.")
        case 3:
            print("Wybrano funckje typu wykładnicza.")
        case 4:
            print("Wybrano funckje typu złożona.")
        case other:
            print(text_error_wrong_input)
            return

    section_start = float(input(text_section_begin))
    section_end = float(input(text_section_end))
    selected_criterion = int(input(text_select_criterion))

    if selected_criterion == 1:  # [ |x(i) − x(i−1)| < ε ]
        print("Wybrano kryterium [ |x(i) − x(i−1)| < ε ]")
        epsilon: float = 0
        epsilon = float(input("Wprowadź wartość epsilon: "))

        match function_type:
            case 1:
                polynomial_epsilon_search(section_start, section_end, epsilon)
            case 2:
                trigonometric_epsilon_search(section_start, section_end, epsilon)
            case 3:
                exponensial_epsilon_search(section_start, section_end, epsilon)
            case 4:
                combination_epsilon_search(section_start, section_end, epsilon)
            case other:
                print(text_error_wrong_input)
                return

    elif selected_criterion == 2:  # Iteration
        print("Wybrano kryterium [ Liczba iteracji ]")
        iteration_number: int = 0
        iteration_number = int(input("Wprowadź liczbę iteracji: "))

        match function_type:
            case 1:
                polynomial_iteration_search(section_start, section_end, iteration_number)
            case 2:
                trigonometric_iteration_search(section_start, section_end, iteration_number)
            case 3:
                exponensial_iteration_search(section_start, section_end, iteration_number)
            case 4:
                combination_iteration_search(section_start, section_end, iteration_number)
            case other:
                print(text_error_wrong_input)
                return

    input_number = input()


if __name__ == '__main__':
    main()
