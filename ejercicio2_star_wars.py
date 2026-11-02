from graph import Graph
from star_wars_data import personajes


def show_title(title):
    print('=' * 60)
    print(title)
    print('=' * 60)


def show_min_tree(graph, origin):
    min_tree = graph.kruskal(origin)
    print(f'Kruskal (Árbol de expansión mínimo) desde {origin}:')
    print(min_tree)


def show_shortest_path(graph, origin, destination):
    print(f'De {origin} a {destination}')
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
        print(f'-> Camino: {" - ".join(camino_completo)}')
        print(f'-> Distancia (episodios compartidos): {peso_total}')
    else:
        print(f'-> No existe camino entre {origin} y {destination}')


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

#B
show_title('1. ÁRBOL DE EXPANSIÓN MÍNIMO DESDE C-3PO, YODA Y LEIA')
for origin in ['C-3PO', 'Yoda', 'Leia']:
    show_min_tree(g, origin)
    print()

#C
maximo = 0
for vertex in g:
    for edge in vertex.edges:
        if edge.weight > maximo:
            maximo = edge.weight

show_title('2. NÚMERO MÁXIMO DE EPISODIOS COMPARTIDOS Y PARES')
print(f'El máximo de episodios compartidos es: {maximo}')
print('Personajes que comparten esa cantidad:')
for vertex in g:
    for edge in vertex.edges:
        # el grafo es no dirigido, cada par se muestra una sola vez
        if edge.weight == maximo and vertex.value < edge.destination:
            print(f'* {vertex.value} y {edge.destination}')
print()

#E
show_title('3. CAMINO MÁS CORTO (Dijkstra)')
show_shortest_path(g, 'C-3PO', 'R2-D2')
print()
show_shortest_path(g, 'Yoda', 'Darth Vader')
print()

#F
show_title('4. PERSONAJES QUE APARECIERON EN LOS 9 EPISODIOS')
for vertex in g:
    if len(vertex.other_values) == 9:
        print(f'* {vertex.value}')
