
from collections import deque

visited = []
Queue = deque([])
TopologicalOrderStack = []

def TopologicalSort(graph):

    global visited
    global Queue
    global TopologicalOrderStack

    for k,v in graph.items():
        Queue.append(k)

    while len(Queue) > 0:
        vertex = Queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            SortUtil(graph, vertex)
            TopologicalOrderStack.append(vertex)

    return TopologicalOrderStack



def SortUtil(graph, v):

    global visited
    global Queue
    global TopologicalOrderStack

    for neighbour in graph[v]:
        if neighbour not in visited:
            visited.append(neighbour)
            SortUtil(graph, neighbour)
            TopologicalOrderStack.append(neighbour)



def main():
    graph = {
        'A':['C'],
        'B':['C','D'],
        'C':['E'],
        'D':['F'],
        'E':['F','H'],
        'F':['G'],
        'H':[],
        'G':[]
    }

    result = TopologicalSort(graph)

    for i in reversed(range(len(result))):
        print(result[i], end=", ")
    # A, B, C, E, D, F, G, H,
    # A, B, D, C, E, H, F, G,

if __name__ == "__main__":
    main()