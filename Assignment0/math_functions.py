""" File name:   math_functions.py
    Author:      Hamza khawaja u6019739
    Date:        28-02-2017
    Description: This file defines a set of variables and simple functions.
                 
                 It should be implemented for Exercise 1 of Assignment 0.
                 
                 See the assignment notes for a description of its contents.
"""
import math
def math_functions():
    ln_e=math.log(math.e)
    twenty_radians=math.radians(20)

def quotient_ceil(x,y):
   return math.ceil(x/y)


def quotient_floor(x,y):
    return math.floor(x/y)

def manhattan(x1,y1,x2,y2):
    return math.fabs(x2-x1) + math.fabs(y2-y1)



    
#quotient_ceil(0.5,0.2)
#quotient_floor(21,20)
#manhattan(10,10,-10,-10)
#math_functions()
    

    
