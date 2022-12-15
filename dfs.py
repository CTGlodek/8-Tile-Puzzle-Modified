#  Modified 8 tile puzzle
# 
# DFS agent
from p_node import PNode
from collections import deque

def dfs(starting_state):

    # Initialize the first node with the starting state
    initial_node = PNode(starting_state, None, None, 0, 0, 0)

    # Initialize the dequeue FILO
    s = deque()

    #add starting node to the dequeue
    s.append(initial_node)

    # var to track the max size of the dequeue
    deque_size = 1

    # initialize the states previously visited as a set
    history = set()

    # main loop for DFS
    while (len(s)>0):

        # update the max size of the dequeue if dequeue is larger
        if len(s) > deque_size:
            deque_size = len(s)

        #pop the first node
        node = s.pop()

        # add the state to the history
        history.add(str(node.state))

        #calling the find children method
        children = node.find_children()

        # iterate through the children found
        for child in children:

            #check to see if the this state has already been visited
            if str(child.state) not in history:

                # check to see if the current state matches the goal state
                if child.match_goal():
                    return child, len(history), deque_size

                # add the child to the dequeue
                s.append(child)

    #return a dumby node if no solution is found
    return PNode([0,0,0,0,0,0,0,0,0], None, "None", 0, 0, 0), 0, 0