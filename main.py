import matplotlib.pyplot as plt
import csv
import numpy
import statistics as st


class Kwiat:
    sepal_length = float
    sepal_width = float
    petal_length = float
    petal_width = float

    def print_stat(self):
        print(f"{self.sepal_length}; {self.sepal_width}; {self.petal_length}; {self.petal_width}")


def tab1(nazwa: str, liczba: int, cala_liczba: int):
    procent = round(liczba / cala_liczba * 100, 1)
    print(f"{nazwa}: liczebność: {liczba}({procent}%)")


def tab2(lista1, lista2, lista3, liczebnosc):
    sepal_length = []
    sepal_width = []
    petal_length = []
    petal_width = []
    for kwiat in lista1:
        sepal_length.append(kwiat.sepal_length)
        sepal_width.append(kwiat.sepal_width)
        petal_length.append(kwiat.petal_length)
        petal_width.append(kwiat.petal_width)
    for kwiat in lista2:
        sepal_length.append(kwiat.sepal_length)
        sepal_width.append(kwiat.sepal_width)
        petal_length.append(kwiat.petal_length)
        petal_width.append(kwiat.petal_width)
    for kwiat in lista3:
        sepal_length.append(kwiat.sepal_length)
        sepal_width.append(kwiat.sepal_width)
        petal_length.append(kwiat.petal_length)
        petal_width.append(kwiat.petal_width)

    wyswietl("Długość działki kielicha (cm)", sepal_length, liczebnosc)
    wyswietl("Szerokość działki kielicha (cm)", sepal_width, liczebnosc)
    wyswietl("Długość płatka (cm)", petal_length, liczebnosc)
    wyswietl("Szerokość płatka (cm)", petal_width, liczebnosc)


def wyswietl(nazwa, tab, licz):
    print(
        f"{nazwa}: Minimum:{min(tab)} średnia:{srednia(tab, licz)} (±{odchylenie(tab, licz)}) Mediana:{round(st.median(tab), 2)} ({kwartyl_dolny(tab, licz)}-{kwartyl_gorny(tab, licz)}) Maksimum:{max(tab)}")


def srednia(tablica, liczebnosc):
    return round(sum(tablica) / liczebnosc, 2)


def odchylenie(tablica, liczebnosc):
    suma = 0
    for wartosc in tablica:
        suma = suma + (wartosc - srednia(tablica, liczebnosc)) ** 2
    return round(numpy.sqrt(suma / liczebnosc), 2)


def kwartyl_dolny(tablica, liczenosc):
    tablica.sort()
    return tablica[int((liczenosc - 1) / 4)]


def kwartyl_gorny(tablica, liczenosc):
    tablica.sort()
    return tablica[int(((liczenosc - 1) * 3) / 4)]


def wykresy(lista1, lista2, lista3):
    sepal_length = []
    sepal_width = []
    petal_length = []
    petal_width = []
    for kwiat in lista1:
        sepal_length.append(kwiat.sepal_length)
        sepal_width.append(kwiat.sepal_width)
        petal_length.append(kwiat.petal_length)
        petal_width.append(kwiat.petal_width)
    for kwiat in lista2:
        sepal_length.append(kwiat.sepal_length)
        sepal_width.append(kwiat.sepal_width)
        petal_length.append(kwiat.petal_length)
        petal_width.append(kwiat.petal_width)
    for kwiat in lista3:
        sepal_length.append(kwiat.sepal_length)
        sepal_width.append(kwiat.sepal_width)
        petal_length.append(kwiat.petal_length)
        petal_width.append(kwiat.petal_width)
    histogram("Długość działki kielicha", sepal_length)
    histogram("Szerokość działki kielicha", sepal_width)
    histogram("Długość płatka", petal_length)
    histogram("Szerokość płatka", petal_width)


def histogram(nazwa, tab):
    nniz = 0
    if (min(tab) < int(min(tab)) + 0.5):
        nniz = int(min(tab))
    else:
        nniz = int(min(tab)) + 0.5
    nmaks = 0
    if (max(tab) < int(max(tab)) + 0.5):
        nmaks = int(max(tab)) + 1
    else:
        nmaks = int(max(tab)) + 1.5

    bins = numpy.arange(nniz, nmaks, 0.5)
    plt.hist(tab, bins=bins, edgecolor='black')
    plt.title(nazwa)
    plt.ylabel("Liczebność")
    plt.xlabel("Długość (cm)")
    plt.show()


def wyk_pudelkowy(lista1, lista2, lista3):
    sepal_length_s = []
    sepal_length_ve = []
    sepal_length_vi = []

    sepal_width_s = []
    sepal_width_ve = []
    sepal_width_vi = []

    petal_length_s = []
    petal_length_ve = []
    petal_length_vi = []

    petal_width_s = []
    petal_width_ve = []
    petal_width_vi = []
    for kwiat in lista1:
        sepal_length_s.append(kwiat.sepal_length)
        sepal_width_s.append(kwiat.sepal_width)
        petal_length_s.append(kwiat.petal_length)
        petal_width_s.append(kwiat.petal_width)
    for kwiat in lista2:
        sepal_length_ve.append(kwiat.sepal_length)
        sepal_width_ve.append(kwiat.sepal_width)
        petal_length_ve.append(kwiat.petal_length)
        petal_width_ve.append(kwiat.petal_width)
    for kwiat in lista3:
        sepal_length_vi.append(kwiat.sepal_length)
        sepal_width_vi.append(kwiat.sepal_width)
        petal_length_vi.append(kwiat.petal_length)
        petal_width_vi.append(kwiat.petal_width)
    plt.boxplot([sepal_length_s, sepal_length_ve, sepal_length_vi], labels=['setosa', 'versicolor', 'virginica'])
    plt.ylabel('Długość (cm)')
    plt.show()
    plt.boxplot([sepal_width_s, sepal_width_ve, sepal_width_vi], labels=['setosa', 'versicolor', 'virginica'])
    plt.ylabel('Szerokość (cm)')
    plt.show()
    plt.boxplot([petal_length_s, petal_length_ve, petal_length_vi], labels=['setosa', 'versicolor', 'virginica'])
    plt.ylabel('Długość (cm)')
    plt.show()
    plt.boxplot([petal_width_s, petal_width_ve, petal_width_vi], labels=['setosa', 'versicolor', 'virginica'])
    plt.ylabel('Szerokość (cm)')
    plt.show()

# Celem zadania pierwszego jest zaimplementowanie i porównanie ze sobą dwóch metod rozwiązywania 
#  (znajdowania miejsca zerowego) równań nieliniowych. 
# Implementacja Metody Bisekcji oraz Metoda Stycznych.
#
# 1. Osiągnięcie zadanej dokładności obliczeń (wariant A lub B powyżej); 
# 2. Wykonanie określonej przez użytkownika liczby iteracji.
#
# Program ma mieć wbudowane kilka różnych funkcji nieliniowych: wielomian, trygonometryczną, wykładniczą i ich złożenia. 
# Użytkownik wybiera jedną z funkcji, określa przedział na którym poszukiwane jest miejsce zerowe oraz wybiera 
# kryterium zatrzymania algorytmu: 
#   a) spełnienie warunku nałożonego na dokładność [|x(i) − x(i−1)| < ε]
#   b) osiągnięcie zadanej liczby iteracji. 
# Następnie użytkownik wprowadza ε (w przypadku wybrania pierwszego kryterium) lub 
#  liczbę iteracji (w przypadku wyboru drugiego kryterium). 
#
# Program wykonuje obliczenia przy użyciu obu metod (bisekcja oraz jeden z przydzielonych wariantów), 
#  wyświetla wyniki i rysuje wykres wybranej funkcji na zadanym przedziale, 
#  zaznaczając rozwiązania na wykresie. 
#
# Program ma sprawdzać poprawność założenia o przeciwnych znakach funkcji na krańcach badanego przedziału. 
# Nie trzeba sprawdzać prawdziwości założeń o stałym znaku pochodnych na przedziale. 
# W przypadku metody stycznych dozwolone jest zakodowanie wartości pochodnej na sztywno, nie trzeba jej liczyć numerycznie.

def main():
    
    pass
    #with open('dane/data.csv', mode='r') as file:
    #    lines = csv.reader(file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    #    licz_stosa = 0
    #    licz_versicolor = 0
    #    licz_virginica = 0
    #    tab_stosa = []
    #    tab_versicolor = []
    #    tab_virginica = []
    #    for line in lines:
    #        kwiat = Kwiat()
    #        kwiat.sepal_length = line[0]
    #        kwiat.sepal_width = line[1]
    #        kwiat.petal_length = line[2]
    #        kwiat.petal_width = line[3]
    #        if line[4] == 0:
    #            print("setosa")
    #            tab_stosa.append(kwiat)
    #            licz_stosa = licz_stosa + 1
    #            tab_stosa[licz_stosa - 1].print_stat()
    #        elif line[4] == 1:
    #            print("versicolor")
    #            tab_versicolor.append(kwiat)
    #            licz_versicolor = licz_versicolor + 1
    #            tab_versicolor[licz_versicolor - 1].print_stat()
    #        elif line[4] == 2:
    #            print("virginica")
    #            tab_virginica.append(kwiat)
    #            licz_virginica = licz_virginica + 1
    #        else:
    #            print("Wrong data")
    #    liczebnosc = licz_stosa + licz_versicolor + licz_virginica
    #    tab1("setosa", licz_stosa, liczebnosc)
    #    tab1("versicolor", licz_versicolor, liczebnosc)
    #    tab1("virginica", licz_virginica, liczebnosc)
    #    tab1("Razem",liczebnosc,liczebnosc)
    #    tab2(tab_stosa, tab_versicolor, tab_virginica, liczebnosc)
    #    wykresy(tab_stosa, tab_versicolor, tab_virginica)
    #    wyk_pudelkowy(tab_stosa, tab_versicolor, tab_virginica)


if __name__ == '__main__':
    main()
