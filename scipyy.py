# scipy stands for scientific python

import sys
import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

import scipy
from scipy import constants

print(constants.liter)
# checking scipy version
print(scipy.__version__)
# scipy constants
# PI is an example of scipy constants
print(constants.pi)
# a list ofvll units under the constants can be seen using the dir() function
print(dir(scipy))
print(dir(constants))
print(constants.centi)
print(constants.yotta)    #1e+24
print(constants.zetta)    #1e+21
print(constants.exa)      #1e+18
print(constants.peta)     #1000000000000000.0
print(constants.tera)     #1000000000000.0
print(constants.giga)     #1000000000.0
print(constants.mega)     #1000000.0
print(constants.kilo)     #1000.0
print(constants.hecto)    #100.0
print(constants.deka)     #10.0
print(constants.deci)     #0.1
print(constants.centi)    #0.01
print(constants.milli)    #0.001
print(constants.micro)    #1e-06
print(constants.nano)     #1e-09
print(constants.pico)     #1e-12
print(constants.femto)    #1e-15
print(constants.atto)     #1e-18
print(constants.zepto)    #1e-21
# these return the specified units in bytes
print(constants.kibi)  #1024
print(constants.gram) # return it in kg
print(constants.degree) # return the unit in radians 0.017453292519943295
# finly we conclude that the constant will return the specified unit in basic unit i.e; gram,milli-gram etc into kilogram
'''
*force into newton
*power into watts
*temperature into kelvin
*speed into metre per second
*volume into cubic meter
*area into square metre
*
*length into metre
*time into seconds
*angle into radians
*mass into kg
*binary into bytes
'''
# scipy optimizer
from scipy.optimize import root
from math import cos
def eqn(x):
    return x + cos(x)
# first argument defines a function  representing an equation
# 2nd argument represent intial guess for the root

myroot=root(eqn,0)
print(myroot.x)
print(myroot)
# high points are called maxima
# low points are called minima
# the highest point is called global maxima whereas the rest of the points are called local maxima
# the lowest point is called global minima whereas the rest of the points are called lcoal minima
# minimize the function
from scipy.optimize import minimize
def eqn(x):
    return x**2 +x+2
mymin=minimize(eqn,0,method='BFGS')
print(mymin)
# scipy sparse data:that has mostly unused elements(elements that does not carry any information)
# dense array is the opposite of sparse array
'''
there are two types of sparse matrices that we use
CSC- compressed sparse column
CSR-compressed sparse row
first create CSR
'''
from scipy.sparse import csr_matrix
import numpy as np
arr=np.array([0,0,0,0,0,1,1,0,2])
print(csr_matrix(arr))
# viewing stored data(not the zero items) with the data property
arr1=np.array([[0,0,0],[0,0,1],[1,0,2]])
print(csr_matrix(arr1).data)
# counting non zero with the count_nonzero() method
print(csr_matrix(arr1).count_nonzero())
# romoving zero-entries from the matrix with the eliminate_zero() method
print(csr_matrix(arr1).sum_duplicates())
# converting the csr to csc with tocsc() method
print(csr_matrix(arr1).tocsc())
# scipy graphs
from scipy.sparse.csgraph import connected_components
arr2=np.array([
    [0,1,2],
    [1,0,0],
    [2,0,0]
])
newarr=csr_matrix(arr2)
print(connected_components(arr2))
from scipy.sparse.csgraph import dijkstra
newarr=csr_matrix(arr2)
# use the dijktra method to find the shortest path 
print(dijkstra(newarr,return_predecessors=True,indices=0))
# use the floyd_warshall() method to find the shortest path between all pairs of elements
from scipy.sparse.csgraph import floyd_warshall
newarr1=csr_matrix(arr2)
print(floyd_warshall(newarr,return_predecessors=True))
# bellman_ford() method can also find the shortest path between all pairs of elements like floyd_warshall() method but this method can handle negetive weight as well
from scipy.sparse.csgraph import bellman_ford

arr3 = np.array([
  [0, -1, 2],
  [1, 0, 0],
  [2, 0, 0]
])
newarr2=csr_matrix(arr3)
print(bellman_ford(newarr,return_predecessors=True,indices=0))
# the depth_first_order() method returns a depth first traversal from a node
from scipy.sparse.csgraph import depth_first_order
arr4 = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])
newarr4=csr_matrix(arr4)
print(depth_first_order(arr4,1))
# breath_first_order() method returns a breadth first traversal from a node
from scipy.sparse.csgraph import breadth_first_order
newarr5=csr_matrix(arr4)
print(breadth_first_order(newarr5,1))
# scipy spatial data
#Three lines to make our compiler able to draw:






