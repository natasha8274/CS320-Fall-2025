from edgegraph import GraphEL, VertexEL, EdgeEL
from collections import Counter


def pld_graph(g: GraphEL):
    if g is None:
        raise ValueError("Bad graph")

    found_palindromes = set()

    value_counts = Counter(edge.get_value() for edge in g.edges())
    
    def _find_paths_from_edge(curr_vertex, path_values, used_edges):
        #  check if the entire path is a palindrome
        if is_palindrome(path_values):
            found_palindromes.add(tuple(path_values))
            
        #  singleton pruning optimization check and if latest is singleton
        n = len(path_values)
        latest_value = path_values[-1]
        if value_counts[latest_value] == 1:
            # Only prune if the path length is odd
            if n % 2 != 0:
                mid = n // 2
                #  and if singleton is not midd element
                if path_values[mid] != latest_value:
                    return

        for edge in g.incident(curr_vertex):
            if edge not in used_edges:
                v1, v2 = edge.ends()
                if v1 == curr_vertex:
                    next_vertex = v2
                else:
                    next_vertex = v1

                _find_paths_from_edge(
                    next_vertex,
                    path_values + [edge.get_value()],
                    used_edges | {edge}
                )

    for edge in g.edges():
        v1, v2 = edge.ends()
        path_value = edge.get_value()

        #  traversal helper method for v1 start
        _find_paths_from_edge(v1, [path_value], {edge})
    
        #  traversal helper method for v2 start
        _find_paths_from_edge(v2, [path_value], {edge})

    #  return empty list if no tuples
    if not found_palindromes:
        return []

    return list(found_palindromes)


#  send the sequence into the helper function
def is_palindrome(seq):
    #  check there are at least 3 edeg values
    if len(seq) < 3:
        return False

    return seq == seq[::-1]
