novo_deck = []


def inserir_novo():
    novo = input('qual o nome do pokemon: ')
    if verificar(novo):
        novo_deck.append(novo)
    else:
        print('Este card já existe no deck')


inserir_novo()
print(len(novo_deck))


def mostrar_deck():
    print(f'seu novo deck tem {len(novo_deck)}')
    print(novo_deck)


mostrar_deck()


def verificar(pokemon):
    if pokemon in novo_deck:
        return False
    else:
        return True


verificar()
