from typing import List

# Check if it is correct math!!! and comment through
#  użyj schematu Hornera.  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def calc_polynomial_function(polynomial: List[int], x_value: float) -> float:
    polynomial_degree: int = len(polynomial)
    result: float = 0
    sum: float = 0

    for i in range(0, polynomial_degree):
        sum = polynomial[i]

        for j in range(polynomial_degree - i - 1):
            sum = sum * x_value

        result += sum
    return result