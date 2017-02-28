


# How to reverse a given Directed Acyclic Graph

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
    graph = {0:[1,2], 1:[2], 2:[3], 3:[4], 4:[5], 5:[6], 6:[3,7], 7:[]}
    print(graph)
    reverse = ReverseDAG(graph)
    print(reverse)

    # for node in (graph["2"]):
    #     print(node)


if __name__ == "__main__":
    main()