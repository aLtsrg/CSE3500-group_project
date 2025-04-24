import random
import heapq
import time
import tracemalloc

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position 
        self.parent = parent #previous node in path
        self.g = g #distance traversed through path
        self.h = h #ditance to goal based on hueristic
        self.f = g + h #total cost of any given path

    def __lt__(self, other):
        return self.f < other.f

def measure_memory(astar_function, start, goal, graph):
    tracemalloc.start()
    path = astar_function(graph, start, goal)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return path, peak  # Peak memory in bytes

def measure_time(astar_function, start, goal, graph):
    start_time = time.perf_counter()
    path = astar_function(graph, start, goal)
    end_time = time.perf_counter()
    return path, end_time - start_time

def generate_grid(size, obstacle_density=0.2):
    """
    Generates a grid of given size with a specified obstacle density.
    
    Parameters:
    - size: tuple (rows, cols) defining grid dimensions.
    - obstacle_density: Fraction (0 to 1) representing obstacle coverage.

    """
    rows, cols = size
    grid = [[0 if random.random() > obstacle_density else 1 for _ in range(cols)] for _ in range(rows)]
    return grid

from manhattan import a_star as manhattan
from chebyshev import astar_algorithm as chebyshev
from euclidean import a_star as euclidean

heuristics = {
    
    "Chebyshev": chebyshev,
    "Manhattan": manhattan,
    
}

#testing size
sizes = [10, 20, 50, 100]
for size in sizes:
    grid = generate_grid((size, size), 0)
    start = (0, 0)
    goal = (size - 1, size - 1)
    print(f"testing size: {size}")
    for name, astar_func in heuristics.items():
        path, time_taken = measure_time(astar_func, start, goal, grid)
        _, memory_used = measure_memory(astar_func, start, goal, grid)

        print(f"Heuristic: {name}")
        print(f"Time Taken: {time_taken:.6f} seconds")
        print(f"Peak Memory Usage: {memory_used / 1024:.2f} KB")
        print("-" * 40)