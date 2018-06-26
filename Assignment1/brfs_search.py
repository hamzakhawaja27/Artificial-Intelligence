"""
    Enter your details below:

    Name: Khawaja Muhammad Hamza
    Student Code: U6019739
    email: u6019739@anu.edu.au
"""

import util
import frontiers
from actions import Directions, Actions

def solve(problem) :
    """ *** YOUR CODE HERE *** """


    cost=1
    Que= frontiers.Queue()
    Que.__init__()
    pos=problem.get_initial_state()
    node1=(pos,'stop',cost)
    Que.push(node1)
    flag=0;
    list_node=[]
    
    while not (Que.is_empty()):
        node=Que.pop();
        successors_list=problem.get_successors(node[0])
        for successor_tuple in successors_list:
            if successor_tuple not in Que.contents:
                suc_pos=successor_tuple[0]
                node_me=CreateNode(suc_pos,node[0],successor_tuple[1])
                list_node.append(node_me)
                if problem.goal_test(suc_pos):
                    print("I have achieved my goal")
                    node_final=node_me
                    flag=1
                    break
                else:
                    Que.push(successor_tuple)
        if flag==1:
            break
    direction_list=[node_final.Action]
    final_list=[node_final.my_position]
    print(problem.get_initial_state())
    while (final_list[len(final_list)-1]!=problem.get_initial_state()):
        for i in range(0,len(list_node)):
            if list_node[i].my_position== node_final.parent_position: 
                final_list.append(list_node[i].my_position)
                node_final=list_node[i]
                if list_node[i].my_position==problem.get_initial_state():
                    break
                direction_list.append(list_node[i].Action)
        
    direction_list.reverse()
    print(final_list)
    print(direction_list)


    return direction_list



class CreateNode():

    my_position=tuple()
    parent_position=tuple()
    Action=''

    def __init__(self,x,y,z):
        self.my_position=x
        self.parent_position=y
        self.Action=z

    def pr(self):
        print(self.my_position)
        print(self.parent_position)
        print(self.Action)
        print("---------------")
        

    
        
        



    
#    util.raise_not_defined() #Remove this line when you have implemented BrFS
