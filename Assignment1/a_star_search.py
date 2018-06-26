"""
    Enter your details below:

    Name: Khawaja Hamza
    Student Code: u6019739
    email: u6019739@anu.edu.au
"""


import util
import frontiers
from actions import Directions, Actions

def solve(problem,heuristic) :
    """ *** YOUR CODE HERE *** """


    cost=0
    Que= frontiers.PriorityQueue()
    Que.__init__()
    Que1= frontiers.PriorityQueue()
    Que1.__init__()
    pos=problem.get_initial_state()
    node1=CreateNode(pos,(-1,-1),'stop',cost,heuristic,problem)
    Que.push(node1,node1.totalCost)
    Que1.push(node1,node1.totalCost)
    flag=0;
    list_node=[]
    
    while not (Que.is_empty()):
        node=Que.pop();
#        print(node.my_position)
        successors_list=problem.get_successors(node.my_position)
        for successor_tuple in successors_list:
            my_Cost=node.Cost+ successor_tuple[2]
            node_temp=CreateNode(successor_tuple[0],node.my_position,successor_tuple[1],my_Cost,heuristic,problem)
            Redflag=0
            for QueNode in Que1.heap:
                if QueNode[2].my_position==node_temp.my_position and QueNode[2].totalCost<=node_temp.totalCost:
                    Redflag=1
                    break
                else:
                    Redflag=0
                
            if Redflag==0:
                list_node.append(node_temp)  
                if problem.goal_test(node_temp.my_position):
                    node_final=node_temp
                    flag=1
                    break
                else:
                    Que.push(node_temp,node_temp.totalCost)
                    Que1.push(node_temp,node_temp.totalCost)
        if flag==1:
            break
    
    
    direction_list=[node_temp.Action]
    final_list=[node_temp.my_position]
    list_node=[]
    for Q in Que1.heap:
        list_node.append(Q[2])


    while (final_list[len(final_list)-1]!=problem.get_initial_state()):
        for i in range(0,len(list_node)):
            if list_node[i].my_position== node_final.parent_position: 
                final_list.append(list_node[i].my_position)
                node_final=list_node[i]
                if list_node[i].my_position==problem.get_initial_state():
                    break
                direction_list.append(list_node[i].Action)
        
    direction_list.reverse()

    return direction_list



class CreateNode():

    my_position=tuple()
    parent_position=tuple()
    Action=''
    Cost=1.0
    totalCost=0.0
    def __init__(self,w,x,y,z,heuristic,problem):
        self.my_position=w
        self.parent_position=x
        self.Action=y
        self.Cost=z
        self.totalCost=z+heuristic(w,problem)
        
    def pr(self):
        print(self.my_position)
        print(self.parent_position)
        print(self.Action)
        print(self.totalCost)
        print("---------------")
        


    
