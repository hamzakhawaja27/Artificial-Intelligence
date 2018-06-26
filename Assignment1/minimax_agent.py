# minimax_agent.py
# --------------
# COMP3620/6320 Artificial Intelligence
# The Australian National University
# For full attributions, see attributions.txt on Wattle at the end of the course

"""
    Enter your details below:

    Name: Hamza khawaja
    Student Code: u6019739
    email: u6019739@anu.edu.au
"""

from agents import Agent
import util
from copy import deepcopy

from search_problems import AdversarialSearchProblem


class MinimaxAgent(Agent):
    """ The agent you will implement to compete with the black bird to try and
        save as many yellow birds as possible. """

    def __init__(self, max_player, depth="2"):
        """ Make a new Adversarial agent with the optional depth argument.
            (MinimaxAgent, str) -> None
        """
        self.max_player = max_player
        self.depth = int(depth)

    def evaluation(self, problem, state):
        """
            (MinimaxAgent, AdversarialSearchProblem,
                (int, (int, int), (int, int), ((int, int)), number, number))
                    -> number
        """
        player, red_pos, black_pos, yellow_birds, score, yb_score = state
        number=0
        min_number=0

        temp=0
        list_number=[]
        if len(yellow_birds)>0 and len(yellow_birds)<10:
            for y in yellow_birds:
                number=number+problem.maze_distance(red_pos, y)
                for yy in yellow_birds:
                    number=number+problem.maze_distance(y, yy)
                list_number.append(number)
            min_number=min(list_number)
            min_number = min_number / len(yellow_birds)
        elif len(yellow_birds)>10:
            for y in yellow_birds:
                number=number + problem.maze_distance(red_pos, y)
            min_number=number
            min_number = min_number / len(yellow_birds)

            

        number3=0
           
        list_distance=[]
        min_dist=1
        if len(yellow_birds)>0:
            for y in yellow_birds:
                list_distance.append(problem.maze_distance(red_pos, y))
            min_dist=min(list_distance)

        number4=problem.maze_distance(red_pos, black_pos)

        temp=0
        number1=0
        number2=0

            
        number2=problem.maze_distance(red_pos, black_pos)
        if number2<2:
            score = score + yb_score - min_number + number3 + (1/min_dist) - 250

        else:
            score = score + yb_score - min_number + number3 + (1/min_dist) 
        return score

                    

    def maximize(self, problem, state, current_depth):

        player, red_pos, black_pos, yellow_birds, score, yb_score = state
       
        if current_depth == self.depth or problem.terminal_test(state):
            return (self.evaluation(problem, state),"STOP")
        else:
            state_list=[]
            for next_state,action,cost in problem.get_successors( state ) :

                minimum=(self.minimize(problem,next_state,(current_depth+1)),action)
                state_list.append(minimum)
        return max(state_list)
 
        



    def minimize(self, problem, state, current_depth):
        player, red_pos, black_pos, yellow_birds, score, yb_score = state

        if current_depth == self.depth or problem.terminal_test(state):
            return self.evaluation(problem, state)
        else:
            state_list=[]
            for next_state,action,cost in problem.get_successors( state ) :
                maximum=self.maximize(problem,next_state,(current_depth+1))
                state_list.append(maximum)
        return min(state_list)[0]
        



    def get_action(self, game_state):
        """ This method is called by the system to solicit an action from
            MinimaxAgent. It is passed in a State object.

            Like with all of the other search problems, we have abstracted
            away the details of the game state by producing a SearchProblem.
            You will use the states of this AdversarialSearchProblem to
            implement your minimax procedure. The details you need to know
            are explained at the top of this file.
        """
        #We tell the search problem what the current state is and which player
        #is the maximizing player (i.e. who's turn it is now).
        problem = AdversarialSearchProblem(game_state, self.max_player)
        state = problem.get_initial_state()
        utility, max_action = self.maximize(problem, state, 0)
        print("At Root: Utility:", utility, "Action:", max_action, "Expanded:", problem._expanded)
        return max_action





    









                       
