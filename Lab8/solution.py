from edgegraph import GraphEL, VertexEL, EdgeEL
from collections import Counter


def pld_graph(g: GraphEL):
    if g is None:
        raise ValueError("Bad graph")

    found_palindromes = set()

    value_counts = Counter(edge.get_value() for edge in g.edges())

    for edge in g.edges():
        v1, v2 = edge.ends()
        path_value = edge.get_value()

        #  traversal helper method for v1 start
        _find_paths_from_edge(v1, [path_value], {edge}, found_palindromes, value_counts)
    
        #  traversal helper method for v2 start
        _find_paths_from_edge(v2, [path_value], {edge}, found_palindromes, value_counts)

    #  return empty if no tuples
    if not found_palindromes:
        return []

    return sorted(found_palindromes)


#  send the sequence into the helper function
def is_palindrome(seq):
    #  check there are at least 3 edeg values
    if len(seq) < 3:
        return False

    return seq == seq[::-1]


#  Helper function to search for curr vertex and detect palindromes
def _find_paths_from_edge(curr_vertex, path_values, used_edges, found_palindromes, value_counts):
    n = len(path_values)
    for i in range(n - 2):
        subsequence = path_values[i:]
        if is_palindrome(subsequence):
            found_palindromes.add(tuple(subsequence))
        
    #  singleton pruning optimization check and if latest is singleton
    latest_value = path_values[-1]
    if value_counts[latest_value] == 1:
        mid = n // 2
        if n % 2 == 0 or path_values[mid] != latest_value:
            return

    for edge in g.incident(curr_vertex):
        if edge not in used_edges:
            v1, v2 = edge.ends[0]
            if v1 == curr_vertex:
                next_vertex = v2
            else:
                next_vertex = v1

            _find_paths_from_edge(next_vertex, 
                                  path_values + [edge.get_values()], 
                                  used_edges | {edge}, 
                                  found_palindromes, 
                                  value_counts)
