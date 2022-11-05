pokedex = ['Bulbasaur', 'Charmander', 'Squirtle', "Butterfree", 'Pikachu']

print(len(pokedex))
print(f'{pokedex[2]} eu escolho você!')

print(pokedex[1:4])
print(f' Último pokemon na pokedex é o {pokedex[-1]}')


card_deck = []
card_deck.append('Pikachu')
card_deck.append('Charmander')
print(len(card_deck))


for pokemon in pokedex:
    print(f'{pokemon} está na sua pokedex.')
else:
    print('Esses são todos os pokemons!')

print('Vamos mosntar o seu novo deck de pokemons')
inserir = '1'
novo_deck = []

while inserir == '1':
    novo_card = input('Qual o nome do pokemon: ')
    novo_deck.append(novo_card)
    inserir = input('Deseja inserir um novo?(1) sim (0) não:')
print(f'Seu novo deck tem {len(novo_deck)} cards')
