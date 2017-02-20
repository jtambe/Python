
vertices = [0,1,2,3,4,5,6,7]
visited = [0,1,3,5,4]
verticesSet = set(vertices)
visitedSet = set(visited)
remainingvertices = verticesSet - visitedSet

print(remainingvertices)
#{2, 6, 7}
print(verticesSet ^ visitedSet)
#{2, 6, 7}

print(len(remainingvertices))
#3

print(verticesSet.intersection(visitedSet))
#{0, 1, 3, 4, 5}

