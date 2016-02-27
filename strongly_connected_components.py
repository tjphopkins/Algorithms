from collections import defaultdict

# graph_ex = {
#     1: set([4]),
#     2: set([8]),
#     3: set([6]),
#     4: set([7]),
#     5: set([2]),
#     6: set([9]),
#     7: set([1]),
#     8: set([5, 6]),
#     9: set([3, 7])
# }

def dfs_strong_connect(graph):
    """Given a directed graph, returns a list of its strongly connected
    components.

    Nodes of graph must be labelled by integers from 1 to the number of nodes.

    e.g. the following is a valid input:
    {
        1: set([4]),
        2: set([8]),
        3: set([6]),
        4: set([7]),
        5: set([2]),
        6: set([9]),
        7: set([1]),
        8: set([5, 6]),
        9: set([3, 7])
    }
    """

    graph_rev = defaultdict(set)
    for node, edges in graph.items():
        for edge in edges:
            if node not in graph_rev[edge]:
                graph_rev[edge].add(node)

    # first pass on reversed graph
    visited, finishing_times, leaders = _dfs_strong_connect_pass(graph_rev)
    # from finishing_times, calculate order in which to process nodes in
    # second pass on graph
    order_of_nodes = []
    for finishing_time in range(len(graph.keys()), 0, -1):
        order_of_nodes.append(finishing_times[finishing_time])
    # second pass on graph
    visited, finishing_times, leaders = \
        _dfs_strong_connect_pass(graph, order_of_nodes=order_of_nodes)

    sccs = []
    for leader, scc in leaders.items():
        sccs.append(scc)

    return sccs


def _dfs_strong_connect_pass(graph, order_of_nodes=None):
    """
    Returns:

    * list of visited nodes
    * dict of finishing times of nodes in the form:
        {
            1: <node with finishing time = 1>,
            2: <node with finishing time = 2>,
            ...
            number_of_nodes: <node with finishing time = number of nodes>
        }
    * dict mapping leader nodes to child nodes
    """
    visited = set()
    num_processed_nodes = 0
    source_node = None
    finishing_times = {}
    leaders = defaultdict(list)

    if not order_of_nodes:
        order_of_nodes = range(len(graph.keys()), 0, -1)

    for next_node in order_of_nodes:
        if next_node not in visited:
            source_node = next_node
            visited, num_processed_nodes, finishing_times, leaders = \
                _dfs_strong_connect_recursion(
                    graph, next_node, visited, num_processed_nodes,
                    source_node, finishing_times, leaders
                )

    return visited, finishing_times, leaders


def _dfs_strong_connect_recursion(
        graph, start_node, visited, num_processed_nodes, source_node,
        finishing_times, leaders):
    visited.add(start_node)
    leaders[source_node].append(start_node)
    for next_node in graph[start_node] - visited:
        visited, num_processed_nodes, finishing_times, leaders = \
            _dfs_strong_connect_recursion(
                graph, next_node, visited, num_processed_nodes,
                source_node, finishing_times, leaders
            )

    num_processed_nodes += 1
    finishing_times[num_processed_nodes] = start_node

    return visited, num_processed_nodes, finishing_times, leaders
