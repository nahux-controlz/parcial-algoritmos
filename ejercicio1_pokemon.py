from random import randint

from pokemon_data import pokemons
from tree import BinaryTree


class Pokemon():

    def __init__(self, nombre, numero, tipos, debilidades, megaevolucion, gigamax):
        self.name = nombre
        self.number = numero
        self.types = tipos
        self.weaknesses = debilidades
        self.mega_evolution = megaevolucion
        self.gigamax = gigamax

    def __str__(self):
        types = ', '.join(self.types)
        weaknesses = ', '.join(self.weaknesses)
        mega = 'Sí' if self.mega_evolution else 'No'
        gigamax = 'Sí' if self.gigamax else 'No'
        return f'{self.number:>5}  {self.name:<13}{types:<21}{weaknesses:<51}{mega:<6}{gigamax}'


TABLE_HEADER = f'{"N°":>5}  {"Nombre":<13}{"Tipos":<21}{"Débil frente a":<51}{"Mega":<6}Gigamax'


def show_title(title):
    print()
    print(title)
    print('-' * len(title))


def show_table(values):
    print(TABLE_HEADER)
    for pokemon in values:
        print(pokemon)


def show_in_columns(values, columns=5, width=19):
    for i in range(0, len(values), columns):
        line = ''
        for value in values[i:i + columns]:
            line += f'{value:<{width}}'
        print('  ' + line.rstrip())


# se mezclan los datos para cargarlos de manera aleatoria
for i in range(len(pokemons) - 1, 0, -1):
    j = randint(0, i)
    pokemons[i], pokemons[j] = pokemons[j], pokemons[i]

arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

for pokemon in pokemons:
    pokemon = Pokemon(
        pokemon['nombre'], pokemon['numero'], pokemon['tipos'],
        pokemon['debilidades'], pokemon['megaevolucion'], pokemon['gigamax']
    )
    arbol_nombre.insert_node(pokemon.name, other_value=pokemon)
    arbol_numero.insert_node(pokemon.number, other_value=pokemon)
    for tipo in pokemon.types:
        arbol_tipo.insert_node(tipo, other_value=pokemon)

print('EJERCICIO 1 - POKÉMONS')
print(f'Pokémons cargados: {len(pokemons)}')

show_title('Búsqueda por número: 6, 94 y 1025')
encontrados = []
for numero in [6, 94, 1025]:
    node = arbol_numero.search(numero)
    if node is not None:
        encontrados.append(node.other_values)
    else:
        print(f'No existe el Pokémon número {numero}')
show_table(encontrados)

show_title('Búsqueda por proximidad: "bul"')
show_table(arbol_nombre.proxy_search_values('bul'))

show_title('Pokémons de tipo fantasma, fuego, acero y eléctrico')
for tipo in ['fantasma', 'fuego', 'acero', 'eléctrico']:
    nombres = arbol_tipo.names_by_value(tipo)
    print()
    print(f'{tipo.capitalize()} ({len(nombres)}):')
    show_in_columns(nombres)

show_title('Listado ascendente por número')
listado = []
for pokemon in arbol_numero.inorden_values():
    listado.append(f'{pokemon.number:>4}  {pokemon.name}')
show_in_columns(listado)

show_title('Listado ascendente por nombre')
listado = []
for pokemon in arbol_nombre.inorden_values():
    listado.append(f'{pokemon.name} ({pokemon.number})')
show_in_columns(listado)

show_title('Listado por nivel por nombre')
niveles = arbol_nombre.by_level_grouped()
for i in range(len(niveles)):
    print(f'Nivel {i + 1} ({len(niveles[i])}):')
    show_in_columns(niveles[i])

show_title('Pokémons débiles frente a Jolteon, Lycanroc y Tyrantrum')
for nombre in ['Jolteon', 'Lycanroc', 'Tyrantrum']:
    node = arbol_nombre.search(nombre)
    if node is not None:
        tipos = node.other_values.types
        debiles = arbol_nombre.weak_against(tipos)
        print()
        print(f'Frente a {nombre} ({", ".join(tipos)}): {len(debiles)} Pokémons')
        show_in_columns(debiles)

show_title('Cantidad de Pokémons por tipo')
for tipo, cantidad in arbol_tipo.count_by_value().items():
    print(f'  {tipo:<12}{cantidad:>3}')

show_title('Megaevolución y forma Gigamax')
print(f'  Con megaevolución: {arbol_numero.count_mega_evolution()}')
print(f'  Con forma Gigamax: {arbol_numero.count_gigamax()}')
