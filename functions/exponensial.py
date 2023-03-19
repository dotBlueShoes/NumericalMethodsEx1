from numpy import float_power

class exponensial:
    a = float
    #b = float
    def __init__(self, a):
        self.a = a
        #self.b = b

    def input(self):
        print("Funkcja wykładnicza ma postać f(x)=a*e^(bx)")
        self.a = input("Podaj wartość a:")
        #self.b = input("Podaj wartość b:")

    def value(self: float, x: float) -> float:
        #print("complex: " + str(numpy.float_power(self.a, x)))
        #print("complex: " + str(self.a ** x))
        return float_power(self.a, x)
        #return factorial(self.a, x)