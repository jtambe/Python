from collections import deque # to use list as a queue

class vertex:

    def __int__(self):
        self.id = None
        self.color = None
        self.discoverTime = None
        self.finishingTime = None


vertexList = []
time = 0


def DFS(graph):

    for k in graph:
        print(str(k) + " : "+str(graph[k]))

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



def main():
    graph = {0:[1,2], 1:[2], 2:[0,1]}
    print(graph)
    # for node in (graph["2"]):
    #     print(node)
    DFS(graph)
    #DFS(graph, 1)

    for node in vertexList:
        print(str(node.id) + ": " + str(node.color) + " discoverTime : " + str(node.discoverTime) +
              " finishingTime : " + str(node.finishingTime))


if __name__ == "__main__":
    main()