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
        return (f"{self.number} - {self.name} - tipos: {', '.join(self.types)} - "
                f"debil frente a: {', '.join(self.weaknesses)} - "
                f"megaevolucion: {'si' if self.mega_evolution else 'no'} - "
                f"gigamax: {'si' if self.gigamax else 'no'}")


# se mezclan los datos para cargarlos de manera aleatoria
for i in range(len(pokemons) - 1, 0, -1):
    j = randint(0, i)
    pokemons[i], pokemons[j] = pokemons[j], pokemons[i]

arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

#A
for pokemon in pokemons:
    pokemon = Pokemon(
        pokemon['nombre'], pokemon['numero'], pokemon['tipos'],
        pokemon['debilidades'], pokemon['megaevolucion'], pokemon['gigamax']
    )
    arbol_nombre.insert_node(pokemon.name, other_value=pokemon)
    arbol_numero.insert_node(pokemon.number, other_value=pokemon)
    for tipo in pokemon.types:
        arbol_tipo.insert_node(tipo, other_value=pokemon)

print(f'cantidad de pokemons cargados {len(pokemons)}')

#B
print()
print('datos de un pokemon por numero')
for numero in [6, 94, 1025]:
    node = arbol_numero.search(numero)
    if node is not None:
        print(node.other_values)
    else:
        print(f'no existe el pokemon numero {numero}')

print()
print('busqueda por proximidad de "bul"')
arbol_nombre.proxy_search_show_all('bul')

#C
for tipo in ['fantasma', 'fuego', 'acero', 'eléctrico']:
    print()
    print(f'pokemons de tipo {tipo}')
    arbol_tipo.show_names_by_value(tipo)

#D
print()
print('listado ascendente por numero')
arbol_numero.inorden_number_name()

print()
print('listado ascendente por nombre')
arbol_nombre.inorden_number_name()

print()
print('listado por nivel por nombre')
arbol_nombre.by_level()

#E
for nombre in ['Jolteon', 'Lycanroc', 'Tyrantrum']:
    node = arbol_nombre.search(nombre)
    if node is not None:
        print()
        print(f'pokemons debiles frente a {nombre} ({", ".join(node.other_values.types)})')
        arbol_nombre.inorden_weak_against(node.other_values.types)

#F
print()
print('tipos de pokemons y cantidad de cada uno')
cantidad_por_tipo = arbol_tipo.count_by_value()
for tipo, cantidad in cantidad_por_tipo.items():
    print(f'{tipo}: {cantidad}')

#G
print()
print(f'cantidad de pokemons con megaevolucion: {arbol_numero.count_mega_evolution()}')

#H
print(f'cantidad de pokemons con forma gigamax: {arbol_numero.count_gigamax()}')
