import networkx as nx
g = nx.Graph()
g.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (4, 5), (5, 6)])
g.add_node(7)
g.add_edges_from([(8, 9)])
print(f'Число вершин: {g.number_of_nodes()}')
print(f'Число рёбер: {g.number_of_edges()}')

cts = list(nx.connected_components(g))
maxc = max(cts, key=len)
gmax = g.subgraph(maxc)
r = nx.radius(gmax)
d = nx.diameter(gmax)
print('\n')
print(f'Радиус главной компоненты: {r}')
print(f'Диаметр главной компоненты: {d}')

shpt = dict(nx.all_pairs_shortest_path_length(g))
print('\n')
print('Длины кратчайших путей между всеми парами вершин: ')
for s, dd in shpt.items():
    for t, d in dd.items():
        if s != t:
            print(f'{s} -> {t}: {d}')
