
"""
COMP3620-6320 Artificial Intelligence 2017 - Planning Assignment Q2

Enter your details below:

Name:
Student Code:
email:


Implements the A* (a-star) search algorithm for planning.

Method to be implemented is a_star.

We import some basic data-structure that can be useful to tackle the problem.
Have a look at *heapq* that is an efficient implementation of a priority queue using a heap data-structure
Have a look at searchspace that gives you an implementation of a searchnode. In particular look at make_root_node and make_child_node
"""

import heapq
import logging

from search import searchspace
import frontiers
from planning_task import Task
from heuristics import BlindHeuristic



def a_star(task, heuristic=BlindHeuristic):
    expandedNodes=0 ## couting the number of nodes
    flag=0
    Que= frontiers.PriorityQueue() ## stack que for saving nodes
    root_node=searchspace.make_root_node(task.initial_state) ## creating nodes out of vertices.
    h_root_node=heuristic(root_node) ## creating a node containing its heuristic values.
    Que.push(root_node,root_node.g + h_root_node)
    node_dict1=dict() ## dictionary to save nodes based on their cost.
    node_dict1[root_node.state]=(root_node.g + h_root_node)

    '''
    A loop to traverse the priority que in order to find the best solution.
    '''
    while not (Que.is_empty()):
        node=Que.pop()
        expandedNodes=expandedNodes+1
        succ_act_state_list=task.get_successor_states(node.state)
        for succ_tuple in succ_act_state_list:
            succ_node=searchspace.make_child_node(node,succ_tuple[0],succ_tuple[1])
            if task.goal_reached(succ_node.state):
                last_node=succ_node
                flag=1
                break
            else:
                h_succ_state=heuristic(succ_node)
                if (succ_node.state in node_dict1.keys()):
                    if (node_dict1[succ_node.state]> (succ_node.g + h_succ_state)):
                        node_dict1[succ_node.state]=succ_node.g + h_succ_state
                        Que.change_priority(succ_node,succ_node.g + h_succ_state)
                else:
                    node_dict1[succ_node.state]=succ_node.g + h_succ_state
                    Que.push(succ_node,succ_node.g + h_succ_state)
        if flag==1:
            break

    current_node=last_node
    action_list=[]
    '''
    Finding the most optimal path to the solution. 
    '''
    while current_node!=root_node:
        action_list.append(current_node.action)
        current_node=current_node.parent

    action_list.reverse()
    print("Expanded Nodes= ",expandedNodes)
    return action_list






    """
    Searches for a plan in the given task using A* search.

    @param task The task to be solved
    @param heuristic  A heuristic callable which computes the estimated steps
                      from a search node to reach the goal.
    """
#    raise NotImplementedError
