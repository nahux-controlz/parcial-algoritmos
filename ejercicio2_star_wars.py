from graph import Graph

# personaje y episodios de la saga (I a IX) en los que aparece
personajes = [
    {"nombre": "Luke Skywalker", "episodios": [3, 4, 5, 6, 7, 8, 9]},
    {"nombre": "Darth Vader", "episodios": [1, 2, 3, 4, 5, 6]},
    {"nombre": "Yoda", "episodios": [1, 2, 3, 5, 6, 8]},
    {"nombre": "Boba Fett", "episodios": [2, 5, 6]},
    {"nombre": "C-3PO", "episodios": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
    {"nombre": "Leia", "episodios": [3, 4, 5, 6, 7, 8, 9]},
    {"nombre": "Rey", "episodios": [7, 8, 9]},
    {"nombre": "Kylo Ren", "episodios": [7, 8, 9]},
    {"nombre": "Chewbacca", "episodios": [3, 4, 5, 6, 7, 8, 9]},
    {"nombre": "Han Solo", "episodios": [4, 5, 6, 7, 9]},
    {"nombre": "R2-D2", "episodios": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
    {"nombre": "BB-8", "episodios": [7, 8, 9]},
    {"nombre": "Obi-Wan Kenobi", "episodios": [1, 2, 3, 4, 5, 6]},
    {"nombre": "Palpatine", "episodios": [1, 2, 3, 6, 9]},
    {"nombre": "Padmé Amidala", "episodios": [1, 2, 3]},
    {"nombre": "Lando Calrissian", "episodios": [5, 6, 9]},
    {"nombre": "Finn", "episodios": [7, 8, 9]},
    {"nombre": "Poe Dameron", "episodios": [7, 8, 9]},
]


def show_min_tree(graph, origin):
    min_tree = graph.kruskal(origin)
    peso_total = 0
    print(f'arbol de expansion minimo desde {origin}')
    for edge in min_tree.split(';'):
        origin_edge, destination_edge, weight = edge.split('/')
        print(f'origin {origin_edge} destination {destination_edge} episodios {weight}')
        peso_total += int(weight)
    print(f'peso total: {peso_total}')


def show_shortest_path(graph, origin, destination):
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
        print(f'el camino mas corto es: {" -> ".join(camino_completo)} con un costo de {peso_total}')
    else:
        print(f'no existe camino entre {origin} y {destination}')


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

g.show()

#B
for origin in ['C-3PO', 'Yoda', 'Leia']:
    print()
    show_min_tree(g, origin)

#C
maximo = 0
for vertex in g:
    for edge in vertex.edges:
        if edge.weight > maximo:
            maximo = edge.weight

print()
print(f'numero maximo de episodios que comparten dos personajes: {maximo}')
for vertex in g:
    for edge in vertex.edges:
        # el grafo es no dirigido, cada par se muestra una sola vez
        if edge.weight == maximo and vertex.value < edge.destination:
            print(f'{vertex.value} - {edge.destination}')

#E
print()
print('camino mas corto desde C-3PO a R2-D2')
show_shortest_path(g, 'C-3PO', 'R2-D2')
print()
print('camino mas corto desde Yoda a Darth Vader')
show_shortest_path(g, 'Yoda', 'Darth Vader')

#F
print()
print('personajes que aparecieron en los nueve episodios')
for vertex in g:
    if len(vertex.other_values) == 9:
        print(vertex.value)
