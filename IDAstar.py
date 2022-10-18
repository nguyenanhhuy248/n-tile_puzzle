#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In the following program, Iterative Deepening A* (IDA*) method 
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


def manhattan_distance(state: List, goal: List) -> int:
    """
    Manhattan distance function.

    Calculating the sum of the distances (sum of the vertical and horizontal 
    distance) of each tile in the n-tile puzzle to it's goal position.
    
    Params:
    ----
     - instance (List): the initial instance/state
     - goal (List): the goal state
     
    Return:
    ----
    - distance (int): the Manhattan distance
    """
    
    d_state = {state[i][j]: (i, j) for i in range(len(state)) for j in range(len(state[i]))}
    d_goal = {goal[i][j]: (i, j) for i in range(len(state)) for j in range(len(state[i]))}
    manhattan_func = lambda x, y: abs(x[0]-y[0]) + abs(x[1]-y[1]) 
    distance = 0
    for number in d_state.keys():
        if number != 0:
            distance += manhattan_func(d_state[number], d_goal[number])
    
    return distance


def ida_star(state: List, goal: List) -> Union[None, int]:
    """
    Iterative deepening A* (IDA*) function.

    Implementing IDA* algorithm to find the shortest path to the goal state from
    an instance (initial state)
        
    Params:
    ----
     - instance (List): the initial instance/state
     - goal (List): the goal state
     
    Return:
    ----
    - None if the solution is not found
    - The depth to reach the goal state (which is the heuristic value at the "is goal" state)
    """
    
    def search(state: List, goal: List, g: int, threshold: int, path: List) -> int:
        """
        Recusive search function.

        Implementing A* algorithm to find the shortest path to the goal state from
        an instance (initial state), with the boundary of heuristic value = the
        threshold    
            
        Params:
        ----
         - state (List): this state
         - goal (List): the goal state
         - g (int): the depth until current state
         - threshold (int): the threshold (the maximum boundary for the value of
         the heuristic function)
         - path (List): the path from initial state to this state
         
        Return:
        ----
        - minimum (int): the minimum value of the heuristic function in the search
          or f (int): the new threshold if threshold exceeded
        """
        
        f = g + manhattan_distance(state[-1], goal[-1])
       
        if f > threshold: 
            return f
        
        if state == goal: 
            return True

        minimum = float('inf') 
        for next_move in move(state): 
            if next_move not in path: 
                tmp = search(next_move, goal, g + 1, threshold, path + [next_move])
                if tmp == True: 
                    return True
                if tmp < minimum: 
                    minimum = tmp
        return minimum 
  
    path = [state]

    threshold = manhattan_distance(state[-1], goal[-1])

    while True:
        tmp = search(path[-1], goal, 0, threshold, path)
        if tmp == True: 
            return True, threshold
        elif tmp == float('inf'): 
            return False, float('inf')
        else:
            threshold = tmp



def run(instance, goal) -> None:
    """
    Run the program
    
    Running the program and print the output (Depth, Total_yield, Time):
    
    params:
    - instance (List): the initial instance/state
    - goal (List): the goal state
    """
    t = process_time()
    _, depth = ida_star(instance, goal)
    elapsed = process_time() - t 
    print(f"Depth = {(depth):3} --- Total_yield: {number_of_yield:6} --- Time = {elapsed:8.2f}")

# Declaring the goal and the initial instances, and running the program:

if __name__ == '__main__':
    print("First five instances:", end='\n')
    goal = [0, 2, [[3, 2, 0], [6, 1, 8], [4, 7, 5]]]
    instances = [[0, 0, [[0, 7, 1], [4, 3, 2], [8, 6, 5]]], 
                [0, 2, [[5, 6, 0], [1, 3, 8], [4, 7, 2]]],
                [2, 0, [[3, 5, 6], [1, 2, 7], [0, 8, 4]]],
                [1, 1, [[7, 3, 5], [4, 0, 2], [8, 1, 6]]],
                [2, 0, [[6, 4, 8], [7, 1, 3], [0, 2, 5]]],]

    for instance in instances:
        number_of_yield = 0
        run(instance, goal)

    print("Next five instances:", end='\n')
    goal = [2, 2, [[1, 2, 3], [4, 5, 6], [7, 8, 0]]]
    instances = [[0, 0, [[0, 1, 8], [3, 6, 7], [5, 4, 2]]],
                 [2, 0, [[6, 4, 1], [7, 3, 2], [0, 5, 8]]],
                 [0, 0, [[0, 7, 1], [5, 4, 8], [6, 2, 3]]],
                 [0, 2, [[5, 4, 0], [2, 3, 1], [8, 7, 6]]],
                 [2, 1, [[8, 6, 7], [2, 5, 4], [3, 0, 1]]],]

    for instance in instances:
        number_of_yield = 0
        run(instance, goal)