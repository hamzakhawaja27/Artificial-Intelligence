
"""
COMP3620-6320 Artificial Intelligence 2017 - Planning Assignment Q1
Classes for representing a STRIPS planning task and capturing its semantics

Enter your details below:

Name:
Student Code:
email:


Implements the Greedy Best First Search (GBFS) search algorithm for planning.

Method to be implemented is gbfs.

We provide imports for some basic data-structure that can be useful to tackle the problem. In particular have a look at heapq that
is an efficient implementation of a priority queue using heap
"""



import heapq
import logging
import frontiers
from search import searchspace
from heuristics import rel_based_heuristics
from planning_task import Task
from heuristics import BlindHeuristic
def gbfs(task, heuristic=BlindHeuristic):
    expandedNodes=0
    flag=0
    Que= frontiers.PriorityQueue()
    root_node=searchspace.make_root_node(task.initial_state)
    heur=heuristic(root_node)
    Que.push(root_node,heur)
    node_dict1=dict()
    node_dict1[root_node.state]=heur
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
                if (succ_node.state in node_dict1):
                    pass
                else:
                    heur=heuristic(succ_node)
                    node_dict1[succ_node.state]=heur
                    Que.push(succ_node,heur)
        if flag==1:
            break
        
    current_node=last_node
    action_list=[]
    while current_node!=root_node:
        action_list.append(current_node.action)
        current_node=current_node.parent

    action_list.reverse()
    print("Expanded Nodes",expandedNodes)
    return action_list
    
