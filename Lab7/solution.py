from edgegraph import GraphEL, VertexEL
from collections import deque

def bfs(graph: GraphEL, start: VertexEL) -> list:
    if graph is None or start is None:
        raise ValueError("Invalid graph or vertex")
    if start.name not in graph._vertices:
        return []
    
    queue = deque([start])
    pass