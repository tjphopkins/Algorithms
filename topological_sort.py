# graph_ex = {
#     'A': set(['B', 'C']),
#     'B': set(['A', 'D', 'E']),
#     'C': set(['A', 'F']),
#     'D': set(['B']),
#     'E': set(['B', 'F']),
#     'F': set(['C', 'E'])
# }

# graph_ex_2 = {
#     'S': set(['V', 'W']),
#     'V': set(['T']),
#     'W': set(['T']),
#     'T': set([])
# }


def dfs_top_sort(graph):
    """Performs a depth-first search and topoligial ordering of a directed,
    acyclic graph.

    Graph must be given in the form:
    {
        'A': set(['B', C']),
        'B': set(['D']),
        'C': set(['D']),
        'D': set([])
    }
    where A to D are vertices and 'A': set(['B']) represents a directed edge
    from A to B.

    A non directed graph can be represented as a directed graph by having two
    oppositely directed edges for each undirected edge.
    """
    visited = set()
    current_label = len(graph.keys())
    top_ordering = {}
    for next_vertex in graph:
        if next_vertex not in visited:
            visited, top_ordering, current_label = \
                _dfs_top_sort_recursion(graph, next_vertex, visited,
                             top_ordering, current_label)

    return visited, top_ordering


def _dfs_top_sort_recursion(
        graph, start_vertex , visited, top_ordering, current_label):
    visited.add(start_vertex)
    for next_vertex in graph[start_vertex] - visited:
        visited, top_ordering, current_label = \
            _dfs_top_sort_recursion(graph, next_vertex, visited,
                         top_ordering, current_label)
    top_ordering[start_vertex] = current_label
    current_label += -1

    return visited, top_ordering, current_label
