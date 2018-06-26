""" File name:   dfa.py
    Author:      <Khawaja Hamza u6019739>
    Date:        <the date goes here>
    Description: This file defines a function which reads in
                 a DFA described in a file and builds an appropriate datastructure.
                 
                 There is also another function which takes this DFA and a word
                 and returns if the word is accepted by the DFA.
                 
                 It should be implemented for Exercise 3 of Assignment 0.
                 
                 See the assignment notes for a description of its contents.
"""
## using dictionay of dictionaries to represent data.
def load_dfa(dfa_file_name):
    file=open(dfa_file_name,'r')
    line_count=0
    inner_dict={}
    outer_dict={}
    l=[]
    list_reuse=[]
    for line in file:
        line_count=line_count+1;
        if line_count==1:
            initial_state=line.split()[1]
        elif line_count==2:
            accepting_states=line.split()[1:];
        else:
            temp=line.split()
            key=temp[1]
            if key in outer_dict.keys():
                inner_dict_temp={}
                inner_dict_temp=outer_dict[key]
                inner_dict_temp[temp[3]]=temp[2]
                outer_dict[key]=inner_dict_temp
            else:
                inner_dict_temp={}
                inner_dict_temp[temp[3]]=temp[2]
                outer_dict[key]=inner_dict_temp


    final_list=[initial_state,accepting_states,outer_dict]

    return final_list
            






def accepts_word(dfa, word):

    state=dfa[0]
    accepting_states=dfa[1]
    outer_dict=dfa[2]

    
    for alpha in word:
        if state in outer_dict.keys():
            inner_dict=outer_dict[state]
            if alpha in inner_dict.keys():
                state=inner_dict[alpha]
                print(state)
            else:
                return "not passed"
        else:
            return "not passed"
    if state in accepting_states:
        return "Passed"
    else:
        return "not passed"

        








