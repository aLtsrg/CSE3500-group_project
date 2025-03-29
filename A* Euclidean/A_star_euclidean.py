#
# A_star implementation utilizing euclidean distance - SRG 3/26/2025
#

import heapq as heap
import math as m

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
    open_list = [] #minheap of nodes to be explored by lowest total cost(f)
    closed_set = set() #set of visited nodes

    start_node = Node(start, None, 0, euclideanDistance(start, goal))
    heap.heappush(open_list, start_node)

    while open_list:
        current_node = heap.heappop(open_list) #get node with lowest f

        if current_node.position == goal: #if path is found 
            path = [] 
            
            #constructs a path by going backwards through the parents and reversing path
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1] #reverse path
        
        closed_set.add(current_node.position)

        #find and add all valid neighbors to open_list
        for x, y in [(-1, 0),(1, 0),(0, -1),(0, 1)]: #iterate through all possible neighbors could add diag moves with eg. (1,1)
            neighbor = (current_node.position[0] + x, current_node.position[1] + y)

            if(0 <= neighbor[0] < len(grid) and #check if neighbor within grid bounds, is not obstacle, has not been visited
               0 <= neighbor[1] < len(grid[0]) and
               grid[neighbor[1]][neighbor[0]] == 0 and
               neighbor not in closed_set):
                
                g = current_node.g + 1
                h = euclideanDistance(neighbor, goal)
                neighbor_node = Node(neighbor, current_node, g, h)

                heap.heappush(open_list, neighbor_node) 
    return None


if __name__ == "__main__":
    grid = [
        [0,0,0,0],
        [1,1,0,0],
        [0,0,1,0],
        [0,0,0,0],
    ]

    start = (0, 0)
    goal = (3, 3)
    path = a_star(grid, start, goal)

    if path:
        print("Path found:", path)
    else:
        print("No path found.")
