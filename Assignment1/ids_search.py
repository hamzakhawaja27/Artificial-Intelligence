"""
    Enter your details below:

    Name: Khawaja Muhammad Hamza
    Student Code: u6019739
    email: u6019739@anu.edu.au
"""

import util

# Check assignment handout for further details and explanations.


def solve(problem):
    final=getDir(problem)
    return final



def getDir(problem):
    list_node=Sys(problem)
    lastNode=list_node[-1]
    direction_list=[lastNode.Action]
    final_list=[lastNode.state]
    while (final_list[len(final_list)-1]!= problem.get_initial_state()):
        for i in range(0,len(list_node)):
            if list_node[i].state== lastNode.parent and list_node[i].pathCost==(lastNode.pathCost-1):
                final_list.append(list_node[i].state)
                lastNode=list_node[i]
                if list_node[i].state==problem.get_initial_state():
                    break
                direction_list.append(list_node[i].Action)
        
    direction_list.reverse()



    return direction_list
    

def Sys( problem ) :
    """ *** YOUR CODE HERE *** """
    N=1
    limit=1
    while N:
        result,N_explored_list=DLS(problem,limit)
        if result != "cut off" and result!="Failure":
            print("The lower-bound =",limit)
            return N_explored_list
        limit=limit+1
        


def DLS(problem,limit):
    a=problem.get_initial_state()
    b=(-1,-1)
    c=0
    d=0
    e=''
    Initial_Node=MakeNode(a,b,c,d,e)
    explored_list=[]
    N_explored_list=[]
    explored_list.append(Initial_Node.state)
    N_explored_list.append(Initial_Node)
    result= RecursiveDLS(Initial_Node,problem,limit,explored_list,N_explored_list)
    return result,N_explored_list

def RecursiveDLS(Node,problem,limit,explored_list,N_explored_list):
    cutoff=False
    if problem.goal_test(Node.state):
        return Node
    elif Node.depth==limit:
        return "cut off"
    else:
        succ_nodes=Expand(Node,problem)
        new_succ_nodes=set()
        for s in succ_nodes:
            flag=0
            for ll in N_explored_list:
                if ll.state==s.state and ll.pathCost<=s.pathCost:
                    flag=1
                    break
            if flag==0:
                new_succ_nodes.add(s)

        for succ_node in new_succ_nodes:
            explored_list.append(succ_node.state)
            N_explored_list.append(succ_node)
            result=RecursiveDLS(succ_node,problem,limit,explored_list, N_explored_list)
            if result == "cut off" or result == "Failure":
                cutoff=True
            else:
                return result
        if cutoff==True:
            return "cut off"

    return "Failure"
    


class MakeNode():

    state=tuple()
    parent=tuple()
    depth=int
    pathCost=int
    Action=''

    def __init__(self,a,b,c,d,e):
        self.state=a
        self.parent=b
        self.depth=c
        self.pathCost=d
        self.Action=e

    def test_print(self):
        print(self.state)
        print(self.parent)
        print(self.Action)
        print("---------------")
        

def Expand(Node,problem):
    successor_nodes=set()
    successors=problem.get_successors(Node.state)
    if len(successors)==0:
        return successor_nodes
    else:
        for success_tuple in successors:
            a=success_tuple[0]
            b=Node.state
            c=Node.depth + 1
            d=Node.pathCost + success_tuple[2]
            e=success_tuple[1]
            New_Node=MakeNode(a,b,c,d,e)
            successor_nodes.add(New_Node)

        return successor_nodes




            
        
        
    





    
            
