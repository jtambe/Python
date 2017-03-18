import collections

def getWeight(element):
    for k,v in element[1].items():
            result = k
    return result

def PrimsTree(graph,start):

    auxDict = {}
    ShortestPathWeights = {}
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

        for k,v in sortedAux.items():
            key = k
            parentNode = ''
            distance = 0
            for m,q in v.items():
                parentNode = q
                distance = m

            ShortestPathWeights[key] = distance

            if parentNode: # create edge and append it to result list
                edge = str(key) + str(parentNode)
                edges.append(edge)
            del auxDict[key] # remove a vertex once it is processed
            break

        neighbours = graph[key]
        for i in range(len(neighbours)):
            if neighbours[i][0] in auxDict:
                Currentweight = 0
                for k,v in auxDict[neighbours[i][0]].items():
                    Currentweight = k
                    break
                if neighbours[i][1] + ShortestPathWeights[key] < Currentweight:
                    auxDict[neighbours[i][0]] = { neighbours[i][1] + ShortestPathWeights[key]: key } # update the auxiliary dictionary with new values
                    ShortestPathWeights[neighbours[i][0]] = neighbours[i][1] + ShortestPathWeights[key]


    return collections.OrderedDict(sorted(ShortestPathWeights.items(), key= lambda t:t[1]))


def main():


    graph = {
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

    EdgesInMinimumSpanningtree = PrimsTree(graph,'D')
    print(EdgesInMinimumSpanningtree)


if __name__ == "__main__":
    main()
