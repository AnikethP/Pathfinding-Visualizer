# Pathfinding-Visualizer
This project is a realtime visualization of pathfinding algorithms such as Dijkstra's, BFS, and A* search.

**How to use:**

- Right click to place or remove a wall (black).
- Left click to select the starting and end nodes respectively (green).
- Watch the searching algorithm in action, yellow squares represent visited nodes.
- After the end node has been found, a red path will be formed from the start to end.

File | Description
------------ | -------------
dijkstra.py | Implements dijkstra's algorithm using a minheap. A* Optimization based on distance is also included.
board.py | Initializes a row x col board of nodes.
Node.py | Represents a node in the graph.
GUI.py | Implements all animations and interactive visualizer components using tkinter.



Demo:

**Dijkstra's/BFS**

https://user-images.githubusercontent.com/66244944/146669877-c599040f-f65d-40f5-a0c0-7fed10f7f64a.mp4


A* Search

https://user-images.githubusercontent.com/66244944/146670011-72eca30a-04f2-4447-a9af-b149b7f3f569.mp4

