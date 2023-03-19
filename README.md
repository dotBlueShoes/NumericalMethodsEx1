# NumericalMethodsEx1

## Metoda bisekcji

1. Wybierz przedział [a, b], w którym znajduje się szukane miejsce zerowe f(x) = 0.
2. Wybierz punkt środkowy c = (a + b) / 2.
3. Oblicz wartość funkcji f(c).
4. Jeśli f(c) = 0, to c jest szukanym miejscem zerowym i algorytm kończy działanie.
5. Jeśli f(a) i f(c) mają różne znaki, to szukane miejsce zerowe znajduje się w przedziale [a, c], w 
przeciwnym przypadku znajduje się w przedziale [c, b].
6. Powtarzaj kroki 2-5, dopóki nie znajdziesz szukanego miejsca zerowego z zadaną dokładnością.
    
## Metoda siecznych 

1. Wybierz dwa punkty startowe x0 i x1.
2. Oblicz wartości funkcji f(x0) i f(x1).
3. Wykorzystując wartości funkcji, wyznacz przybliżenie wartości pochodnej w punkcie x1:
f'(x1) ≈ (f(x1) - f(x0)) / (x1 - x0)
4. Wyznacz kolejny przybliżony punkt zerowy x2 jako przecięcie siecznej przechodzącej przez punkty (x0, f(x0)) i (x1, f(x1)) z osią OX. 
 Można to obliczyć ze wzoru: x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
5. Przypisz x1 do x0 i x2 do x1.
6. Powtarzaj kroki 3-5, aż osiągniesz zadaną dokładność lub ustalony limit iteracji.

# Polecenie
Celem zadania pierwszego jest zaimplementowanie i porównanie ze sobą dwóch metod rozwiązywania
(znajdowania miejsca zerowego) równań nieliniowych. 
Implementacja Metody Bisekcji oraz Metoda Siecznych.

1. Osiągnięcie zadanej dokładności obliczeń (wariant A lub B powyżej); 
2. Wykonanie określonej przez użytkownika liczby iteracji.

Program ma mieć wbudowane kilka różnych funkcji nieliniowych: wielomian, trygonometryczną, wykładniczą i ich złożenia. 
Użytkownik wybiera jedną z funkcji, określa przedział na którym poszukiwane jest miejsce zerowe oraz wybiera 
kryterium zatrzymania algorytmu: 
a. spełnienie warunku nałożonego na dokładność [|x(i) − x(i−1)| < ε]
b. osiągnięcie zadanej liczby iteracji.

Następnie użytkownik wprowadza ε (w przypadku wybrania pierwszego kryterium) lub 
 liczbę iteracji (w przypadku wyboru drugiego kryterium). 

Program wykonuje obliczenia przy użyciu obu metod (bisekcja oraz jeden z przydzielonych wariantów), 
 wyświetla wyniki i rysuje wykres wybranej funkcji na zadanym przedziale, 
 zaznaczając rozwiązania na wykresie. 

Program ma sprawdzać poprawność założenia o przeciwnych znakach funkcji na krańcach badanego przedziału. 
Nie trzeba sprawdzać prawdziwości założeń o stałym znaku pochodnych na przedziale. 
W przypadku metody stycznych dozwolone jest zakodowanie wartości pochodnej na sztywno, nie trzeba jej liczyć numerycznie.

Wielomian
W(x) = 1x^4 + 1x^3 + 1x^2 + 1x + 1 

# Note! float in python is same as C double type !
