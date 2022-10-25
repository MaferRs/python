

from functools import reduce


def f_soma(x, y): return x+y


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = reduce(f_soma, numeros)
