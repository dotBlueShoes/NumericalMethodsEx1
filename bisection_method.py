from typing import List
from sys import float_info
import shared
            
def iteration(iterations: int, polynomial_values: List[int], section_start: float, section_end: float):
	for i in range(iterations):

		section_mid: float = (section_start + section_end) / 2
		mid_result: float = shared.calc_polynomial_function(polynomial_values, section_mid)

		print("I " + str(i + 1) + ": s/m/e: " +str(section_start) + ", " + str(section_mid) + ", " + str(section_end))

		if mid_result == 0.0:
			print("WYNIK: x = " + str(section_mid) + " jest miejscem 0'wym.")
			return
		else:
			result_start: float = shared.calc_polynomial_function(polynomial_values, section_start)
			if (result_start >= 0 and mid_result >= 0) or (result_start < 0 and mid_result < 0): # Check for the same sign
				#print("+, " + str(result_start) + ", " + str(mid_result) + ", ")
				section_start = section_mid
			else:
				#print("-, " + str(result_start) + ", " + str(mid_result))
				section_end = section_mid


# |x(i) − x(i−1)| < ε
def epsilon(epsilon: int, polynomial_values: List[int], section_start: float, section_end: float):
	
	section_mid: float = float_info.max
	prev_section_mid: float = 0
	mid_result: float = 0
	i: int = 0

	while epsilon < abs(section_mid - prev_section_mid):

		prev_section_mid = section_mid
		section_mid = (section_start + section_end) / 2

		#print(str(abs(section_mid - prev_section_mid)))

		mid_result = shared.calc_polynomial_function(polynomial_values, section_mid)

		i += 1
		print("I " + str(i) + ": s/m/e: " +str(section_start) + ", " + str(section_mid) + ", " + str(section_end))

		if mid_result == 0.0:
			print("WYNIK: x = " + str(section_mid) + " jest miejscem 0'wym.")
			return
		else:
			result_start: float = shared.calc_polynomial_function(polynomial_values, section_start)
			if (result_start >= 0 and mid_result >= 0) or (result_start < 0 and mid_result < 0): # Check for the same sign
				#print("+, " + str(result_start) + ", " + str(mid_result) + ", ")
				section_start = section_mid
			else:
				#print("-, " + str(result_start) + ", " + str(mid_result))
				section_end = section_mid