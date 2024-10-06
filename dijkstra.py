def dijkstra(graph, source, destination):
    possibleRoutes = []
    visited = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if i == source and graph[i][j] > 0:
                l = list()
                l.append(j)
                possibleRoutes.append(l)
    print(possibleRoutes)
    ...

def main():
    graph = [
        [0, 2, 3, 0],
        [2, 0, 0, 4],
        [3, 0, 0, 2],
        [0, 4, 2, 0]
        ]
    source = 0
    destination = 3
    dijkstra(graph, source, destination)
main()