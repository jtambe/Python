

# Given a 2d matrix convert it into hankel matrixs

import numpy as np


def HankelMatrix(matrix):
    numRows = len(matrix)
    numCols = len(matrix[0])
    print('Rows: '+ str(numRows) + ' & Cols: ' + str(numCols))

    # for i in range(numRows):
    #     for j in range(numCols):
    #         print(matrix[i,j])

    #for i,j in enumerate(matrix):

    for j in range(numCols):
        x = 0
        y = j
        sum = 0
        while (x <= j):
            sum = sum + matrix[x,y]
            x = x + 1
            y = y - 1
        matrix[0,j] = sum

    for j in range(numCols):
        x = 0
        y = j
        while(x <= j):
            matrix[x,y] = matrix[0,j]
            x = x + 1
            y = y - 1



    for i in range(1,numRows):
        x = i
        y = numCols-1
        sum = 0
        while( x <= numRows -1):
            sum = sum + matrix[x,y]
            x = x + 1
            y = y - 1
        matrix[i,numCols-1] = sum

    for i in range(1, numRows):
        x = i
        y = numCols -1
        while(x <= numRows -1):
            matrix[x,y] = matrix[i,numCols-1]
            x = x + 1
            y = y - 1


    #print(matrix)





def Execute2DList():
    b = np.arange(12).reshape(4,3)
    #print(b)
    b = np.arange(30).reshape(6,5)
    print(b)
    HankelMatrix(b)
    print(b)


def main():
    Execute2DList()

if __name__ == '__main__':
    main()

