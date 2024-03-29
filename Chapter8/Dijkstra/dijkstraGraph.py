from Chapter8.bfs.Vertex import Vertex
from Chapter8.bfs.Graph import Graph
from Chapter8.Dijkstra.prioQue import PriorityQueue

def dijkstra(aGraph, start):

    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in aGraph])

    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.getDistance(newDist)
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert, newdist)
