from board import *
from Node import *
from tkinter import *
import heapq
import itertools
import math
yellows = []

def dijkstra(grid, start, finish):
    '''
    Implements dijkstra's algorithm using a minheap. A* Optimization based on distance is also included.
    '''
    visited = set()
    table = {x : [float("inf"), None] for y in grid.board for x in y}
    table[grid.getNode(start)][0] = 0
    counter = itertools.count()
    min_dist_heap = [(0, -1, grid.getNode(start))]
    while(not grid.getNode(finish).visited):
        if(len(min_dist_heap) == 0):
            return
        curr_dist, _, curr_node = heapq.heappop(min_dist_heap)
        up = grid.getNode((curr_node.row + 1, curr_node.col))
        down = grid.getNode((curr_node.row -1, curr_node.col))
        left = grid.getNode((curr_node.row, curr_node.col-1))
        right = grid.getNode((curr_node.row, curr_node.col+1))
        neighbors = [up, down, left, right]
        neighbors = [x for x in neighbors if x]
        if curr_node in visited: continue
        visited.add(curr_node)
        curr_node.visit()

        yellows.append((curr_node.row, curr_node.col))
        for neighbor in neighbors:
            if neighbor in visited: continue
            distance = curr_dist + abs(neighbor.row - curr_node.row) + abs(neighbor.col - curr_node.col)
            if distance < table[neighbor][0]:
                table[neighbor][0] = distance
                table[neighbor][1] = curr_node
                #Dijkstra's Algorithm
                heapq.heappush(min_dist_heap, (distance, next(counter), neighbor))
                #A* Optimization: heapq.heappush(min_dist_heap, ((math.sqrt((neighbor.row - finish[0])**2 + (neighbor.col - finish[1])**2)), next(counter), neighbor))
    return table
board = Board(5, 5)