from edgegraph import GraphEL, VertexEL, EdgeEL
from collections import Counter

def pld_graph(g: GraphEL):
    if g is None:
        raise ValueError("Bad graph")
    
    #  set of tuples so that they will not be duplicated
    found_palindromes = set()
    
    for edge in g.edged():
        
    #  return empty if no tuples
    if not found_palindromes:
        return []

    return list(found_palindromes)

#  send the sequence into the helper function
def is_palindrome(s):
    #  check there are at least 3 edeg values
    if len(s) < 3:
        return False

    #  Check if the sequence is same both ways
    return s == s[::-1]

#  traversal function 
def _find_paths_from_edge(g, curr_vertex, path_values, used_edges, found_palindromes):
    #  check curr depth for palindromes
    if is_palindrome(path_values):
        found_palindromes.add(tuple(path_values))
    
    for edge in g.incident(curr_vertex):
        if edge not in used_edges:
            ends = edge.ends()
            v1 = ends[0]
            v2 = ends[1]
            if v1 == curr_vertex:
                next_vertex = v2
            else:
                next_vertex = v1
            
                
    
            