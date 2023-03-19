import ploting

def iteration(iterations: int, mathematical_function: object, section_start: float, section_end: float) -> int:
	
	prev_prev_value: float = section_start
	prev_value: float = section_end

	prev_prev_calculation: float
	prev_calculation: float

	current: float = 0
	i: int = 0
	
	for i in range(iterations):	

		prev_prev_calculation = mathematical_function.value(prev_prev_value)
		prev_calculation = mathematical_function.value(prev_value)

		denominator: float = (prev_calculation - prev_prev_calculation)
		if (denominator == 0.0):
			print("Mianownik wynosi '0' przerwanie iteracji ! [ Dla cos(x) przedział nie może być równy np. -5, 5]")
			ploting.plot_function(mathematical_function, section_start, section_end, 'Metoda siecznych', True, current)
			return i

		current = prev_value - (
			(prev_calculation * (prev_value - prev_prev_value)) /
			denominator
		)

		print("I " + str(i + 1) + ": pp/p/c: " + str(prev_prev_value) + ", " + str(prev_value) + ", " + str(current))

		prev_prev_value = prev_value
		prev_value = current

	ploting.plot_function(mathematical_function, section_start, section_end,'Metoda siecznych', True, current)
	return i

def epsilon(epsilon: float, mathematical_function: object, section_start: float, section_end: float) -> int:
	
	prev_prev_value: float = section_start
	prev_value: float = section_end
	current: float = 0

	prev_prev_calculation: float
	prev_calculation: float

	i: int = 0

	while epsilon < abs(prev_value - prev_prev_value):

		prev_prev_calculation = mathematical_function.value(prev_prev_value)
		prev_calculation = mathematical_function.value(prev_value)
		i += 1

		denominator: float = (prev_calculation - prev_prev_calculation)
		if (denominator == 0.0):
			print("Mianownik wynosi '0' przerwanie iteracji ! [ Dla cos(x) przedział nie może być równy np. -5, 5]")
			ploting.plot_function(mathematical_function, section_start, section_end, 'Metoda siecznych',True , current)
			return i

		current = prev_value - (
			(prev_calculation * (prev_value - prev_prev_value)) /
			denominator
		)

		print("I " + str(i) + ": pp/p/c: " + str(prev_prev_value) + ", " + str(prev_value) + ", " + str(current))

		prev_prev_value = prev_value
		prev_value = current

	ploting.plot_function(mathematical_function, section_start, section_end, 'Metoda siecznych', True , current)
	return i