# class Point:
#     def __init__(self, x,y):
#         self.x = x
#         self.y = y
#
# currentPath = []
#
# def GetPaths(x,y):
#
#     P = Point(x,y)
#     currentPath.append(P)
#
#     if(x == 0 and y ==0):
#         return True
#
#     success = False
#
#     if(x>= 1 ):
#         success = GetPaths(x-1,y)
#
#     if(not success and y >= 1):
#         success = GetPaths(x, y-1)
#
#     if(not success):
#         currentPath.remove(P)
#
#     return success
#
#
# GetPaths(3,4)
#
# for point in currentPath:
#     print("X: " + str(point.x) + " Y :" + str(point.y) )





# def IsFree(x,y):
#     if grid[x][y] != -1:
#         return True
#     else:
#         return False
#
# def IsValidSquare(x,y):
#     if x > 3 or y > 4 or x < 0 or y < 0:
#         return False
#     else:
#         return IsFree(x,y)
#
#
# def IsAtEnd(x,y):
#     if x == 3 and y == 4:
#         return True
#
#
# def GetPathCount(x, y):
#     print("GetPathCount[" + str(x) + "][" + str(y) + "]")
#     if(not IsValidSquare(x,y)):
#         return 0
#     if(IsAtEnd(x,y)):
#         return 1
#     if( paths[x][y] == 0):
#         print("paths["+str(x)+"]["+str(y)+"]: "+ str(paths[x][y]))
#         a = GetPathCount(x + 1, y)
#         #a = 0 if (a == None) else a
#
#         print("b = GetPathCount(" + str(x) + ","+str(y+1)+")")
#         b = GetPathCount(x, y + 1)
#         print("a: " + str(a) +" b:" + str(b))
#         #b = 0 if (b == None) else b
#         paths[x][y] = a + b
#
# # print(paths)
# # print('\n')
# # print(grid)
#
# #GetPathCount(0,0)



import numpy
grid = numpy.zeros((4,5))

grid[2][0] = -1
grid[3][3] = -1
grid[2][2] = -1
grid[1][3] = -1
#grid[0][1] = -1


def GetCount(x,y):

    paths = numpy.zeros((x, y))

    # from end position there is only 1 path
    paths[x-1][y-1] = 1

    # from last horizontal row, one can only move right,
    # which means there is only one path to get to end, unless there is roadblock which means 0 paths
    for i in range(y-1):
        if grid[x-1][i] == -1:
            paths[x - 1][i] = 0
        else:
            paths[x - 1][i] = 1


    # from last vertical column, one can only move down,
    # which means there is only one path to get to end, unless there is roadblock which means 0 paths
    for i in range(x - 1):
        if grid[i][y-1] == -1:
            paths[i][y - 1] = 0
        else:
            paths[i][y - 1] = 1


    # Now calculate remaining blocks of matrix using following logic,
    # which is same as in Gayle's video on you tube
    # https://www.youtube.com/watch?v=P8Xa2BitN3I&list=PLuPgntZBM57y0GdsFiqpydxJKsIqMVYD6&index=1
    # No of paths at current block = no of paths from right block + no of paths from lower block
    for i in reversed(range(3)):
        for j in reversed(range(4)):
            if grid[i][j] == -1:
                paths[i][j] = 0
            else:
                paths[i][j] = paths[i+1][j] + paths[i][j+1]

    print(paths)
    print("Number of total paths from origin :"+str(paths[0][0]))


GetCount(4,5)
