# while True:
#     try:
#         x = int(input('Digite um n:'))
#         break
#     except ValueError:
#         print("entre com um n valido")


def dividir(x, y):
    try:
        resultado = x/y
        print(' a resposta é: , resultado')
    except ZeroDivisionError:
        print(" divisão por zero")


dividir(3, 0)
dividir(3, 2)

# try:
#    Bloco 1
# except:
#    Bloco 2
# Instrução fora do try/except
