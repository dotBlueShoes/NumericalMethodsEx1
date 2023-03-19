from typing import List
import shared

# Also called Newton-Raphson method

def polynomial_iteration(
	iterations: int, 
	x_value: int, 
	polynomial_values: List[int], 
	derivative_values: List[int], 
) -> int:
	
	previous: int = x_value
	current: int = 0
	i: int = 0

	for i in range(iterations):
		current = previous - (
			shared.calc_polynomial_function(polynomial_values, previous) / 
			shared.calc_polynomial_function(derivative_values, previous)
		)
		previous = current
		print("I " + str(i + 1) + ": 0: " + str(previous))

	return i

def polynomial_epsilon(
	epsilon: int, 
	x_value: int, 
	polynomial_values: List[int], 
	derivative_values: List[int], 
) -> int:
	
	current: int = x_value
	previous: int = 0
	i: int = 0

	while epsilon < abs(current - previous):
		print(str(abs(current - previous)))

		previous = current
		current = previous - (
			shared.calc_polynomial_function(polynomial_values, previous) / 
			shared.calc_polynomial_function(derivative_values, previous)
		)
		
		print("I " + str(i + 1) + ": 0: " + str(current))

	return i