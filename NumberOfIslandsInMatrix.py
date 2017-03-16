import numpy as np


visited = np.zeros([5, 5])
count = 0

def VisitNeighbours(arr,i,j):

    global visited

    if j+1 < len(arr[i]):
        visited[i][j+1] = 1
        if arr[i][j+1] == 1:
            VisitNeighbours(arr,i, j+1)

    if i+1 < len(arr[j]):
        visited[i+1][j] = 1
        if arr[i+1][j] == 1 :
            VisitNeighbours(arr,i+1, j)

    if i+1 < len(arr[j]) and j+1 < len(arr[i]) :
        visited[i+1][j+1] = 1
        if arr[i+1][j+1] == 1:
            VisitNeighbours(arr,i+1, j+1)



def CountIslands(arr):

    global visited
    global count

    for i in range(5):
        for j in range(5):
            if visited[i][j] == 0:
                visited[i][j] = 1
                if(arr[i][j] == 1):
                    count += 1
                    VisitNeighbours(arr,i, j)












arr = np.zeros([5,5])
arr[0][0] = arr[0][1] = arr[1][0] = arr[1][1] = 1
arr[0][3] = arr[0][4] = arr[1][3] = arr[1][4] = 1
arr[3][0] = arr[3][1] = arr[4][0] = arr[4][1] = 1
arr[3][3] = arr[4][3]  = 1

print(arr)
'''
[[ 1.  1.  0.  1.  1.]
 [ 1.  1.  0.  1.  1.]
 [ 0.  0.  0.  0.  0.]
 [ 1.  1.  0.  1.  0.]
 [ 1.  1.  0.  1.  0.]]
'''


CountIslands(arr)
print(count) # 4

print(visited)
'''
[[ 1.  1.  1.  1.  1.]
 [ 1.  1.  1.  1.  1.]
 [ 1.  1.  1.  1.  1.]
 [ 1.  1.  1.  1.  1.]
 [ 1.  1.  1.  1.  1.]]
'''


























