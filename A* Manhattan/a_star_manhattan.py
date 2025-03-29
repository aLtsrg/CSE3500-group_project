import heapq

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #g is the cost to get to current node
        self.g = float('inf')
        #f is the total estimated cost (g+h)
        self.f = float('inf')
        #h is the heuristic, distance to the goal
        self.h = 0
        self.parent = None

    def __lt__(self, other):
        #choose node with smaller f
        return self.f < other.f

def manhattan_distance(start, end):
    #calculate manhattan distance between the start and end points
    return abs(start.x - end.x) + abs(start.y - end.y)

def a_star(grid, start, end):
    #nodes that need to be visited
    open_list = []
    #nodes that have already been visited
    closed_set = set()
    
    start_node = Node(start[0], start[1])
    end_node = Node(end[0], end[1])
    
    #calculates f= g + h
    start_node.g = 0
    start_node.h = manhattan_distance(start_node, end_node)
    start_node.f = start_node.g + start_node.h
    
    #add the start node to open list
    heapq.heappush(open_list, (start_node.f, start_node))
    
    while open_list:
        #take the node w/ the smallest f 
        current_node = heapq.heappop(open_list)[1]
        
        #if current node is the goal
        #follow the path back by adding nodes to the list from current to parent, then reverse it
        if current_node.x == end_node.x and current_node.y == end_node.y:
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1]
        
        #mark this node as visited
        closed_set.add((current_node.x, current_node.y))


        
        #####PSEUDOCODE FOR HANDLING NEIGHBORS#####
        #work in progress 

        #Iterate over possible movements (left, right, up, down)
        #if the new position is within bounds and not blocked 
        #then create a new node and check if it should be considered
        #update values based on g-cost if the new path is better
        #if not already in open list, add it
    
    
    return None  #there is no path

if __name__ == "__main__":

    #test case to check pathfinding
    grid = [
        [0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]
    ]

    start = (0, 0)
    end = (4, 4)
    
    path = a_star(grid, start, end)

    if path is None:
        print("path not yet found")
    else:
        print("path was incorrectly returned")
