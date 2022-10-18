# Solving n-tile puzzle with Iterative Deepening Depth First Search (IDDFS) and Iterative Deepening A* (IDA*)
In the n-tile puzzle game, the goal is to reach this state:

![Screenshot 2022-10-19 at 00 08 33](https://user-images.githubusercontent.com/81903733/196561911-151afcea-6d0f-4eab-8b1e-dca771c5a2de.png)

The initial state may look like this:

![Screenshot 2022-10-19 at 00 09 02](https://user-images.githubusercontent.com/81903733/196561958-1b7bc739-8dfa-43cc-8423-e7cfeb4f3c04.png)

The player's mission is to slide the tiles to reach the goal state from an initial state.

The python scripts employ 2 search algorithms, Iterative Deepening Depth First Search (IDDFS) and Iterative Deepening A* (IDA*), to solve the n-tile puzzle.

The code can work with any size of the tile puzzle. However, for demonstration, start and goal states of a 8-tile puzzle are used.

In the python scripts, the states of the n-tile puzzle are represented by lists of numbers.

![Screenshot 2022-10-19 at 00 21 18](https://user-images.githubusercontent.com/81903733/196562993-da2a95a7-0fa1-42ec-810c-ec45b29520d8.png)

The above state, for example, is represented as: [1,1, [[2,1,6],[4,0,8],[7,5,3]] ]

Where the first 2 numbers are the position of the blank tile.
