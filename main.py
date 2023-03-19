import matplotlib.pyplot as plt
import numpy
import statistics as st
from typing import List

import methods.bisection as bisection
import methods.newtons as newtons
import methods.secant as secant

from functions.trigonometric import trigonometric
from functions.exponensial import exponensial
from functions.polynomial import polynomial

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

def value_exponential_fuction(a, b, x):
    e = numpy.e
    return a * (e ** (b * x))


def mabs(x):
    if x < 0:
        return x*(-1)
    else:
        return x


def factorial(x, y):
    value:int = 1
    if y%1 == 0: # W zwiazku z zakazem podnoszenia do potęgi całkowitej za pomocą funkcji zastosowaliśmy dane rozwiazanie
        for i in y:
            value = value * x
        return value
    else:
        return numpy.float_power(x, y)

# TEXTS
text_section_begin: str = "Podaj wartość reprezentującą początek przedziału: "
text_section_end: str = "Podaj wartość reprezentującą koniec przedziału: "
text_select_criterion: str = "Wybierz kryterium (1.Spełnienie warunku epsilon  2.Liczba Iteracji): "
text_error_wrong_input: str = "Wprowadzono błędny znak nie odpowiadający poleceniu!"
text_select_function: str = "Wybierz funkcję (1.Wielomian, 2.Trygonometryczna, 3.Wykładnicza, 4.Złożona): "

def polynomial_iteration_search(section_start: float, section_end: float, iteration_number: float):

    polynomial_values = polynomial([1, 0, -2, -5]) 
    #polynomial_values.input()

    print("\n")

    # BISECTION METHOD
    bisection_iterations: int = bisection.iteration(iteration_number, polynomial_values, section_start, section_end)
    print("bisection: " + str(bisection_iterations) + "\n")

    # SECANT METHOD
    secant_iterations: int = secant.iteration(iteration_number, polynomial_values, section_start, section_end)
    print("secant: " + str(secant_iterations))
    

def polynomial_epsilon_search(section_start: float, section_end: float, epsilon_number: int):

    polynomial_values = polynomial([1, 0, -2, -5]) #polynomial_values.input()

    print("\n")

    # BISECTION METHOD
    bisection_iterations: int = bisection.epsilon(epsilon_number, polynomial_values, section_start, section_end)
    print("bisection: " + str(bisection_iterations) + "\n")

    # SECANT METHOD
    secant_iterations: int = secant.epsilon(epsilon_number, polynomial_values, section_start, section_end)
    print("secant: " + str(secant_iterations))

def trigonometric_iteration_search(section_start: float, section_end: float, iteration_number: float):

    function_type: int = 1 # sin, cos, tg, ctg
    trigonometric_values = trigonometric(function_type)

    print("\n")

    # BISECTION METHOD
    bisection_iterations: int = bisection.iteration(iteration_number, trigonometric_values, section_start, section_end)
    print("bisection: " + str(bisection_iterations) + "\n")

    # SECANT METHOD
    secant_iterations: int = secant.iteration(iteration_number, trigonometric_values, section_start, section_end)
    print("secant: " + str(secant_iterations))

def trigonometric_epsilon_search(section_start: float, section_end: float, epsilon_number: int):

    function_type: int = 1 # sin, cos, tg, ctg
    trigonometric_value = trigonometric(function_type)

    print("\n")

    # BISECTION METHOD
    bisection_iterations: int = bisection.epsilon(epsilon_number, trigonometric_value, section_start, section_end)
    print("bisection: " + str(bisection_iterations) + "\n")

    # SECANT METHOD
    secant_iterations: int = secant.epsilon(epsilon_number, trigonometric_value, section_start, section_end)
    print("secant: " + str(secant_iterations))

def exponensial_iteration_search(section_start: float, section_end: float, iteration_number: float):

    exponensial_value = exponensial(-2)

    print("\n")

    # BISECTION METHOD
    bisection_iterations: int = bisection.iteration(iteration_number, exponensial_value, section_start, section_end)
    print("bisection: " + str(bisection_iterations) + "\n")

    # SECANT METHOD
    secant_iterations: int = secant.iteration(iteration_number, exponensial_value, section_start, section_end)
    print("secant: " + str(secant_iterations))

def exponensial_epsilon_search(section_start: float, section_end: float, epsilon_number: int):

    exponensial_value = exponensial(numpy.e) #exponensial(-2)

    print("\n")

    # BISECTION METHOD
    bisection_iterations: int = bisection.epsilon(epsilon_number, exponensial_value, section_start, section_end)
    print("bisection: " + str(bisection_iterations) + "\n")

    # SECANT METHOD
    secant_iterations: int = secant.epsilon(epsilon_number, exponensial_value, section_start, section_end)
    print("secant: " + str(secant_iterations))

def combination_iteration_search(section_start: float, section_end: float, iteration_number: float):
    pass

def combination_epsilon_search(section_start: float, section_end: float, epsilon_number: int):
    pass


# polynomial:
#  1: x^3 - 2x - 5, x = 2 
# 
# trigonometric:
#  1: sin(x) + sin(x/2)
#  x: cos(x) + sin(x) + tg(x) - ctg(x), x = 0
#

# 1. Wybór funkcji
# 2. Wybiera przedział A-B
# 3. Wybiera kryterium a, b
def main():

    limit_iterations: int = 2
    limit_epsilon: int = 1

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

    if selected_criterion == limit_epsilon:
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

    elif selected_criterion == limit_iterations:
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
