from edgegraph import GraphEL, VertexEL, EdgeEL
from collections import Counter

def pld_graph(g: GraphEL) -> list:
    if g is None:
        raise ValueError("Bad graph")
    
    #  set of tuples so that they will not be duplicated
    set_tuples = set()
    
    edge_count = Counter()
    for edge in g.edges():
        edge_count[edge.get_value()] += 1
    
    #  return empty if no tuples
    if not set_tuples:
        return []
    
    return list(set_tuples)