from typing import List

#def calc_derivative(polynomial: List[int]) -> List[int]:


def calc_polynomial_function(polynomial: List[int], x_value: float) -> float:
	polynomial_degree: int = len(polynomial)
	last_elem: int = polynomial_degree - 1
	sum: float = 0
	
	#print("fe: " + str(polynomial[0]) + ", le: " + str(polynomial[last_elem]))
	sum += polynomial[0] * x_value	# highest degree.

	for i in range(1, last_elem):
		sum = (sum + polynomial[i]) * x_value

	sum += polynomial[last_elem]	# 0-degree that doesnt get multiplied by x.

	#for i in range(0, polynomial_degree):
	#	sum = polynomial[i]

	#	for j in range(polynomial_degree - i - 1):
	#		sum = sum * x_value

	#	result += sum
	return sum