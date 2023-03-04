# NumericalMethodsEx1

      Metoda bisekcji
    1.Wybierz przedział [a, b], w którym znajduje się szukane miejsce zerowe f(x) = 0.
    2.Wybierz punkt środkowy c = (a + b) / 2.
    3.Oblicz wartość funkcji f(c).
    4.Jeśli f(c) = 0, to c jest szukanym miejscem zerowym i algorytm kończy działanie.
    5.Jeśli f(a) i f(c) mają różne znaki, to szukane miejsce zerowe znajduje się w przedziale [a, c], w przeciwnym przypadku znajduje się w przedziale [c, b].
    6.Powtarzaj kroki 2-5, dopóki nie znajdziesz szukanego miejsca zerowego z zadaną dokładnością.
    
    Metoda siecznych 
    1.Wybierz dwa punkty startowe x0 i x1.
    2.Oblicz wartości funkcji f(x0) i f(x1).
    3.Wykorzystując wartości funkcji, wyznacz przybliżenie wartości pochodnej w punkcie x1:
    f'(x1) ≈ (f(x1) - f(x0)) / (x1 - x0)
    4.Wyznacz kolejny przybliżony punkt zerowy x2 jako przecięcie siecznej przechodzącej przez punkty (x0, f(x0)) i (x1, f(x1)) z osią OX. 
    Można to obliczyć ze wzoru: x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    5.Przypisz x1 do x0 i x2 do x1.
    6.Powtarzaj kroki 3-5, aż osiągniesz zadaną dokładność lub ustalony limit iteracji.
