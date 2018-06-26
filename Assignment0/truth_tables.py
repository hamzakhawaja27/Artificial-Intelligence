""" File name:   truth_tables.py
    Author:      hamza khawaja u6019739
    Date:        <the date goes here>
    Description: This file defines a number of functions which implement Boolean
                 expressions.
                 
                 It also defines a function to generate and print truth tables
                 using these functions.
                 
                 It should be implemented for Exercise 2 of Assignment 0.
                 
                 See the assignment notes for a description of its contents.
"""



def boolean_fn1(a,b,c):
    return (not(a or b) or ((not a) and (not b)))

def boolean_fn2(a,b,c):
    return ((a and b) or ((not a) and (not b)))

def boolean_fn3(a,b,c):
    return ((not c) or a) and ((a and not b) or ((not a) and b))

def draw_truth_table(boolean_fn):
    print("a           b            c             res")
    print("------------------------------------------")
    L=[True,False]
    M=[True,False]
    N=[True,False]
    for i in L:
        for j in M:
            for k in N:
                final=boolean_fn(i,j,k)
                print("{}       {}        {}         {}".format(out(i),out(j),out(k),out(final)))

def out(i):
    if i==True:
        return "True "
    else:
        return "False"
        



