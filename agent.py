# Student: Corey Glodek
# Class: CSC 480 
# Assignment 1: Modified 8 tile puzzle
# 
# Main Program Agent

# import the agent methods
from bfs import bfs
from dfs import dfs
from iterative_deepening import iddfs
from a_star import a_star

# Hard coding the difficulty sequences
easy = [1,3,4,8,6,2,7,0,5]
medium = [2,8,1,0,4,3,7,6,5]
hard = [5,6,7,4,0,8,3,2,1]

# bool for the main while loop
quit = False

# method for iterating though the solution sequence and printing the results
def results(node, hist, q):
    i = 0

    # If the dumby node is detected this informs the user that no solution was found
    if node.state == [0,0,0,0,0,0,0,0,0]:
        print("No solution was found.")
        return

    # calling solution info from the goal node
    path_moves, path_cost, path_total_cost, path_states = node.solution()
                
    while i in range(len(path_moves)):
        if i == 0:
            print("\nInitial State:\n    ", str(path_states[i][0:3])+'\n     '+ str(path_states[i][3:6])+ '\n     '+ str(path_states[i][6:9]))
        elif i == len(path_moves)-1:
            print("\nFinal State:\n    ", str(path_states[i][0:3])+'\n     '+ str(path_states[i][3:6])+ '\n     '+ str(path_states[i][6:9]))
        else:
            print("\nState:\n    ", str(path_states[i][0:3])+'\n     '+ str(path_states[i][3:6])+ '\n     '+ str(path_states[i][6:9]))
        print("Move: ", path_moves[i])
        print("Cost: ", path_cost[i])
        print("Total Cost: ", path_total_cost[i])
        print("Depth: ", i)

        i = i + 1

    print("\nMax Length of history: ", hist)
    print("Max size of the queue: ", q)
    print("Max Depth: ", node.depth)
    return

# main loop 
while quit is False:
    print("\n*************************************\nWelcome to the 8 tile Puzzle Program.\n*************************************\n")
    
    #initializing the main vars
    agent_type = ""
    difficulty = 0
    max_depth = 0
    agent_dict = {"BFS": bfs, "DFS": dfs, "IDDFS": iddfs, "UCS": a_star, "BESTFS": a_star, "A*1": a_star, "A*2": a_star, "A*3": a_star}
    diff_dict = {"E" : easy, "M" : medium, "H": hard}

    # ask the user for the type of agent to use for processeing
    while not agent_type in ("BFS","DFS","IDDFS","UCS","BESTFS","A*1","A*2","A*3"):

        agent_type = input("""Which agent would you like to use?: \n     Breadth First Serch (BFS), 
     Depth First Search (DFS), \n     Iterative Deepening (IDDFS), \n     Uniform Cost (UCS), 
     Best First (BESTFS), \n     A*1 (A*1), \n     A*2 (A*2), \n     A*3 (A*3)\n""")

    # ask user for a maximum depth if Iterative Deepening is the agent
    if agent_type == "IDDFS":
        while max_depth == 0:
            max_depth = input("What would you like as a max depth for Iterative Deepening? (Please pick an integer): ")
            if not max_depth.isnumeric: 
                print("please try again.")
                max_depth = 0
            else:
                max_depth = int(max_depth)

    # ask user for difficulty level
    while not difficulty in ("E","M","H"):
        difficulty = input("What difficulty would you like to run? Easy (E), Medium (M), or Hard (H): ")
    
    # assign the heuristic value if one of the agents using a priority queue is selected
    if agent_type == "UCS":
        heuristic = 4
    elif agent_type =="BESTFS":
        heuristic = 0
    elif agent_type == "A*1":
        heuristic = 1
    elif agent_type == "A*2":
        heuristic = 2
    elif agent_type == "A*3":
        heuristic = 3

    # assign the agent type and difficulty
    agent_type = agent_dict[agent_type]
    difficulty = diff_dict[difficulty]

    # agent call for processing
    if agent_type == iddfs:
        run_agent, history, queue_size = agent_type(difficulty,max_depth) #Need to add a response if no solution was found
    elif agent_type == a_star:
        run_agent, history, queue_size = agent_type(difficulty,heuristic)
    else:
        run_agent, history, queue_size = agent_type(difficulty)
    
    #print the solution if one exists
    results(run_agent, history,queue_size)

    # ask the user if they would like to continue
    end_prog = input("\nWould you like to run another agent? \nPress any key to continue or Q to quit: ")
    if end_prog =="Q":
        quit = True
