#
# A_star implementation utilizing euclidean distance - SRG 3/26/2025
#
import random
import heapq as heap
import math as m
import matplotlib.pyplot as plt
from visualize_grid import visualize_grid

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position 
        self.parent = parent #previous node in path
        self.g = g #distance traversed through path
        self.h = h #ditance to goal based on hueristic
        self.f = g + h #total cost of any given path

    def __lt__(self, other):
        return self.f < other.f

def euclideanDistance(pos, goal):
    return m.sqrt((goal[0] - pos[0])**2 + (goal[1] - pos[1])**2)

def a_star(grid, start, goal):
    open_list = []
    closed_set = set()
    visited_nodes = []

    start_node = Node(start, None, 0, euclideanDistance(start, goal))
    heap.heappush(open_list, start_node)

    plt.ion()  # enable interactive plotting

    while open_list:
        current_node = heap.heappop(open_list)

        if current_node.position in closed_set:
            continue  # skip already visited

        visited_nodes.append(current_node.position)
        visualize_grid(grid, visited=visited_nodes, start=start, goal=goal)

        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            visualize_grid(grid, visited=visited_nodes, path=path[::-1], start=start, goal=goal)
            plt.ioff()
            plt.show()
            return path[::-1]

        closed_set.add(current_node.position)

        for x, y in [(-1, 0),(1, 0),(0, -1),(0, 1)]:
            neighbor = (current_node.position[0] + x, current_node.position[1] + y)

            if (0 <= neighbor[0] < len(grid[1]) and
                0 <= neighbor[1] < len(grid) and
                grid[neighbor[1]][neighbor[0]] == 0 and
                neighbor not in closed_set):

                g = current_node.g + 1
                h = euclideanDistance(neighbor, goal)
                neighbor_node = Node(neighbor, current_node, g, h)
                heap.heappush(open_list, neighbor_node)
    

    plt.ioff()
    plt.show()
    return None



def create_grid(rows, cols):
    # Create a 2D array
    grid = [[random.choices([0, 1], weights=[100, 0])[0] for _ in range(cols)] for _ in range(rows)]
    return grid


if __name__ == "__main__":
    grid = create_grid(30, 30)
    

    start = (0, 0)
    goal = (29, 29)
    path = a_star(grid, start, goal)

    if path:
        print("Path found:", path)
    else:
        print("No path found.")