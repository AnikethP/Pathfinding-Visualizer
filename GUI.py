from board import *
from dijkstra import *
from tkinter import *

'''
Implements all GUI features and animations of the visualizer

How to use:

Right click to place or remove a wall (black).
Left click to select the starting and end nodes respectively (green).
Watch the searching algorithm in action, yellow squares represent visited nodes.
After the end node has been found, a red path will be formed from the start to end.
'''

x1,x2,y1,y2 = 0,0,0,0
blacks = {}
root = Tk()
canvas = Canvas(width=500, height=500, borderwidth=0, highlightthickness=0)
canvas.pack(side="top", fill="both", expand="true")
rows = 30
columns = 61
cellwidth = 25
cellheight = 25
e = 0
rect = {}
for column in range(columns):
    for row in range(rows):
        x1 = column*cellwidth
        y1 = row * cellheight
        x2 = x1 + cellwidth
        y2 = y1 + cellheight
        rect[row,column] = canvas.create_rectangle(x1,y1,x2,y2, fill="white", tags="rect")

def getorigin(eventorigin):

    global e, x, x1, y1, x2, y2
    x = eventorigin.x//cellwidth
    y = eventorigin.y//cellheight
    if(e == 0):
        for c in range(columns):
            for r in range(rows):
                m = c*cellwidth
                n = r * cellheight
                b = m + cellwidth
                v = n + cellheight
                board.board[c][r].visited = False
                board.board[c][r].prev = None
                if(board.board[c][r].black == False):
                    board.board[c][r].green = False
                    rect[r,c] = canvas.create_rectangle(m,n,b,v, fill="white", tags="rect")
            
        x1 = x
        y1 = y

        a = x1*cellwidth
        b = y1* cellheight
        a1 = a + cellwidth
        b1 = b + cellheight
        if(board.board[x1][y1].black == False and board.board[x1][y1].green == False):
            rect[row,column] = canvas.create_rectangle(a,b,a1,b1, fill="green", tags="rect")
            board.board[x1][y1].green = True
            e+=1
    elif(e == 1):
        x2 = x
        y2 = y
        a = x2*cellwidth
        b = y2* cellheight
        a1 = a + cellwidth
        b1 = b + cellheight
        if(board.board[x2][y2].black == False and board.board[x2][y2].green == False):
            rect[row,column] = canvas.create_rectangle(a,b,a1,b1, fill="green", tags="rect")
            board.board[x1][y1].green = True
            e=0
            doDijkstra(board, (x1,y1), (x2,y2))

        
def doDijkstra(grid, start, finish):
    graph = dijkstra(grid, start, finish)
    if graph == None:
        return
    s = graph[board.getNode((x2, y2))]
    canvas.unbind("<Button 1>")
    canvas.unbind("<Button 3>")
    while yellows:
        node = yellows.pop(0)
        
        a = node[0]*cellwidth
        b = node[1]* cellheight
        a1 = a + cellwidth
        b1 = b + cellheight
        
        def drawy():
            if((node[0], node[1]) != start and (node[0], node[1]) != finish):
                rect[row,column] = canvas.create_rectangle(a,b,a1,b1, fill="yellow", tags="rect")
        root.after(5, drawy())
        root.update()  
    while((s[1].row, s[1].col) != (x1,y1)):
            
        a = s[1].row*cellwidth
        b = s[1].col* cellheight
        a1 = a + cellwidth
        b1 = b + cellheight
        
        def draw():
            rect[row,column] = canvas.create_rectangle(a,b,a1,b1, fill="red", tags="rect")
        root.after(5, draw())
        root.update()
        s = graph[board.getNode((s[1].row, s[1].col))]
    canvas.bind("<Button 1>", getorigin)
    canvas.bind("<Button 3>", addblock)    
def addblock(eventorigin):
    x = eventorigin.x//cellwidth
    y = eventorigin.y//cellheight
    x1 = x
    y1 = y

    a = x1*cellwidth
    b = y1* cellheight
    a1 = a + cellwidth
    b1 = b + cellheight
    if(board.board[x][y].black == True and board.board[x][y].green == False):
        rect[row,column] = canvas.create_rectangle(a,b,a1,b1, fill="white", tags="rect")
        board.board[x][y].black = False
    elif(board.board[x][y].black == False and board.board[x][y].green == False):
        rect[row,column] = canvas.create_rectangle(a,b,a1,b1, fill="black", tags="rect")
        board.board[x][y].black = True

canvas.bind("<Button 1>", getorigin)
canvas.bind("<Button 3>", addblock)
board = Board(columns, rows)
root.mainloop()