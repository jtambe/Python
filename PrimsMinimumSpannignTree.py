import collections
import json

# def deep_convert_dict(layer):
#     to_ret = layer
#     if isinstance(layer, collections.OrderedDict):
#         to_ret = dict(layer)
#
#     try:
#         for key, value in to_ret.items():
#             to_ret[key] = deep_convert_dict(value)
#     except AttributeError:
#         pass
#
#     return to_ret
#
# class Vertex:
#     def __init__(self,vertex):
#         self.id = vertex
#         self.edges = [] # vertex has list of edges
#
#     def AddEdge(self, edge):
#         self.edges.append(edge)
#
# class Edge:
#     def __int__(self,source, destination, weight):
#         self.u = source
#         self.v = destination
#         self.weight = weight
#
# class Graph:
#     def __init__(self):
#         self.vertices = [] # graph has list of vertices, and vertex has list of edges
#
#     def AddVertex(self, vertex):
#         self.vertices.append(vertex)

def getWeight(element):

    # print(element)
    # print(element[1])
    for k,v in element[1].items():
            result = k
    return result

def PrimsTree(graph,start):

    auxDict = {}
    for key,value in graph.items():
        auxDict[key] = { float("infinity"): None }

    key = ''
    edges = []
    auxDict[start] = {0:None}

    print("\n")

    # for all vertices in graph
    while len(auxDict) > 0:

        # sort the auxiliary dictionary to get minimum weight vertex edge next
        sortedAux = collections.OrderedDict(sorted(auxDict.items(), key=getWeight)) # sends each item to getWeight as tuple
        # print("sortedAux")
        # print(sortedAux)

        # q = repr(dict(sortedAux))
        # # q = deep_convert_dict(sortedAux)
        # print(q)

        for k,v in sortedAux.items():
            key = k
            parentNode = ''
            for m,q in v.items():
                parentNode = q
            if parentNode: # create edge and append it to result list
                edge = str(key) + str(parentNode)
                edges.append(edge)
            # print("Edges" + str(edges))
            # print(str(key) + " : " + str(value))
            del auxDict[key] # remove a vertex once it is processed
            break

        # print("after removing " + str(key))
        # for k, v in auxDict.items():
        #     print(str(k) + " : " + str(v), end=", ")

        neighbours = graph[key]
        # print("\n Neighbours of " +  str(key) + ": ")
        # print(neighbours)
        for i in range(len(neighbours)):
            if neighbours[i][0] in auxDict:
                Currentweight = 0
                for k,v in auxDict[neighbours[i][0]].items():
                    Currentweight = k
                    break
                if neighbours[i][1] < Currentweight:
                    auxDict[neighbours[i][0]] = { neighbours[i][1]: key } # update the auxiliary dictionary with new values

        # print("\n auxdict after relaxing")
        # for k, v in auxDict.items():
        #     print(str(k) + " : " + str(v), end=", ")
        # print('\n')

    return edges


def main():

    # graph = Graph()

    # e1 = Edge('a', 'b', 3)
    # e2 = Edge('a', 'd', 1)
    # e3 = Edge('b', 'c', 1)
    # e4 = Edge('d', 'c', 1)
    # e5 = Edge('d', 'e', 6)
    # e6 = Edge('c', 'e', 5)
    # e7 = Edge('e', 'f', 2)
    # e8 = Edge('c', 'f', 4)

    # v1 = Vertex('a')
    # v1.AddEdge(e1)
    # v1.AddEdge(e2)

    # v2 = Vertex('b')
    # v2.AddEdge(e1)


    graph = {
                # 'A': [{'B': 16}, {'I': 6 },{'K': 20}]
                'A': [('B', 16), ('I', 6), ('K', 20)],
                'B': [('A', 16), ('C', 1), ('H', 8), ('I', 2)],
                'C': [('B', 1), ('D', 3), ('E', 8)],
                'D': [('C', 3), ('E', 12)],
                'E': [('C', 8), ('D', 12), ('G', 3), ('H', 7)],
                'F': [('J', 28)],
                'G': [('E', 3)],
                'H': [('B', 8), ('E', 7), ('I', 2)],
                'I': [('A', 6), ('J', 19), ('H', 2)],
                'J': [('F', 28), ('I', 19), ('K', 16)],
                'K': [('A', 20), ('J', 16)]
             }

    # for key,value in graph.items():
    #     print(str(key) + " : " + str(value), end='\n')
    
    EdgesInMinimumSpanningtree = PrimsTree(graph,'D')
    print(EdgesInMinimumSpanningtree)

    #
    # x = [{'B': 16}, {'I': 6 },{'K': 20}]
    # print(x)
    # y = sorted(x, key= value)
    # print(y)

    # x = [('B', 16), ('I', 6 ),('K', 20)]
    # y = sorted(x, key= lambda t:t[1])
    # print(y)


if __name__ == "__main__":
    main()
