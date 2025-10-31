from edgegraph import GraphEL, VertexEL
from collections import deque

def bfs(graph: GraphEL, start: VertexEL) -> list:
    if graph is None or start is None:
        raise ValueError("Invalid graph or vertex")
    if start.name not in graph._vertices:
        return []

    #  queue to track the traversal
    queue = deque([start])
    #  the visited/explored vertices
    explored = {start}
    #  list of tuples to be returned at the end
    list_tuples = []
    #  groups vertices that are the same numer of hops from vertex
    current_level_list = [start]

    while queue:
        list_tuples.append(tuple(current_level_list))
        current_level_size = len(queue)
        next_level_list = []
        for _ in range (current_level_size):
            u = queue.popleft()
            #  gets all vertices adjacent to u while maintining time complexity 
            neighbors = graph.adjacent(u)


    pass