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

        
       #iterate over possible movements(left, right, up, down)
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            #calculate new position
            x , y = current_node.x + dx, current_node.y + dy
            #check if new position is valid
            if (0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0):
                #create a new neigbor node
                #skio if already visited
                neighbor = Node(x, y)
                if (neighbor.x, neighbor.y) in closed_set:
                    continue
                
                #calculate g to track steps from start to this spot
                tentative_g = current_node.g + 1
                
                #update neighbor if the new path is better
                if tentative_g < neighbor.g:
                    neighbor.parent = current_node
                    neighbor.g = tentative_g
                    neighbor.h = manhattan_distance(neighbor, end_node)
                    neighbor.f = neighbor.g + neighbor.h
                    
                    #add to open list if it's not there
                    # if not any(n[1].x == neighbor.x and n[1].y == neighbor.y for n in open_list):
                    heapq.heappush(open_list, (neighbor.f, neighbor))    
    
    #return none if no path is found
    return None


####TEST CASE####

def mark_grid(grid, path):
    #mark the path with *
    for x, y in path:
        grid[x][y] = '*'
    return grid

def print_grid(grid):
    #print the grid row by row
    for row in grid:
        print(' '.join(str(cell) for cell in row))

#sample grid, can change values to test different scenarios
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

#start and end point
start = (0, 0)  
end = (4, 4)    


path = a_star(grid, start, end)

#check if a path was found
if path is None:
    print("Path not found")
else:
    print("Path found:", path)
    
    # mark the path on the grid
    #print the grid w/ the path
    visual_path = mark_grid(grid, path)
    print("\nGrid with the path:")
    print_grid(visual_path)
