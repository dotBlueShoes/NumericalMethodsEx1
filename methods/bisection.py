from typing import List
from sys import float_info
import ploting
            
def iteration(iterations: int, mathematical_function: object, section_start: float, section_end: float) -> int:
	i: int = 0
	range_start = section_start
	range_end = section_end
	for i in range(iterations):

		section_mid: float = (section_start + section_end) / 2
		mid_result: float = mathematical_function.value(section_mid)

		print("I " + str(i + 1) + ": s/m/e: " + str(section_start) + ", " + str(section_mid) + ", " + str(section_end))

		if mid_result == 0.0:
			print("WYNIK: x = " + str(section_mid) + " jest miejscem 0'wym.")
			ploting.plot_function(mathematical_function, range_start, range_end, 'Metoda bisekcji', True, section_mid)
			return i
		else:
			result_start: float = mathematical_function.value(section_start)
			if (result_start >= 0.0 and mid_result >= 0.0) or (result_start < 0.0 and mid_result < 0.0): # Check for the same sign
				section_start = section_mid
			else:
				section_end = section_mid

	ploting.plot_function(mathematical_function, range_start, range_end, 'Metoda bisekcji', True, section_mid)
	return i

# |x(i) − x(i−1)| < ε
def epsilon(epsilon: float, mathematical_function: object, section_start: float, section_end: float) -> int:
	range_start = section_start
	range_end = section_end
	section_mid: float = float_info.max
	prev_section_mid: float = 0
	mid_result: float = 0
	i: int = 0

	while epsilon < abs(section_mid - prev_section_mid):

		prev_section_mid = section_mid
		section_mid = (section_start + section_end) / 2

		#print(str(abs(section_mid - prev_section_mid)))

		mid_result = mathematical_function.value(section_mid)
		#print("mid_result: " + str(mid_result))

		i += 1
		print("I " + str(i) + ": s/m/e: " + str(section_start) + ", " + str(section_mid) + ", " + str(section_end))

		if mid_result == 0.0:
			print("WYNIK: x = " + str(section_mid) + " jest miejscem 0'wym.")
			ploting.plot_function(mathematical_function, range_start, range_end,'Metoda bisekcji', True, section_mid)
			return i
		else:
			result_start: float = mathematical_function.value(section_start)
			if (result_start >= 0 and mid_result >= 0) or (result_start < 0 and mid_result < 0): # Check for the same sign
				#print("+, " + str(result_start) + ", " + str(mid_result) + ", ")
				section_start = section_mid
			else:
				#print("-, " + str(result_start) + ", " + str(mid_result))
				section_end = section_mid

	ploting.plot_function(mathematical_function, range_start, range_end, 'Metoda bisekcji', True, section_mid)
	return i