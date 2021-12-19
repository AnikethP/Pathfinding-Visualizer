class Node:
    '''
    Represents a node in the graph
    '''
    def __init__(self, my_row, my_col):  
        self.row = my_row
        self.col = my_col
        self.visited = False
        self.prev = None
        self.black = False
        self.green = False
    def visit(self):
        self.visited = True
    def __repr__(self):
        return f"Node({self.row},{self.col})"