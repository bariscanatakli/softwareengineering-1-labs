#quadratic formula

import sys # for get input from command-line
import math

a = int(sys.argv[1])

b = int(sys.argv[2])

c = int(sys.argv[3])

delta = (math.pow(b,2)) - (4*a*c)


def getRootFirst(a,b,c):
    firstRoot = (-b -(math.pow(delta,0.5)))/a/2
    

    return firstRoot
def getRootSecond(a,b,c):
    
    secondRoot = (-b +(math.pow(delta,0.5)))/a/2

    return secondRoot

if delta > 0: # if delta greater than zero, that means there are 2 roots.
   print("Roots are 'x1: {0}, x2: {1}'".format(getRootFirst(a,b,c),getRootSecond(a,b,c)))
elif delta == 0: # if delta equals to zero, there are two roots actually but they are same.(Duplicated, Repeated)
    print("Roots are 'x1: {0}'".format(getRootSecond(a,b,c))) 
else: # there is no root
    print("There is no root.")