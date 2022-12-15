# Modified 8 tile puzzle
# 
# Uniform Cost, Best First, and A* agents

from p_node import PNode
import heapq
from heapq import _siftdown

# method for Uniform Cost, Best First, and A* agents
def a_star(starting_state, h_state):

    # Initialize the first node with the starting state
    initial_node = PNode(starting_state, None, None, 0, 0, 0)

    # Initialize the Heap Priority Queue
    hd = []

    # add starting node to the Heap Priority Queue,
    # total cost was used for the initial node
    heapq.heappush(hd, (initial_node.total_cost, initial_node))
    
    # initialize the states previously visited as a set
    history = set()

    # create a dictionary to track what is in the queue and where
    # this will be used to update any existing entries if a child state matches and is of a lesser value
    heap_dict = {}
    
    # var to track the size of the heap priority queue
    hd_size = 1
      
    # main loop for A* and Best First
    while bool(hd):

        # bool for directing logic if the child already exists in the heap
        exists_in_heap = False

         # update the max size of the var if heap priority queue is larger
        if len(hd) > hd_size:
            hd_size = len(hd) 

        #pop the first node
        node = heapq.heappop(hd)

        # assign the node from the heap priority queue without the priority information
        node = node[1]

        # remove node from the dict if it exists
        if str(node.state) in heap_dict:
            heap_dict.pop(str(node.state))

        # add the state to the history
        history.add(str(node.state))

        #calling the find children method
        children = node.find_children()

        # iterate through the children found
        for child in children:

            # calculate the h_cost based on which search agent was called
            h_cost = child.h_rack_stack(h_state)

            # check if the child is already in the queue
            if str(child.state) in heap_dict:

                # get the value of the child in the dict
                existing_child = heap_dict.get(str(child.state))

                # check if the new child value is less than the existing one
                if h_cost < existing_child:

                    # update the value of the child in the queue
                    hd[existing_child] = (h_cost, child)

                    # bubble the updated node to its correct position
                    _siftdown(hd, existing_child, h_cost)

                    # remove the existing node from the dict
                    heap_dict.pop(str(child.state))

                    # add the updated node to the dict
                    heap_dict[str(child.state)] = h_cost

                    # update the bool
                    exists_in_heap = True

                # check if the two nodes have equal value
                elif h_cost == existing_child:
                    exists_in_heap = True


            #check to see if the this state has already been visited
            if str(child.state) not in history: #and child not in hd:

                # check to see if the current state matches the goal state
                if child.match_goal():
                    return child, len(history), hd_size
                
                # add the child to the priority queue and dict based on the h_cost if it does not exist in the heap
                if not exists_in_heap:
                    heapq.heappush(hd, (h_cost, child))
                    heap_dict[str(child.state)] = h_cost

    #return a dumby node if no solution is found
    return PNode([0,0,0,0,0,0,0,0,0], None, "None", 0, 0, 0), 0, 0
