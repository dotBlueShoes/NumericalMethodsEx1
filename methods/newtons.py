from typing import List
import helpers

# Also called Newton-Raphson method
# Needs a redo.

def polynomial_iteration(
	iterations: int, 
	x_value: float, 
	polynomial_values: List[float], 
	derivative_values: List[float], 
) -> int:
	
	previous: float = x_value
	current: float = 0
	i: int = 0

	for i in range(iterations):
		current = previous - (
			helpers.calc_polynomial_function(polynomial_values, previous) / 
			helpers.calc_polynomial_function(derivative_values, previous)
		)
		previous = current
		print("I " + str(i + 1) + ": 0: " + str(previous))

	return i

def polynomial_epsilon(
	epsilon: float, 
	x_value: float, 
	polynomial_values: List[float], 
	derivative_values: List[float], 
) -> int:
	
	current: float = x_value
	previous: float = 0
	i: int = 0

	while epsilon < abs(current - previous):
		print(str(abs(current - previous)))

		previous = current
		current = previous - (
			helpers.calc_polynomial_function(polynomial_values, previous) / 
			helpers.calc_polynomial_function(derivative_values, previous)
		)
		
		print("I " + str(i + 1) + ": 0: " + str(current))

	return i