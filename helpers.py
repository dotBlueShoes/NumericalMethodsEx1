from typing import List
import numpy

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