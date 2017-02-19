from collections import deque # to use list as a queue

def BFS(graph, source):

    level = 0
    queue = deque([]) # this queue is use add neighbours
    visited = [] # this list will keep track of visited nodes

    queue.append(source)
    visited.append(source)
    print("Node: "+ str(source) +" Hop count: "+ str(level))

    while(len(queue) != 0):
        node = queue.popleft() # popleft is deque function
        level += 1
        for neighbour in graph[node]:
            if not neighbour in visited: # process neighbours of current visited node only if they are not previously visited
                visited.append(neighbour)
                queue.append(neighbour)
                print("Node: " + str(neighbour) + " Hop count: " + str(level))



def main():
    graph = {0:[1,2], 1:[2], 2:[0,1]}
    print(graph)
    # for node in (graph["2"]):
    #     print(node)
    BFS(graph,0)
    BFS(graph, 1)



if __name__ == "__main__":
    main()