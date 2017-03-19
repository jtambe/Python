
'''
credit : https://www.youtube.com/watch?v=xouin83ebxE
'''

class NQueenProblem:

    class Position:
        def __init__(self, row, col):
            self.row = row
            self.col = col


    def solveNqueen(self, n):

        positions = [None] * n
        hasSolution = self.NqueenUtil(n, 0, positions)

        if hasSolution ==  True:
            return positions
        else:
            return False

    def NqueenUtil(self, n,row, positions):

        if n == row:
            return True

        col = 0
        for col in range(n):
            foundsafe = True

            for queen in range(row):

                if positions[queen].col == col \
                    or positions[queen].row - positions[queen].col == row - col \
                    or positions[queen].row + positions[queen].col == row + col:
                    foundsafe = False
                    break

            if foundsafe:
                p = self.Position(row,col)
                positions[row] = p
                if self.NqueenUtil(n, row +1, positions):
                    return True







prob = NQueenProblem()
positions = (prob.solveNqueen(4))

for i in range(len(positions)):
    print(str(positions[i].row) + " : " + str(positions[i].col))
