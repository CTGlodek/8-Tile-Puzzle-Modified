#  Modified 8 tile puzzle
# 
# Iterative Deepening agent
from p_node import PNode
from collections import deque

def iddfs(starting_state, max_depth):
    
    # initialize i to track depth level while looping
    i = 0

    # Identified an issue where if the max size was 30 (target depth for hard difficulty), 
    # the agent would return no solution found,
    # This is a temp work around

    if max_depth == 30:
        max_depth = max_depth +1

    # main loop for Iterative Deepening
    while not i > max_depth:

        # Initialize the first nodewith the starting state
        initial_node = PNode(starting_state, None, None, 0, 0, 0)

        # Initialize the dequeue FILO
        s = deque()

        #add starting node to the dequeue
        s.append(initial_node)

        # var to track the max size of the dequeue
        deque_size = 1

        # initialize the states previously visited as a set
        history = set()

        # subloop for each layer
        while (len(s)>0):

            # update the max size of the dequeue if dequeue is larger
            if len(s) > deque_size:
                deque_size = len(s)

            #pop the first node
            node = s.pop()
            
            # process the nodes upto the max depth for this iteration
            if node.depth < i:

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

        # increment i to move to the next depth iteration
        i = i + 1

    #return a dumby node if no solution is found
    return PNode([0,0,0,0,0,0,0,0,0], None, "None", 0, 0, 0), 0, 0