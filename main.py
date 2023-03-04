# Program tworzący opisy położenia i zróżnicowania rozkładu empirycznego w postaci tabel
#  na przykładzie klasycznego zbioru danych irysów. 
# Mateusz Strumiłło 242539. Program napisany w języku python z użyciem dod. pakietów
#		- cli-tables [ pip install cli-tables ] : do wyświetlenia tablic przy użyciu konsoli (moga się rozjeżdżać na mniejszych rozdzielczościach).

from cli_tables.cli_tables import print_table
import matplotlib.pyplot as plt
import numpy as np
import math
import csv

#region [ Classes ]

class Iris:
	def __init__(self, sepal_length: float, sepal_width: float, petal_length: float, petal_width: float):
		self.sepal_length = sepal_length
		self.petal_length = petal_length
		self.sepal_width = sepal_width
		self.petal_width = petal_width
	
	# UNUSED
	#def print(self):
	#	print(f'{self.sepal_length} {self.sepal_width} {self.petal_length} {self.petal_width}')

class Measures:
	def __init__(self, numericValues: list[float]):
		self.numericValues = numericValues
		self.numericValues.sort()

	def minimum(self) -> float:
		return min(self.numericValues)
	
	def maximum(self) -> float:
		return max(self.numericValues)

	def arithmetic_averge(self) -> float:
		return sum(self.numericValues) / len(self.numericValues)

	def median(self) -> float:
		if (len(self.numericValues) % 2 == 0):
			return (self.numericValues[int(len(self.numericValues) / 2) - 1] + self.numericValues[int(len(self.numericValues) / 2)]) / 2
		else:
			return self.numericValues[int((len(self.danumericValuesta_list) - 1) / 2 )] 

	def standard_deviation(self) -> float:
		avarge = self.arithmetic_averge()
		deviation = 0

		for val in self.numericValues:
			deviation += (val - avarge)**2

		deviation /= len(self.numericValues)
		deviation = math.sqrt(deviation)
		return deviation

	def quartile_first(self) -> float:
		return self.numericValues[int((len(self.numericValues) - 1) / 4)]

	def quartile_last(self) -> float:
		return self.numericValues[int(((len(self.numericValues) - 1) * 3) / 4)]

#endregion

#region [ Printing ]

def display_sum_table(setosa_count: str, versicolor_count: str, virginica_count: str, whole_length: str) -> None:
	print_table([
		['Gatunek', 	'Liczebność (%)'],
		['setosa', 		setosa_count	],
		['versicolor', 	versicolor_count],
		['virginica', 	virginica_count	],
		['Razem', 		whole_length	],
	])

def display_table(
	sepal_lengths_measures: Measures, 
	sepal_widths_measures: Measures, 
	petal_lengths_measures: Measures, 
	petal_widths_measures: Measures
) -> None:
	print_table([
		['Cecha', 'Minimum', 'Śr. arytm. (±odchy.stand.)', 'Mediana (Q1 - Q3)', 'Maksimum'],

		[
			'Długość działki kielicha (cm)',
			str(sepal_lengths_measures.minimum()), 
			'{} (±{})'.format(
       			round(sepal_lengths_measures.arithmetic_averge(),	2),
          		round(sepal_lengths_measures.standard_deviation(),	2)
            ),
			'{} ({} - {})'.format(
       			sepal_lengths_measures.median(),
          		sepal_lengths_measures.quartile_first(), 
            	sepal_lengths_measures.quartile_last()
            ), 
			str(sepal_lengths_measures.maximum())
		],

		[
			'Szerokość działki kielicha (cm)',
			str(sepal_widths_measures.minimum()), 
			'{} (±{})'.format(
       			round(sepal_widths_measures.arithmetic_averge(),	2),
          		round(sepal_widths_measures.standard_deviation(),	2)
            ), 
			'{} ({} - {})'.format(	
                sepal_widths_measures.median(),
                sepal_widths_measures.quartile_first(),
                sepal_widths_measures.quartile_last()
            ), 
			str(sepal_widths_measures.maximum())
		],

		[
			'Długość Płatka (cm)',
			str(petal_lengths_measures.minimum()), 
			'{} (±{})'.format(
       			round(petal_lengths_measures.arithmetic_averge(),	2),
          		round(petal_lengths_measures.standard_deviation(),	2)
            ), 
			'{} ({} - {})'.format(
       			petal_lengths_measures.median(), 
                petal_lengths_measures.quartile_first(),
                petal_lengths_measures.quartile_last()
            ), 
			str(petal_lengths_measures.maximum())
		],

		[
			'Szerokość płatka (cm)',
			str(petal_widths_measures.minimum()), 
			'{} (±{})'.format(
       			round(petal_widths_measures.arithmetic_averge(),	2),
          		round(petal_widths_measures.standard_deviation(),	2)
            ), 
			'{} ({} - {})'.format(
       			petal_widths_measures.median(),
          		petal_widths_measures.quartile_first(),
            	petal_widths_measures.quartile_last()
            ), 
			str(petal_widths_measures.maximum())
		]
	])

#endregion

#region [ Plotting ]

def box_plot(title: str, window_title: str, iris_type = [Iris]):

	sepal_lengths 	= [iris.sepal_length for iris in iris_type]
	sepal_widths 	= [iris.sepal_width for iris in iris_type]
	petal_lengths 	= [iris.petal_length for iris in iris_type]
	petal_widths 	= [iris.petal_width for iris in iris_type]

	labels = ['sepal_lengths', 'sepal_widths', 'petal_lengths', 'petal_widths']
	data = [sepal_lengths, sepal_widths, petal_lengths, petal_widths]

	fig = plt.figure(figsize = (16, 9), dpi = 70)
	fig.canvas.manager.set_window_title(window_title)
	
	plot = plt.boxplot(data, patch_artist=True, labels = labels)
	plt.title(title)

	colors = ['pink', 'lightblue', 'lightgreen', 'tan']
	for patch, color in zip(plot['boxes'], colors):
		patch.set_facecolor(color)

	plt.show()

def hist_plot(window_title: str, setosas = [Iris], versicolors = [Iris], virginicas = [Iris]):

	labels = ['Setosa', 'Versicolor', 'Virginica']
	colors = ['lightblue', 'yellow', 'red']

	fig = plt.figure(figsize = (16, 9), dpi = 70)
	fig.canvas.manager.set_window_title(window_title)

	# SEPAL LENGTHS
	lengths = np.transpose(np.array([
		[iris.sepal_length for iris in setosas], 
		[iris.sepal_length for iris in versicolors], 
		[iris.sepal_length for iris in virginicas]
	]))

	bins = int(len(lengths) / 2)

	ax = plt.subplot(2, 2, 1)
	ax.hist(
		lengths, bins = bins, histtype = 'bar', stacked = False, 
		fill = True, label = labels, color = colors, edgecolor = "k"
	)

	ax.set_title('Histogram długości działki kielicha')
	ax.set_xlabel('Długość działki kielicha')
	ax.set_ylabel('Ilość')
	ax.grid(True)
	ax.legend()

	# SEPAL WIDTHS
	lengths = np.transpose(np.array([
		[iris.sepal_width for iris in setosas], 
		[iris.sepal_width for iris in versicolors], 
		[iris.sepal_width for iris in virginicas]
	]))

	bins = int(len(lengths) / 2)

	ax = plt.subplot(2, 2, 2)
	ax.hist(
		lengths, bins = bins, histtype = 'bar', stacked = False, 
		fill = True, label = labels, color = colors, edgecolor = "k"
	)

	ax.set_title('Histogram szerokości działki kielicha')
	ax.set_xlabel('Szerokość działki kielicha')
	ax.set_ylabel('Ilość')
	ax.grid(True)
	ax.legend()

	# PETAL LENGTHS
	lengths = np.transpose(np.array([
		[iris.petal_length for iris in setosas], 
		[iris.petal_length for iris in versicolors], 
		[iris.petal_length for iris in virginicas]
	]))

	bins = int(len(lengths) / 2)

	ax = plt.subplot(2, 2, 3)
	ax.hist(
		lengths, bins = bins, histtype = 'bar', stacked = False, 
		fill = True, label = labels, color = colors, edgecolor = "k"
	)

	ax.set_title('Histogram długośći działki płatka')
	ax.set_xlabel('Długość działki płatka')
	ax.set_ylabel('Ilość')
	ax.grid(True)
	ax.legend()

	# PETAL WIDTHS
	lengths = np.transpose(np.array([
		[iris.petal_width for iris in setosas], 
		[iris.petal_width for iris in versicolors], 
		[iris.petal_width for iris in virginicas]
	]))

	bins = int(len(lengths) / 2)

	ax = plt.subplot(2, 2, 4)
	ax.hist(
		lengths, bins = bins, histtype = 'bar', stacked = False, 
		fill = True, label = labels, color = colors, edgecolor = "k"
	)

	ax.set_title('Histogram szerokości działki płatka')
	ax.set_xlabel('Szerokość działki płatka')
	ax.set_ylabel('Ilość')
	ax.grid(True)
	ax.legend()

	plt.show()

#endregion

def display_iris_measures(iris_type_name: str, iris_type = []):
	sepal_lengths 	= Measures([iris.sepal_length for iris in iris_type])
	sepal_widths 	= Measures([iris.sepal_width for iris in iris_type])
	petal_lengths 	= Measures([iris.petal_length for iris in iris_type])
	petal_widths 	= Measures([iris.petal_width for iris in iris_type])

	print(iris_type_name)
	display_table(
		sepal_lengths, 
		sepal_widths, 
		petal_lengths, 
		petal_widths
	)

def main():

	# Path to the file that contains the data.
	data_path = 'dane/data.csv'

	# Creating the lists needed to contain read data.
	versicolors, setosas, virginicas = [], [], []

	# Opening the csv file using with and special csv class.
	with open(data_path, 'r') as csvfile:
		rows = csv.reader(csvfile, delimiter = ',', quoting = csv.QUOTE_NONNUMERIC)

		for row in rows:
			if row[-1] == 0:											# Setosa
				setosas.append(Iris(row[0], row[1], row[2], row[3]))
			elif row[-1] == 1: 											# Versicolor
				versicolors.append(Iris(row[0], row[1], row[2], row[3]))
			elif row[-1] == 2: 											# virginica
				virginicas.append(Iris(row[0], row[1], row[2], row[3]))

		# Getting the lengths
		versicolors_length = len(versicolors)
		virginicas_length = len(virginicas)
		setosas_length = len(setosas)
		whole_length = versicolors_length + virginicas_length + setosas_length

		# Measures
		if (whole_length != 0):
			versicolors_percentage_length = versicolors_length / whole_length
			virginicas_percentage_length = virginicas_length / whole_length
			setosas_percentage_length = setosas_length / whole_length

		# Printing
		print('\n')
		display_sum_table( 
			'{} ({}%)'.format(setosas_length, round(setosas_percentage_length, 2)),
			'{} ({}%)'.format(versicolors_length, round(versicolors_percentage_length, 2)),
			'{} ({}%)'.format(virginicas_length, round(virginicas_percentage_length, 2)),
			'{} (100%)'.format(whole_length)
		)

		display_iris_measures("Setosa", setosas)
		display_iris_measures("Versicolors", versicolors)
		display_iris_measures("Virginicas", virginicas)
		display_iris_measures("Wszystkie", setosas + versicolors + virginicas)
		print('\n')

		# Plotting
		box_plot("Setosa", data_path, setosas)
		box_plot("Versicolors", data_path, versicolors)
		box_plot("Virginicas", data_path, virginicas)
		box_plot("Wszystkie", data_path, setosas + versicolors + virginicas)
		hist_plot(data_path, setosas, versicolors, virginicas)


if __name__ == "__main__":
	main()