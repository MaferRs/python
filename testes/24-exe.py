lista_numeros = [9.56783, 7.57568, 3.00914, 6.2321]

lista_precisao = [2, 2, 3, 3]
def arredondamento(x, y): return round(x, y)


resultado = list(map(arredondamento, lista_numeros, lista_precisao))
print(resultado)
