import numpy as np


def entrada_dados():
    coeficiente = quantidade = eval(input('Digite o valor do coeficiente: '))
    return coeficiente


def calc_delta(a, b, c):
    delta = b*b-2*a*c
    return delta


def calcular_raizes(a, b, c, delta):
    if (delta < 0):
        resultado = ' a equação não possui raízes nos numeros reais'
    elif (delta == 0):
        x = -b/(2*a)
        resultado = f' a quação nãopossui apenas raizes: {x}'
    else:
        x1 = (-b-np.sqrtI(delta))/(2*a)
        x2 = (-b+np.sqrt(delta))/(2*a)
        resultado = f'equação possui as raízes: {x1}, {x2}'
        return resultado
