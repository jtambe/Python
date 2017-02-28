'''
This is Kosaraju''s algorithm to find SCC
credits:
https://www.youtube.com/watch?v=RpgcYiky7uw - Tushar Roy
'''
import numpy

# d = numpy.empty((9, 0)).tolist()
# for i in range(9):
#     print(d[i])
# print(d)
# d = [[] for x in range(9)]
# print(d)
# for i in range(9):
#     print(d[i])

from collections import deque # to use list as a queue

class vertex:

    def __int__(self):
        self.id = None
        self.color = None
        self.discoverTime = None
        self.finishingTime = None

# auxiliary list for DFS
vertexList = []
# discovery and finishing time in DFS
time = 0
# stack of vertices in decreasing finishing time as explained in algorithm
VerticesStack = []

# created dictionary of strongly connected components
# i is auxiliary variable used to created list of nodes in each Strongly connected components
i = 0
SCC = {}


def DFS(graph):
    # for k in graph:
    #     print(str(k) + " : "+str(graph[k]))

    global time
    time = 0
    for k in graph:
        v = vertex()
        v.id = k
        v.color = "white"
        v.discoverTime = None
        v.finishingTime = None
        vertexList.append(v)

    # for node in vertexList:
    #     print(str(node.id) + ": " + str(node.color) + " discoverTime : " + str(node.discoverTime) +
    #           " finishingTime : " + str(node.finishingTime))

    for k in graph:
        if vertexList[k].color == "white":
            DFSVisit(graph, k)

def DFSVisit(graph, u):
    global time
    time += 1
    vertexList[u].discoverTime = time
    vertexList[u].color = "gray"

    for neighbour in graph[u]:
        if vertexList[neighbour].color == "white":
            DFSVisit(graph, neighbour)

    vertexList[u].color = "black"
    time += 1
    vertexList[u].finishingTime = time
    global VerticesStack
    VerticesStack.append(u)


# DFS of reverse Graph using stack of nodes in decreasing order of finishing time
def ReverseGraphDFS(reverseGraph):
    # for k in graph:
    #     print(str(k) + " : "+str(graph[k]))

    global  vertexList
    vertexList = []

    global time
    time = 0

    for k in reverseGraph:
        v = vertex()
        v.id = k
        v.color = "white"
        v.discoverTime = None
        v.finishingTime = None
        vertexList.append(v)

    # for node in vertexList:
    #     print(str(node.id) + ": " + str(node.color) + " discoverTime : " + str(node.discoverTime) +
    #           " finishingTime : " + str(node.finishingTime))

    global  VerticesStack
    global i
    global SCC

    while(len(VerticesStack) > 0):
        k = VerticesStack.pop()
        if vertexList[k].color == "white":
            i += 1
            SCC[i] = []
            SCC[i].append(k)
            ReverseGraphDFSVisit(reverseGraph, k)

def ReverseGraphDFSVisit(reverseGraph, u):
    global time
    global i
    global SCC
    time += 1
    vertexList[u].discoverTime = time
    vertexList[u].color = "gray"

    for neighbour in reverseGraph[u]:
        if vertexList[neighbour].color == "white":
            SCC[i].append(neighbour)
            ReverseGraphDFSVisit(reverseGraph, neighbour)

    vertexList[u].color = "black"
    time += 1
    vertexList[u].finishingTime = time



# function to reverse a given DAG
def ReverseDAG(graph):

    newGraph = {}


    for k in graph:
        # print(graph[k])
        for item in (graph[k]):
            # print(item, end=",")
            if item in newGraph:
                newGraph[item].append(k)
            else:
                newGraph[item] = []
                newGraph[item].append(k)

    for k in graph:
        if k not in newGraph:
            newGraph[k] = []

    return newGraph



def main():
    graph = {0:[1,2], 1:[2], 2:[0,1]}
    graph = {0: [1], 1: [2], 2: [0,3], 3: [4], 4: [5], 5: [6], 6: [3], 7: [6]}
    # print(graph)

    DFS(graph)

    #print(VerticesStack)

    reverseGraph = ReverseDAG(graph)

    ReverseGraphDFS(reverseGraph)

    global SCC
    print(SCC)

    # for node in vertexList:
    #     print(str(node.id) + ": " + str(node.color) + " discoverTime : " + str(node.discoverTime) +
    #           " finishingTime : " + str(node.finishingTime))

    # print(VerticesStack)



if __name__ == "__main__":
    main()
