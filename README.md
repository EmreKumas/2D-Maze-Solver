# 2D-Maze-Solver
This program solves a ***2D maze*** with the help of several search algorithms like ***BFS, DFS, A&#42; (A-Star)*** etc. It takes an input file containing different kinds of informations about the maze and perform each search algorithms, so you can compare and see the differences between each algorithm.

## Details

The program firstly reads the input file you provided and creates the maze. The input file must contain the following informations:

- Maze Size
- Wall Locations
- Trap Locations
- Goal Locations
- Start Location

![img](https://i.ibb.co/dDFRGLV/Maze.jpg)

After that, the program start to search the maze based upon the algorithms it contains. After the algorithm finishes, it prints out the cost of the solution found, the solution path itself and the list of expanded nodes. Here are the algorithms that is contained within the program itself:

- Depth-First Search (DFS)
- Breath-First Search (BFS)
- Iterative-Deepening Search (IDS)
- Uniform-Cost Search (UCS)
- Greedy-Best-First Search (GBFS)
- A-Star Search (A*)

Greedy-Best-First Search and A-Star Search algorithms use an admissible heuristic that is created within the program itself.
