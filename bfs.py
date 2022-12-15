#  Modified 8 tile puzzle
# 
# BFS agent
from p_node import PNode
from queue import Queue

def bfs(starting_state):

    # Initialize the first node with the starting state
    initial_node = PNode(starting_state, None, None, 0, 0, 0)

    # Initialize the queue - FIFO
    q = Queue()

    #add starting node to the queue
    q.put(initial_node)

    # initialize the states previously visited as a set
    history = set()

    current_q = set()
    current_q.add(str(initial_node.state))

    # var to track the max size of the queue
    queue_size = 1

    # main loop for BFS
    while not(q.empty()):

        # update the max size of the queue if queue is larger
        if q.qsize() > queue_size:
            queue_size = q.qsize()
        
        #pop the first node
        node = q.get()
        current_q.discard(str(node.state))
        
        # add the state to the history
        history.add(str(node.state))

        #calling the find children method
        children = node.find_children()
        
        # iterate through the children found
        for child in children:
            
            #check to see if the this state has already been visited
            if str(child.state) not in history and str(child.state) not in current_q:

                # check to see if the current state matches the goal state
                if child.match_goal():
                    return child, len(history), queue_size

                # add the child to the queue
                q.put(child)
                current_q.add(str(child.state))

    #return a dumby node if no solution is found
    return PNode([0,0,0,0,0,0,0,0,0], None, "None", 0, 0, 0), 0, 0
