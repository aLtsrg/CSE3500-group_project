import heapq

# Function to calculate Chebyshev distance
def calculate_chebyshev_distance(current_node, goal_node):
    difference_in_x = abs(current_node[0] - goal_node[0])
    difference_in_y = abs(current_node[1] - goal_node[1])
    return max(difference_in_x, difference_in_y)

# Function for the A* algorithm
def astar_algorithm(grid, start_position, goal_position):
    # Get the dimensions of the grid
    rows = len(grid)
    columns = len(grid[0])

    # Priority queue to store nodes to be evaluated
    open_list = []
    heapq.heappush(open_list, (0, start_position))

    # Dictionary to store the cost to reach each node
    g_score = {start_position: 0}

    # Dictionary to store the path
    path_history = {}

    while open_list:
        # Extract the node with the lowest cost
        _, current_node = heapq.heappop(open_list)

        # If the goal is reached, reconstruct and return the path
        if current_node == goal_position:
            path = []
            while current_node in path_history:
                path.append(current_node)
                current_node = path_history[current_node]
            path.append(start_position)
            path.reverse()  # Reverse to get the path from start to goal
            return path

        # Generate neighbors of the current node
        potential_neighbors = [
            (current_node[0] - 1, current_node[1]),   # Move up
            (current_node[0] + 1, current_node[1]),   # Move down
            (current_node[0],     current_node[1] - 1),  # Move left
            (current_node[0],     current_node[1] + 1),  # Move right
            (current_node[0] - 1, current_node[1] - 1),  # Diagonal: top-left
            (current_node[0] + 1, current_node[1] + 1),  # Diagonal: bottom-right
            (current_node[0] - 1, current_node[1] + 1),  # Diagonal: top-right
            (current_node[0] + 1, current_node[1] - 1)   # Diagonal: bottom-left
        ]

        for neighbor in potential_neighbors:
            neighbor_row = neighbor[0]
            neighbor_column = neighbor[1]

            # Check if the neighbor is valid (within the grid boundaries and not an obstacle)
            if 0 <= neighbor_row < rows and 0 <= neighbor_column < columns and grid[neighbor_row][neighbor_column] == 0:
                # Calculate tentative cost to reach the neighbor
                tentative_g_score = g_score[current_node] + 1

                # Update if this path is shorter than any previously known path
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + calculate_chebyshev_distance(neighbor, goal_position)
                    heapq.heappush(open_list, (f_score, neighbor))
                    path_history[neighbor] = current_node

    
    return None

if __name__ == "__main__":
    
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    start_position = (0, 0)
    goal_position = (3, 3)

    resulting_path = astar_algorithm(grid, start_position, goal_position)
    print("Path from start to goal:", resulting_path)