from Node import *

class Board:
    '''
    Initializes a row x col board of Nodes
    '''
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.board = []
        for i in range(row):
            self.board.append([Node(i, x) for x in range(col)])
    def getNode(self, coords):
        if(coords[0] < 0 or coords[1] < 0 or coords[0] >= self.row or coords[1] >= self.col or self.board[coords[0]][coords[1]].black == True):
            return None 
        return self.board[coords[0]][coords[1]]
# board = Board(5, 5)
# print(board.board)