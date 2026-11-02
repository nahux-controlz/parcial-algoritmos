from graph import Graph
from star_wars_data import personajes


def show_title(title):
    print()
    print(title)
    print('-' * len(title))


def show_min_tree(min_tree):
    peso_total = 0
    print(f'  {"Personaje":<20}{"Personaje":<20}Episodios juntos')
    for edge in min_tree.split(';'):
        origin, destination, weight = edge.split('/')
        print(f'  {origin:<20}{destination:<20}{weight:>9}')
        peso_total += int(weight)
    print(f'  Peso total del árbol: {peso_total}')


def show_shortest_path(graph, origin, destination):
    title = f'{origin} a {destination}:'
    if graph.exist_path(origin, destination):
        paths = graph.dijkstra(origin)
        peso_total = None
        camino_completo = []

        while paths.size() > 0:
            value = paths.pop()
            if value[0] == destination:
                if peso_total is None:
                    peso_total = value[1]
                camino_completo.append(value[0])
                destination = value[2]
        camino_completo.reverse()
        print(f'  {title:<22}{" -> ".join(camino_completo)}  (costo: {peso_total} episodios)')
    else:
        print(f'  {title:<22}no existe camino')


g = Graph(is_dir=False)

for personaje in personajes:
    g.add_vertex(personaje['nombre'], personaje['episodios'])

# la arista entre dos personajes es la cantidad de episodios en los que aparecieron juntos
for i in range(len(personajes)):
    for j in range(i + 1, len(personajes)):
        episodios_juntos = 0
        for episodio in personajes[i]['episodios']:
            if episodio in personajes[j]['episodios']:
                episodios_juntos += 1
        if episodios_juntos > 0:
            g.add_edge(episodios_juntos, personajes[i]['nombre'], personajes[j]['nombre'])

print('EJERCICIO 2 - GRAFO DE PERSONAJES DE STAR WARS')
print(f'Personajes cargados: {len(g)}')

show_title('Árbol de expansión mínimo (Kruskal) desde C-3PO, Yoda y Leia')
origenes = ['C-3PO', 'Yoda', 'Leia']
arboles = []
for origen in origenes:
    arboles.append(g.kruskal(origen))

if arboles[0] == arboles[1] == arboles[2]:
    print('Desde los tres vértices se obtiene el mismo árbol, porque todos los personajes están conectados.')
    print()
    show_min_tree(arboles[0])
else:
    for i in range(len(origenes)):
        print()
        print(f'Desde {origenes[i]}:')
        show_min_tree(arboles[i])

maximo = 0
for vertex in g:
    for edge in vertex.edges:
        if edge.weight > maximo:
            maximo = edge.weight

show_title('Máximo de episodios compartidos')
print(f'El máximo es {maximo} episodios y lo comparten:')
for vertex in g:
    for edge in vertex.edges:
        # el grafo es no dirigido, cada par se muestra una sola vez
        if edge.weight == maximo and vertex.value < edge.destination:
            print(f'  {vertex.value} y {edge.destination}')

show_title('Camino más corto (Dijkstra)')
show_shortest_path(g, 'C-3PO', 'R2-D2')
show_shortest_path(g, 'Yoda', 'Darth Vader')

show_title('Personajes que aparecieron en los nueve episodios')
for vertex in g:
    if len(vertex.other_values) == 9:
        print(f'  {vertex.value}')
