# 8-Tile-Puzzle-Modified
A modified version of the 8 tile puzzle

Overview
Objective is to solve a modified version of the eight-puzzle. 

Specifications:
1.	The cost of each move is the value of the tile being moved. 
2.	Repeated state checking: both previously visited and currently in the “queue”
3.	User interface: minimum is a simple text interface
4.	Easy, medium, and hard difficulties set beginning states
5.	Print out the resulting solution, if one was found, showing the state, move that was made, cost of the move, and total cost.

Approach
I implemented the following algorithms successfully for easy, medium, and hard difficulties:
•	Breadth-first search (BFS)
•	Depth-first search (DFS)
•	Iterative deepening (IDDFS)
•	Uniform cost search (UCS)
•	Best-first search (BESTFS), where h = # of misplaced tiles
•	A*1, where h = # of misplaced tiles
•	A*2, where h = # of sum of the Manhattan distances
•	A*3, where h= # of misplaced tiles + # of sum of the Manhattan distances

BFS was implemented with a queue using a first in first out (FIFO) methodology. 

DFS was implemented with a deque using a first in last out (FILO) methodology. I did not implement a check to see if the state being visited was already in the deque. As this would defeat the purpose of the FILO methodology. I did perform testing to verify that this would result in a significant increase in both length and space.

IDDFS was implemented with a deque using a first in last out (FILO) methodology, but with an iterative approach. Essentially DFS was performed for each depth layer before incrementing the depth up to the maximum depth (user defined) and repeating until either a solution was found or not found. Similar to DFS, I did not implement a check to see if the state being visited was already in the deque. Since this approach uses an iterative approach, I also reset the data structure tracking visited nodes with every depth increment.  

I did experience one issue with IDDFS. If the maximum depth, as defined by the user, was 30 and the difficulty was ‘hard’, the agent would return ‘non solution found’. I hard coded an adjustment that if the input depth was 30, it would become 31. However, the solution found would indicate a solution depth of 30. This issue did not present itself with the ‘easy’ or ‘medium’ difficulties.

UCS was implemented with a priority queue heap using the total cost for priority.

BESTFS was implemented with a priority queue heap using the total number of tiles that ware not in the correct position for priority.

A*1 was implemented with a priority queue heap using f(n) = g(n) + h(n) for priority. Where g(n) is the total cost up to the state and h(n) is total number of tiles that ware not in the correct position.

A*2 was implemented with a priority queue heap using f(n) = g(n) + h(n) for priority. Where g(n) is the total cost up to the state and h(n) is sum of the Manhattan distance for each tile from its current position to the correct position.

A*3 was implemented with a priority queue heap using f(n) = g(n) + h(n) for priority. Where g(n) is the total cost up to the state and h(n) is sum of the Manhattan distance for each tile from its current position to the correct position and total number of tiles that ware not in the correct position.

UCS, BESTFS, A*1, A*2, A*3 all performed checks to see if the new state was already in the ‘queue’ and if it was present, if had a lower value. The existing state would be updated if the new state was of a lesser value.
