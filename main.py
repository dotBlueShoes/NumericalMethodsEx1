import numpy
from typing import List

from functions.trigonometric import trigonometric
from functions.exponensial import exponensial
from functions.polynomial import polynomial
from functions.combination import combination

import methods.bisection as bisection
import methods.newtons as newtons
import methods.secant as secant

# TEXTS
text_section_begin: str = "Podaj wartość reprezentującą początek przedziału: "
text_section_end: str = "Podaj wartość reprezentującą koniec przedziału: "
text_select_criterion: str = "Wybierz kryterium (1.Spełnienie warunku epsilon  2.Liczba Iteracji): "
text_error_wrong_input: str = "Wprowadzono błędny znak nie odpowiadający poleceniu!"
text_select_function: str = "Wybierz funkcję (1.Wielomian, 2.Trygonometryczna, 3.Wykładnicza, 4.Złożona): "

# HARDCODED VALUES
hardcoded_polynomial: List[float] = [1, 0, -2, -5]
hardcoded_trigonometric: int = 2 # define - sin, cos, tg, ctg
hardcoded_exponensial: List[float] = [3, -2]
hardcoded_combination: List[int] = [1, 2] # define - wielomian, trygonometryczna, wykładnicza; wielomian, trygonometryczna, wykładnicza, złożona 

def polynomial_iteration_search(section_start: float, section_end: float, iteration_number: float):

    polynomial_values = polynomial(hardcoded_polynomial) 

    print("\n")

    # BISECTION METHOD
    bisection_iterations: int = bisection.iteration(iteration_number, polynomial_values, section_start, section_end)
    print("bisection: " + str(bisection_iterations) + "\n")

    # SECANT METHOD
    secant_iterations: int = secant.iteration(iteration_number, polynomial_values, section_start, section_end)
    print("secant: " + str(secant_iterations))
    

def polynomial_epsilon_search(section_start: float, section_end: float, epsilon_number: int):

    polynomial_values = polynomial(hardcoded_polynomial)

    print("\n")

    # BISECTION METHOD
    bisection_iterations: int = bisection.epsilon(epsilon_number, polynomial_values, section_start, section_end)
    print("bisection: " + str(bisection_iterations) + "\n")

    # SECANT METHOD
    secant_iterations: int = secant.epsilon(epsilon_number, polynomial_values, section_start, section_end)
    print("secant: " + str(secant_iterations))

def trigonometric_iteration_search(section_start: float, section_end: float, iteration_number: float):

    trigonometric_values = trigonometric(hardcoded_trigonometric)

    print("\n")

    # BISECTION METHOD
    bisection_iterations: int = bisection.iteration(iteration_number, trigonometric_values, section_start, section_end)
    print("bisection: " + str(bisection_iterations) + "\n")

    # SECANT METHOD
    secant_iterations: int = secant.iteration(iteration_number, trigonometric_values, section_start, section_end)
    print("secant: " + str(secant_iterations))

def trigonometric_epsilon_search(section_start: float, section_end: float, epsilon_number: int):

    trigonometric_value = trigonometric(hardcoded_trigonometric)

    print("\n")

    # BISECTION METHOD
    bisection_iterations: int = bisection.epsilon(epsilon_number, trigonometric_value, section_start, section_end)
    print("bisection: " + str(bisection_iterations) + "\n")

    # SECANT METHOD
    secant_iterations: int = secant.epsilon(epsilon_number, trigonometric_value, section_start, section_end)
    print("secant: " + str(secant_iterations))

def exponensial_iteration_search(section_start: float, section_end: float, iteration_number: float):

    exponensial_value = exponensial(hardcoded_exponensial)

    print("\n")

    # BISECTION METHOD
    bisection_iterations: int = bisection.iteration(iteration_number, exponensial_value, section_start, section_end)
    print("bisection: " + str(bisection_iterations) + "\n")

    # SECANT METHOD
    secant_iterations: int = secant.iteration(iteration_number, exponensial_value, section_start, section_end)
    print("secant: " + str(secant_iterations))

def exponensial_epsilon_search(section_start: float, section_end: float, epsilon_number: int):

    exponensial_value = exponensial(hardcoded_exponensial)

    print("\n")

    # BISECTION METHOD
    bisection_iterations: int = bisection.epsilon(epsilon_number, exponensial_value, section_start, section_end)
    print("bisection: " + str(bisection_iterations) + "\n")

    # SECANT METHOD
    secant_iterations: int = secant.epsilon(epsilon_number, exponensial_value, section_start, section_end)
    print("secant: " + str(secant_iterations))

def combination_iteration_search(section_start: float, section_end: float, iteration_number: float):

    combination_value = combination(hardcoded_combination)

    print("\n")

    # BISECTION METHOD
    bisection_iterations: int = bisection.iteration(iteration_number, combination_value, section_start, section_end)
    print("bisection: " + str(bisection_iterations) + "\n")

    # SECANT METHOD
    secant_iterations: int = secant.iteration(iteration_number, combination_value, section_start, section_end)
    print("secant: " + str(secant_iterations))

def combination_epsilon_search(section_start: float, section_end: float, epsilon_number: int):

    combination_value = combination(hardcoded_combination)

    print("\n")

    # BISECTION METHOD
    bisection_iterations: int = bisection.epsilon(epsilon_number, combination_value, section_start, section_end)
    print("bisection: " + str(bisection_iterations) + "\n")

    # SECANT METHOD
    secant_iterations: int = secant.epsilon(epsilon_number, combination_value, section_start, section_end)
    print("secant: " + str(secant_iterations))

# 1. Wybór funkcji
# 2. Wybiera przedział A - B
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
