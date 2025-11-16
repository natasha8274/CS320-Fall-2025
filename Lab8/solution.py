from edgegraph import GraphEL, VertexEL, EdgeEL
from collections import Counter


def pld_graph(g: GraphEL):
    if g is None:
        raise ValueError("Bad graph")

    found_palindromes = set()

    edge_values = [edge.get_value() for edge in g.edges()]
    value_counts = Counter(edge_values)

    for start_edge in g.edges():
        v1, v2 = start_edge.ends()
        edge_value = start_edge.get_value()

        #  traversal helper method for v1 start
        _find_paths_from_edge(g, v2, [edge_value], {start_edge}, found_palindromes, value_counts)
    
        #  traversal helper method for v2 start
        _find_paths_from_edge(g, v1, [edge_value], {start_edge}, found_palindromes, value_counts)

    #  return empty if no tuples
    if not found_palindromes:
        return []

    return list(found_palindromes)

#  send the sequence into the helper function
def is_palindrome(seq):
    #  check there are at least 3 edeg values
    if len(seq) < 3:
        return False

    return seq == seq[::-1]

#  Helper function to search for curr vertex and detect palindromes
def _find_paths_from_edge(g, curr_vertex, path_values, used_edges, found_palindromes, value_counts):
    #  check curr depth for palindromes
    if is_palindrome(path_values):
        found_palindromes.add(tuple(path_values))
        
    #  singleton pruning optimization check 
    latest_value = path_values[-1]
    length = len(path_values)
    
    #  check if latest is a singleton
    if value_counts[latest_value] == 1:
        if length % 2 == 0 or latest_value != path_values[length // 2]:
            #  pruning the branch, can no longer form a longer palindrome
            return

    for edge in g.incident(curr_vertex):
        if edge not in used_edges:
            ends = edge.ends()
            v1 = ends[0]
            v2 = ends[1]
            if v1 == curr_vertex:
                next_vertex = v2
            else:
                next_vertex = v1
                
            new_used_edges = used_edges.copy()
            new_used_edges.add(edge)
            
            new_path_values = path_values + [edge.get_value()]

            _find_paths_from_edge(g, next_vertex, new_path_values, new_used_edges, found_palindromes, value_counts)
