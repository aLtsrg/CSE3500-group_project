import matplotlib.pyplot as plt
import numpy as np



def visualize_grid(grid, visited=None, path=None, start=None, goal=None, final = False):
    clear = True
    grid_array = np.array(grid)
    display_grid = np.where(grid_array == 1, 0, 0.8)

    if visited:
        for x, y in visited:
            if grid_array[y][x] == 0:
                display_grid[y][x] = 0.5  # visited = medium gray

    if path:
        for x, y in path:
            display_grid[y][x] = 1  # final path = white
            clear = False

    if start:
        display_grid[start[1]][start[0]] = 0.0  # start = black

    if goal:
        display_grid[goal[1]][goal[0]] = 1.0  # goal = white

    plt.imshow(display_grid, cmap='gray', interpolation='nearest', vmin=0, vmax=1)
    plt.pause(0.000001)
    
    if clear:
        plt.clf()
