'''A graph is a set of vertices and edges that form connections between the vertices. In a more formal approach,
a graph G is an ordered pair of a set V of vertices and a set E of edges given as G = (V, E) in formal mathematical notation.
Undirected Graphs
Directed Graphs
Weighted Graphs'''

'''Graphs can be represented in two main forms. One way is to use an adjacency matrix and the other is to use an adjacency list.'''

#Adjacency List
graph = dict()
graph['A'] = ['B','C']
graph['B'] = ['E','A']
graph['C'] = ['A','B','E','F']
graph['E'] = ['B','C']
graph['F'] = ['C']

#Adjancey Matrix
matrix_elements = sorted(graph.keys())
cols = rows = len(matrix_elements)
adjancency_matrix = [[0 for x in range(rows)] for y in range(cols)]
edges_list = []
for key in matrix_elements:
    for neighbour in graph[key]:
        edges_list.append((key,neighbour))

print(edges_list)
#[('A', 'B'), ('A', 'C'), ('B', 'E'), ('B', 'A'), ('C', 'A'), ('C', 'B'), ('C', 'E'), ('C', 'F'), ('E', 'B'), ('E', 'C'), ('F', 'C')]

for edge in edges_list:
    index_of_first_vertex = matrix_elements.index(edge[0])
    index_of_second_vertex = matrix_elements.index(edge[1])
    adjancency_matrix[index_of_first_vertex][index_of_second_vertex] = 1

print(adjancency_matrix)
#[[0, 1, 1, 0, 0], [1, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 1, 1, 0, 0], [0, 0, 1, 0, 0]]