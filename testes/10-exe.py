lista = [10, 2, 5, 5, 7, 6, 3]
n = len(lista)
soma = 0
for i in range(n):
    if (lista[i] % 2 == 0):
        soma = soma+lista[i]
        print(f'o somatório dos elementos pares da lista é: {soma}')


lista = [10, 2, 5, 5, 7, 6, 3]
soma = 0
for num in lista:
    if (num % 2 == 0):
        soma = soma+num
print(f'o somatório dos elementos pares da lista é: {soma}')

# len = verifica o comprimento do array
#range = intervalo
# método range(), Python cria uma sequência de números inteiros, desde uma maneira simples até a mais complexa.
