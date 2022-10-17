nota = 8.5


if (nota >= 7.0):
    situacao = "aprovado"
elif (nota >= 5.0):
    situacao = 'recuperação'
else:
    situacao = 'reprovado'

print(f'o estudante está: {situacao}')
