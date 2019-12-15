from Chapter8.Dijkstra.DecreaseKey.Graph import Graph

graph = Graph()

graph.addVertex("START")
graph.addVertex("A")
graph.addVertex("C")
graph.addVertex("B")
graph.addVertex("D")
graph.addVertex("END")


graph.addEdge("START", "A", 0)
graph.addEdge("START", "C", 1)
graph.addEdge("A", "B", 20)
graph.addEdge("A", "D", 10)
graph.addEdge("C", "B", 1)
graph.addEdge("C", "D", 8)
graph.addEdge("B", "END", 100)
graph.addEdge("D", "END", 15)
graph.dijkstra("START", "END")