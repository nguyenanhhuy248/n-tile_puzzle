#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In the following program, Iterative Deepening Depth First Search (IDDFS) method 
will be employed to solve an n-tile puzzle. The code can work with any size of 
the tile puzzle. However, for demonstration, start and goal states of a 8-tile
puzzle will be used.

First five initial instances used for demonstrations are:
    [0, 0, [[0, 7, 1], [4, 3, 2], [8, 6, 5]]],
    [0, 2, [[5, 6, 0], [1, 3, 8], [4, 7, 2]]], 
    [2, 0, [[3, 5, 6], [1, 2, 7], [0, 8, 4]]], 
    [1, 1, [[7, 3, 5], [4, 0, 2], [8, 1, 6]]], 
    [2, 0, [[6, 4, 8], [7, 1, 3], [0, 2, 5]]],
and the goal state to reach is: 
    [0, 2, [[3, 2, 0], [6, 1, 8], [4, 7, 5]]]  

Next five initial instances used for demonstrations are:
    [0, 0, [[0, 1, 8], [3, 6, 7], [5, 4, 2]]], 
    [2, 0, [[6, 4, 1], [7, 3, 2], [0, 5, 8]]], 
    [0, 0, [[0, 7, 1], [5, 4, 8], [6, 2, 3]]], 
    [0, 2, [[5, 4, 0], [2, 3, 1], [8, 7, 6]]], 
    [2, 1, [[8, 6, 7], [2, 5, 4], [3, 0, 1]]],
with the goal state 
    [2,2,[[1,2,3],[4,5,6],[7,8,0]]].

As an output, the program will print:
    1. Depth: the number of moves to reach the goal from each initial state 
    (i.e. the number of states minus 1 in the shortest path from each instance 
    to the goal)
    2. Total_yield: the total number states that the program yield during the 
    search for a solution for each initial instance
    3. Time: the computing time the search took for each initial instance
"""
# importing the python libraries
from copy import deepcopy
from typing import List, Union
from time import process_time

def move_blank(i: int , j: int, n: int) -> tuple:
    """
    Moving the blank tile function
   
    Yielding all the possible movements of the blank tile (down/up/right/left) 
    from 1 state with 1 move
    
    Params:
    ----
    - i (int): the vertical position of the blank tile, i is in range (0,n-1)
    - j (int): the vertical position of the blank tile, j is in range (0,n-1)
    - n (int): the number of rows/columns in the puzzle
    
    Returns:
    ----
     - (i1,j1) (tuple): all the possible positions of the blank tile as tuples of (i,j)
    
    """
    if i+1 < n: 
        yield (i+1, j)
    if i-1 >= 0:
        yield (i-1, j)
    if j+1 < n:
        yield (i, j+1) 
    if j-1 >= 0:
        yield (i, j-1)


def move(state: List) -> List:
    """
    Changing the state function
    
    Yielding all the possible states can be generated from 1 state after 1 move
    
    Params:
    ----
    - state (list): the state before such move
    
    Returns:
    ----
    - next_state (list): all the next possilbe states after such move
    
    """
    global number_of_yield
    [i, j, grid] = deepcopy(state)
    n = len(grid)
    for pos in move_blank(i, j, n):
        i1, j1 = pos
        grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]
        yield [i1, j1, grid]
        number_of_yield += 1
        grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]


def id_dfs(instance: List, goal: List, max_depth: int=100) -> Union[None, List]:
    """
    IDDFS implementation function
    
    Implementing IDDFS algorithm to find the shortest path to the goal state from
    an instance (initial state)

    Params:
    ----
     - instance (List): the initial instance/state
     - goal (List): the goal state
     - max_depth: the maximum depth to explore, set as default to be 100

    Returns:
    ----
     - None if the solution is not found at the maximum depth
     - The depth to reach the goal state and the path from the intial state to
     the goal state
    """
    def dfs_rec(path: List, state: List, max_depth: int) -> List:
        """
        Recusive depth first search 
        
        Implementing depth first search algorithm until a maximum depth to check
        if the goal state is reached
    
        Params:
        ----
         - path (List): the path before the current state
         - state (List): this state
         - max_depth: the maximum depth to explore, taken from the loop below
    
        Returns:
        ----
         - None if the solution is not found at the maximum depth
         - The path from the intial state to the goal state
        """    
        path.append(state)
        if state == goal:
            return path
        else:
            if len(path)>=max_depth:
                return None
            else:
                for next_state in move(state):
                    path_copy = path.copy()
                    if next_state not in path_copy:
                        solution = dfs_rec(path_copy, next_state, max_depth) 
                        if solution != None:
                            return solution
            return None

    
    for depth in range(max_depth):
        solution = dfs_rec([],instance, depth)
        if solution:
            return depth, solution


def run(instance, goal) -> None:
    """
    Run the program
    
    Running the program and print the output (Depth, Total_yield, Time):
    
    params:
    - instance (List): the initial instance/state
    - goal (List): the goal state
    """
    t = process_time()
    depth,  _ = id_dfs(instance, goal)
    elapsed = process_time() - t
    print(f"Depth = {(depth-1):3} --- Total_yield: {number_of_yield:10} --- Time = {elapsed:8.2f}")

# Declaring the goal and the initial instances, and running the program:
    
if __name__ == '__main__':
    print("First five instances:", end='\n')
    goal = [0, 2, [[3, 2, 0], [6, 1, 8], [4, 7, 5]]]    
    instances = [[0, 0, [[0, 7, 1], [4, 3, 2], [8, 6, 5]]],
                [0, 2, [[5, 6, 0], [1, 3, 8], [4, 7, 2]]],
                [2, 0, [[3, 5, 6], [1, 2, 7], [0, 8, 4]]],
                [1, 1, [[7, 3, 5], [4, 0, 2], [8, 1, 6]]],
                [2, 0, [[6, 4, 8], [7, 1, 3], [0, 2, 5]]]]

    for instance in instances:
        number_of_yield = 0
        run(instance, goal)

    print("Second five instances:", end='\n')
    goal = [2, 2, [[1, 2, 3], [4, 5, 6], [7, 8, 0]]]
    instances = [[0, 0, [[0, 1, 8], [3, 6, 7], [5, 4, 2]]],
                  [2, 0, [[6, 4, 1], [7, 3, 2], [0, 5, 8]]],
                  [0, 0, [[0, 7, 1], [5, 4, 8], [6, 2, 3]]],
                  [0, 2, [[5, 4, 0], [2, 3, 1], [8, 7, 6]]],
                  [2, 1, [[8, 6, 7], [2, 5, 4], [3, 0, 1]]]]

    for instance in instances:
        number_of_yield = 0
        run(instance, goal)