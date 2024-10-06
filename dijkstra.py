def dijkstra(graph, source, destination):
    possibleRoutes = []
    unvisited = list(graph.keys())
    for l in graph[source]:
        initialLinks = list()
        initialLinks.append(l)
        possibleRoutes.append(initialLinks)
    unvisited.remove(source)
    
    for node in unvisited:
        for link in graph[node]:
            print(link)
            # if node[0] in unvisited:
            #     possibleRoutes[i].append(node)
            #     if node[0] != destination:
            #         unvisited.remove(node[0])
            #     if node == source:
            #         ...
            #     ...
        ...
    ...
    print(possibleRoutes)

def main():
    graph = {'A':[('B',2),('C',3)],
            'B':[('A',2),('D',4)],
            'C':[('A',3),('D',2)],
            'D':[('B',4),('C',2)]}
    source = 'A'
    destination = 'D'
    dijkstra(graph, source, destination)
main()