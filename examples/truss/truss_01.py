# -*- coding: utf-8 -*-
# ***********************************
#  Author: Pedro Jorge De Los Santos     
#  E-mail: delossantosmfq@gmail.com 
#  Blog: numython.github.io
#  License: MIT License
# ***********************************
from nusa._experimental import *

"""
Logan, D. (2007). A first course in the finite element analysis.
Example 3.1, pp. 70.
"""
# Input data 
E = 30e6 # psi
A = 2.0 # in^2
P = 10e3 # lbf
L = 10*(12.0)  # ft -> in
L2 = np.sqrt(L**2 + L**2) # in
# Model
m = TrussModel("Truss Model")
# Nodes
n1 = Node((0,0))
n2 = Node((0,120))
n3 = Node((120,120))
n4 = Node((120,0))
# Elements
kdg = np.pi/180.0
e1 = Truss((n1,n2),E,A,90*kdg)
e2 = Truss((n1,n3),E,A,45*kdg)
e3 = Truss((n1,n4),E,A,0*kdg)

# Add elements 
for nd in (n1,n2,n3,n4):
    m.addNode(nd)
for el in (e1,e2,e3):
    m.addElement(el)

m.buildGlobalMatrix()
m.addForce(n1,(0.0,-P))
m.addConstraint(n2,ux=0,uy=0) # fixed 
m.addConstraint(n3,ux=0,uy=0) # fixed
m.addConstraint(n4,ux=0,uy=0) # fixed
m.plot_model()
m.solve() # Solve model
m.show()
