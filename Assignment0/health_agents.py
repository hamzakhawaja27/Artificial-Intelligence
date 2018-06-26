""" File name:   health_agents.py
    Author:      <hamza khawaja u6019739>
    Date:        <the date goes here>
    Description: This file contains agents which fight disease. It is used
                 in Exercise 4 of Assignment 0.
"""

import random
import copy
class HealthAgent(object):
    """ A simple disease fighting agent. """
    
    def __init__(self, locations, conn):
        """ This contructor does nothing except save the locations and conn.
            Feel free to overwrite it when you extend this class if you want
            to do some initial computation.
            
            (HealthAgent, [str], { str : set([str]) }) -> None
        """
        self.locations = locations
        self.conn = conn

    def choose_move(self, location, valid_moves, disease, threshold, growth, spread):
        """ Using given information, return a valid move from valid_moves.
            Returning an inalid move will cause the system to stop.
            
            Changing any of the mutable parameters will have no effect on the operation
            of the system.
            
            This agent will locally move to the highest disease, of there is
            is no nearby disease, it will act randomly.
            
            (HealthAgent, str, [str], [str], { str : float }, float, float, float) -> str  
        """
        max_disease = None
        max_move = None
        for move in valid_moves:
           if max_disease is None or disease[move] > max_disease:
               max_disease = disease[move]
               max_move = move
        
        if not max_disease:
            return random.choice(valid_moves)
        
        return max_move
        
#Make a new agent here called SmartHealthAgent, which extends HealthAgent and acts a bit more sensibly

class SmartHealthAgent(HealthAgent):
    """ A simple disease fighting agent. """
    
    def __init__(self, locations, conn):
        """ This contructor does nothing except save the locations and conn.
            Feel free to overwrite it when you extend this class if you want
            to do some initial computation.
            
            (HealthAgent, [str], { str : set([str]) }) -> None
        """
        self.locations = locations
        self.conn = conn

    def choose_move(self, location, valid_moves, disease, threshold, growth, spread):
        """ Using given information, return a valid move from valid_moves.
            Returning an inalid move will cause the system to stop.
            
            Changing any of the mutable parameters will have no effect on the operation
            of the system.
            
            This agent will locally move to the highest disease, of there is
            is no nearby disease, it will act randomly.
            
            (HealthAgent, str, [str], [str], { str : float }, float, float, float) -> str  
        """
        max_disease = None
        max_move = None
        All_max_neib=[]
        for move in valid_moves:
           if max_disease is None or disease[move] > max_disease:
               max_disease = disease[move]
               max_move = move
        if not max_disease:    
            return bfirst(location,self.conn,disease,spread)
## bfirst function perform breadth first
## algorithm and returns the shortest path to the maximum diseased area
        return max_move
        


def bfirst(location,conn,disease,spread):
    agent_loc=location
    max_disease=0
    max_disease_loc2=[]
    for key in disease:
        if disease[key]> max_disease:
                max_disease_loc=key
                max_disease_value=disease[key]
   
    max_conn=0
    for key in disease:
        if disease[key]==max_disease_value:
            if len(conn[key])>max_conn:
                max_conn=len(conn[key])
                output_location=key

    max_disease_loc=output_location
    
        
    neb=conn[agent_loc]
    b_list=[agent_loc]
    for nn in neb:
        b_list.append(nn)
    
    path=[]

    for b in b_list:
        l=[b]
        path.append(l)
        
    for node in b_list:
        neb=conn[node]
        neb1=list(neb)
        
        for n in neb1:
            if n not in b_list:
                for ll in path:
                    temp=[]
                    if ll[len(ll)-1]==node:
                        temp=copy.deepcopy(ll)
                        temp.append(n)
                        path.append(temp)
                b_list.append(n)
                if n==max_disease_loc:
                    break
        if n==max_disease_loc:
            break


    jump_loc=''
    for p_list in path:
        if max_disease_loc in p_list:
            jump_loc=p_list[0]
            break

    return jump_loc


        
