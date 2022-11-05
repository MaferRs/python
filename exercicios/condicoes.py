# mana_jogador = 5
# mana_invocar = int(input('Custo de mana do card: '))

# if mana_jogador >= mana_invocar:
#     print('Card posicionado na mesa de jogo.')

# mana_jogador2 = 5
# mana_invocar = int(input('Custo de mana do card: '))

# if mana_jogador2 >= mana_invocar:
#     mana_jogador2 = mana_jogador2 - mana_invocar
#     print('Card posicionado na mesa de jogo.')
# else:
#     print('Você não pode usar esta carta. Escolha outro card.')


print('Informe o tipo da carta que você deseja buscar:',
      '(1) Druida',
      '(2) Caçador',
      '(3) Mago',
      '(4) Paladino',
      '(5) Xamã')

tipo_carta = input('Digite um número: ')
if tipo_carta == '1':
    tipo_carta = 'Druida'
elif tipo_carta == '2':
    tipo_carta = 'Caçador'
elif tipo_carta == '3':
    tipo_carta = 'Mago'
elif tipo_carta == '4':
    tipo_carta = 'Paladino'
elif tipo_carta == '5':
    tipo_carta = 'Xamã'
else:
    print('Erro, nenhum tipo correspondente')

print('Sua escolha foi: ', tipo_carta)
