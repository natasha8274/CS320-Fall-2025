from edgegraph import GraphEL, VertexEL, EdgeEL

def pld_graph(g: GraphEL) -> list:
    if g is None:
        raise ValueError("Bad graph")
    
    #  set of tuples so that they will not be duplicated
    tuples = set()
    # tuples lis to be returned at the end
    list_tuples = []
    
    #  return empty if no tuples
    if not list_tuples:
        return []
    
    return list_tuples