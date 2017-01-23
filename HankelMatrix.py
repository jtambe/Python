

# Given a 2d matrix convert it into hankel matrixs

import numpy as np


def HankelMatrix(matrix):
    # get rows and columns in a 2d matrix
    numRows = len(matrix)
    numCols = len(matrix[0])
    print('Rows: '+ str(numRows) + ' & Cols: ' + str(numCols))

    # for i in range(numRows):
    #     for j in range(numCols):
    #         print(matrix[i,j])

    #for i,j in enumerate(matrix):

    # for number of columns, traverse diagonally and calculate the average
    for j in range(numCols):
        x = 0
        y = j
        sum = 0
        count = 1
        while (x <= j):
            sum = (sum + matrix[x,y])/count
            x = x + 1
            y = y - 1
            count += 1
        matrix[0,j] = sum

    # traverse linearly oen more time to set the values
    for j in range(numCols):
        x = 0
        y = j
        while(x <= j):
            matrix[x,y] = matrix[0,j]
            x = x + 1
            y = y - 1

    # for number of rows, starting from 1 (not 0), traverse diagonally and calculate the average
    for i in range(1,numRows):
        x = i
        y = numCols-1
        sum = 0
        count = 1
        while( x <= numRows -1):
            sum = (sum + matrix[x,y])/count
            x = x + 1
            y = y - 1
            count += 1
        matrix[i,numCols-1] = sum

    # traverse linearly oen more time to set the values
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
    # call HankelMatrix function and pass argument
    HankelMatrix(b)
    print(b)


def main():
    Execute2DList()

if __name__ == '__main__':
    main()

