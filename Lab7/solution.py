from edgegraph import GraphEL, VertexEL

def bfs(graph: GraphEL, start: VertexEL) -> list:
    if graph is None or start is None:
        raise ValueError("Invalid graph or vertex")
    if start not in graph:
        return []
    pass