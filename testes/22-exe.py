veiculos = ['aviao', 'carro', 'navio', 'onibus']


def f_maiuscula(x): return str.upper(x)


nomes_maiusculos = list(map(f_maiuscula, veiculos))
print(f'nomes maiusculos = {nomes_maiusculos}')
