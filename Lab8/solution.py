from edgegraph import GraphEL, VertexEL, EdgeEL
from collections import Counter


def pld_graph(g: GraphEL):
    if g is None:
        raise ValueError("Bad graph")

    found_palindromes = set()
    
    #  get all edge value counts for the optimization
    
    def _find_paths_from_edge(curr_vertex, path_list, used_edges_set):
        #  check if the entire path is a palindrome
        if is_palindrome(path_list):
            found_palindromes.add(tuple(path_list))

        #  loop through all connecting edges 
        for edge in g.incident(curr_vertex):
            if edge not in used_edges_set:
                edge_value = edge.get_value()

                v1, v2 = edge.ends()
                if v1 == curr_vertex:
                    next_vertex = v2
                else:
                    next_vertex = v1

                path_list.append(edge_value)
                used_edges_set.add(edge)

                _find_paths_from_edge(
                    next_vertex,
                    path_list,
                    used_edges_set
                )
                used_edges_set.remove(edge)
                path_list.pop()

    for edge in g.edges():
        v1, v2 = edge.ends()
        path_value = edge.get_value()
        path = [path_value]
        used = {edge}

        #  traversal helper method for v1 start
        _find_paths_from_edge(v1, path, used)
    
        #  traversal helper method for v2 start
        _find_paths_from_edge(v2, path, used)

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
