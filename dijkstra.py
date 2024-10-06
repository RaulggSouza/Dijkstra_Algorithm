def dijkstra(graph, source, destination):
    possibleRoutes = []
    unvisited = list(graph.keys())
    for link in graph.values():
        for node in link:
            if node[0] not in unvisited:
                ...
        ...
    ...

def main():
    graph = {'A':[('B',2),('C',3)],
            'B':[('A',2),('D',4)],
            'C':[('A',3),('D',2)],
            'D':[('B',4),('C',2)]}
    source = 0
    destination = 3
    dijkstra(graph, source, destination)
main()