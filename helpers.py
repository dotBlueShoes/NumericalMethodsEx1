from typing import List
import numpy

#def calc_derivative(polynomial: List[int]) -> List[int]:

# 2, 0, 1
# 2x^2 + 1
# x(2x) + 1

# x(x(2) + 0*1) + 1

#def calc_polynomial_function(polynomial: List[int], x_value: float) -> float:
#	polynomial_degree: int = len(polynomial)
#	last_elem: int = polynomial_degree - 1
#	sum: float = 0
	
#	#print("fe: " + str(polynomial[0]) + ", le: " + str(polynomial[last_elem]))
#	sum += polynomial[0] * x_value	# highest degree.

#	for i in range(1, last_elem):
#		sum = (sum + polynomial[i]) * x_value

#	sum += polynomial[last_elem]	# 0-degree that doesnt get multiplied by x.

	#for i in range(0, polynomial_degree):
	#	sum = polynomial[i]

	#	for j in range(polynomial_degree - i - 1):
	#		sum = sum * x_value

	#	result += sum
#	return sum


# W zwiazku z zakazem podnoszenia do potęgi całkowitej za pomocą funkcji zastosowaliśmy dane rozwiazanie

def powii(x: int, y: int) -> int:
	value: int = 1
	for _i in range(y):
		value = value * x
	return value

def powfi(x: float, y: int) -> float:
	value: float = 1
	for _i in range(y):
		value = value * x
	return value

def powff(x: float, y: float) -> float:
	return numpy.float_power(x, y)