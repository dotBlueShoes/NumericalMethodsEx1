import matplotlib.pyplot as plt
import statistics as stat

def plot_function(obj: object, start, end, title: str, zero_place: bool = False, place_zero : float = 0):
    x = []
    y = []
    i = start

    while i < end:
        x.append(i)
        y.append(obj.value(i))
        i = i + abs(start-end) / 100

    if zero_place:
        plt.scatter(place_zero,0)

    plt.xlabel('Wartości x')
    plt.ylabel('Wartości y')
    plt.title(title)
    plt.plot(x,y)
    plt.grid()
    plt.show()