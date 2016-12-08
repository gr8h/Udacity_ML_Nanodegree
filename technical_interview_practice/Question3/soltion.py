import heapq
import sys


def question3(G, start=None):

    if not G or G == [[]]:
        return

    # heap
    pq = []
    # store vertex to edge
    vertexToEdge = {}
    # final result MST
    result = []

    # set the start vertex
    for vertex in G:
        if start is None or vertex == start:
            heapq.heappush(pq, (0, vertex))
            start = vertex
        else:
            heapq.heappush(pq, (sys.maxsize, vertex))

    # create a dic for easy lookup
    pq_lookup = dict([(v, w) for (w, v) in pq])

    # while heap is not empty
    while pq:
        # get the edge with the min weight
        current_w, current_v = heapq.heappop(pq)
        del pq_lookup[current_v]

        # if the current edge is in vertexToEdge then this is our min edge
        if current_v in vertexToEdge:
            result.append(vertexToEdge[current_v])

        # get the current edge neighbors
        for edge_v, edge_w in G[current_v]:
            # check if the this neighbor edge in our heap and its weight is less that the current value
            if edge_v in pq_lookup and pq_lookup[edge_v] > edge_w:
                # update the heap with the new min weight
                updateHeap(pq, pq_lookup, edge_v, edge_w)
                # add this edge to vertexToEdge
                vertexToEdge[edge_v] = (current_v, edge_v)

    return result


def updateHeap(pq, pq_lookup, vertex, weight):
    for i in range(len(pq)):
        w, v = pq[i]
        if v == vertex:
            del pq[i]
            break
    pq_lookup[vertex] = weight
    heapq.heappush(pq, (weight, vertex))


G = {'A': [('B', 2)],
     'B': [('A', 2), ('C', 5)],
     'C': [('B', 5)]}

print question3(G)
# [('A', 'B'), ('B', 'C')]

G = dict(A=[('D', 1), ('B', 3)],
         B=[('A', 3), ('D', 3), ('C', 1)],
         C=[('B', 1), ('D', 1), ('E', 5), ('F', 4)],
         D=[('A', 1), ('B', 3), ('C', 1), ('E', 6)],
         E=[('D', 6), ('C', 5), ('F', 2)],
         F=[('E', 2), ('C', 4)])

print question3(G)
# [('A', 'D'), ('D', 'C'), ('C', 'B'), ('C', 'F'), ('F', 'E')]

G = {'A': [('D', 2)],
     'B': [('E', 2), ('H', 5)],
     'C': [('F', 5)]}

print question3(G)
# []

G = {}

print question3(G)
# []