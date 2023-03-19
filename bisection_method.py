from typing import List
import shared

def bisection_method_recurent(polynomial_values: List[int], section_start: float, section_end: float):
    section_mid: float = (section_start + section_end) / 2
    mid_result: float = shared.calc_polynomial_function(polynomial_values, section_mid)

    if mid_result == 0:
        print("Wynik: x = " + str(section_mid) + " jest miejscem 0'wym.")
        return
    else:
        result_start: float = shared.calc_polynomial_function(polynomial_values, section_start)
        # result_end: float = calc_polynomial_function(polynomial_values, section_end)

        # Sprawdzenie czy znak jest taki sam.
        if result_start >= 0 and mid_result >= 0 or result_start < 0 and mid_result < 0:
            # [c, b]
            print("+, " + str(result_start) + ", " + str(mid_result))
            bisection_method_recurent(polynomial_values, section_mid, section_end)
        else:
            # [a, c]
            print("-, " + str(result_start) + ", " + str(mid_result))
            bisection_method_recurent(polynomial_values, section_start, section_mid)
            
def bisection_method(iterations: int, polynomial_values: List[int], section_start: float, section_end: float):
	for i in range(iterations):

		section_mid: float = (section_start + section_end) / 2
		mid_result: float = shared.calc_polynomial_function(polynomial_values, section_mid)
		#print("mid_result = " + str(mid_result))

		print("section: " + str(section_start) + ", " + str(section_mid) + ", " + str(section_end))

		if mid_result == 0.0:
			print("Wynik: x = " + str(section_mid) + " jest miejscem 0'wym.")
			return
		else:
			result_start: float = shared.calc_polynomial_function(polynomial_values, section_start)
			if (result_start >= 0 and mid_result >= 0) or (result_start < 0 and mid_result < 0): # Check for the same sign
				print("+, " + str(result_start) + ", " + str(mid_result) + ", ")
				#bisection_method_recurent(polynomial_values, section_mid, section_end)
				section_start = section_mid
			else:
				print("-, " + str(result_start) + ", " + str(mid_result))
				#bisection_method_recurent(polynomial_values, section_start, section_mid)
				section_end = section_mid

	#if mid_result == 0:
	#	print("Wynik: x = " + str(section_mid) + " jest miejscem 0'wym.")
	#	return
	#else:
	#	result_start: float = shared.calc_polynomial_function(polynomial_values, section_start)
	#	# result_end: float = calc_polynomial_function(polynomial_values, section_end)
	#
	#	# Sprawdzenie czy znak jest taki sam.
	#	if result_start >= 0 and mid_result >= 0 or result_start < 0 and mid_result < 0:
	#		# [c, b]
	#		print("+, " + str(result_start) + ", " + str(mid_result))
	#		bisection_method_recurent(polynomial_values, section_mid, section_end)
	#	else:
	#		# [a, c]
	#		print("-, " + str(result_start) + ", " + str(mid_result))
	#		bisection_method_recurent(polynomial_values, section_start, section_mid)