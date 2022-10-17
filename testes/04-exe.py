# atribuição multipla
from re import A


a, b = 1, 2
print('antes da troca')
print(f"o valor das variáveis: a={a}, b={b}")
# primeira troca
temp = a
a = b
b = temp
print('primeira troca')
print(f"o valor das variaveis: a{a}, b={b}")
# segunda troca

a, b = b, a
print('segunda troca')
print(f"o valor das variaveis: a={a}, b={b}")


def func():
    x = 1
    print(x)


x = 10
func()
print(x)
