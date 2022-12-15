# Modified 8 tile puzzle
# 
# Node class for the 8tile puzzle

class PNode:
    #goal state for checking
    goal = [1,2,3,8,0,4,7,6,5]

    #construct the node
    def __init__(self, state, parent, move, cost, total_cost, depth):
        self.parent = parent
        self.state = state
        self.move = move
        self.cost = cost
        self.depth = depth

        #Update total cost of a node upon construction
        if parent:
            self.total_cost = parent.total_cost + cost
            self.depth = parent.depth + 1
        else:
            self.total_cost = cost

    # to string -> print the state, used mostly for debugging
    def __str_(self):
        return str(self.state)
    
    def __hash__(self):
        return hash(str(self))

    #quick check for if goal state has been reach
    def match_goal(self):
        if self.state == self.goal:
            return True
        else:
            return False

    # method to calculate the h_cost to be returned for use by the priority queue
    def h_rack_stack(self, h_state):

        #h_state values of:
        # 4 identifies Uniform Cost, 
        # 0  identifies Best First, 
        # 1   identifies A*1,  
        # 2   identifies A*2, 
        # 3   identifies A*3

        if h_state == 0 or h_state == 1 or h_state == 3:

            out_o_place = 0
            i = 0

            #calc the number of tiles out of place
            for i in range(len(self.goal)):
                if self.state[i] != self.goal[i]:
                    out_o_place = out_o_place + 1
    
        # calcs the manhattan distance
        if h_state == 3 or h_state == 2:
            
            manhattan_distance = 0
            i = 0 

            for i in range(len(self.goal)):
                if self.state[i] != self.goal[i]:

                    #returns the location of the current state [i]
                    temp = self.goal.index(self.state[i])
                    
                    y_current = int(i / 3)
                    x_current = int(i % 3)

                    y_goal = int(temp / 3)
                    x_goal = int(temp % 3)

                    manhattan_distance = manhattan_distance + abs(y_current-y_goal)+abs(x_current-x_goal)
        
        # Uniform Cost 
        if h_state == 4:
            return self.total_cost
        
        # Best First 
        elif h_state == 0:
            return out_o_place
        
        # A*1
        elif h_state == 1:
            return out_o_place + self.total_cost
        
        # A*2
        elif h_state == 2:
            return manhattan_distance + self.total_cost

        # A*3
        elif h_state == 3:
            return manhattan_distance + out_o_place + self.total_cost

        return


    #overloading the comparators to allow the priority queue to evaluate properly: less than, greater than, and equals
    def __lt__(self, other):
        return self.total_cost < other.total_cost
    
    def __gt__(self, other):
        return self.total_cost > other.total_cost

    def __eq__(self, other):
        if(other == None):
            return False
        return self.total_cost == other.total_cost

    #Method to find all the children of the node
    def find_children(self):
        #initialize empty list for all children found
        children = []
        
        #find the location in the array of tile 0
        temp = self.state.index(0)

        #finds the location of tile 0 in relation to a 3x3 board
        y = int(temp / 3)
        x = int(temp % 3)
        
        #return all available moves basedon the location of tile 0
        available_moves = self.find_moves(y,x)

        #iterate through the available moves
        for move in available_moves:
            #create a copy of the current state for creating the new child
            temp_state = self.state.copy()

            #based on a valid move swap positions of tile 0 and the tile to be moved and update the cost
            if move == "Up":
                temp_state[temp], temp_state[temp-3] = temp_state[temp-3], temp_state[temp]
                temp_cost = int(temp_state[temp])

            if move == "Down":
                temp_state[temp], temp_state[temp+3] = temp_state[temp+3], temp_state[temp]
                temp_cost = int(temp_state[temp])

            if move == "Left":
                temp_state[temp], temp_state[temp-1] = temp_state[temp-1], temp_state[temp]
                temp_cost = int(temp_state[temp])

            if move == "Right":
                temp_state[temp], temp_state[temp+1] = temp_state[temp+1], temp_state[temp]
                temp_cost = int(temp_state[temp])

            #add the child to the list with the current node as the parent
            #Note: total cost and depth are updated upon creation of the node
            children.append(PNode(temp_state,self,move,temp_cost,self.total_cost,self.depth))

        return children

    #Method to find valid moves based on position of tile 0 and removes invalid moves, if any
    @staticmethod
    def find_moves(y,x):
        moves = ["Left", "Right", "Up", "Down"]

        if y == 0:
            moves.remove("Up")
        elif y == 2:
            moves.remove("Down")
        if x == 0:
            moves.remove("Left")
        elif x == 2:
            moves.remove("Right")
        
        return moves
    
    #method to return the solution path, sequence of moves, cost of the move, total cost to that point, and the current state
    def solution(self):
        solution_path = []
        solution_cost = []
        solution_total_cost = []
        solution_state = []

        #add current state details
        solution_path.append(self.move)
        solution_cost.append(self.cost)
        solution_total_cost.append(self.total_cost)
        solution_state.append(self.state)

        #copy of the current node for iteration
        path = self

        #Iterate through the parents starting with the current node and add the details to each list
        while path.parent != None:
            path = path.parent
            solution_path.append(path.move)
            solution_cost.append(path.cost)
            solution_total_cost.append(path.total_cost)
            solution_state.append(path.state)

        #reverse the order of the lists to facilitate ease of printing
        solution_path.reverse()
        solution_cost.reverse()
        solution_total_cost.reverse()
        solution_state.reverse()

        return solution_path, solution_cost, solution_total_cost, solution_state




        

