import networkx as nx

g = nx.Graph()
g.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1),
                  (1, 6), (6, 7), (7, 8), (8, 6), (9, 10)])
den = nx.density(g)
numcs = nx.number_connected_components(g)
print(f'плотность графа: {den:.4f}')
print(f'Число связных компонент: {numcs} ')

sn = 1
dfs_pr = nx.dfs_predecessors(g, sn)
print('\n')
print(f"Предшественники при DFS из вершины {sn}: {dfs_pr}")

g2 = nx.complete_graph(5)
s = 2
t = 4
allp = list(nx.all_simple_paths(g2, s, t))
print('\n')
print(f"Все простые пути из вершины {s} в вершину {t} в полносвязном графе:")
for p in allp:
    print(f'{p}')
