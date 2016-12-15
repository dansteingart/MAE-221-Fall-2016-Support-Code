##Author: Dan Steingart
##Date Started: 2016-09-19
##Notes: MS Problem 2.90

from pithy import *

#make a pretty print helper function
#We give it the variable and the unit and it makes a nicely printed relationship.  Purely for display.
def pp(val,unit): print "%s = %.3f %s" %(val,eval(val),unit)

#Step 1: Digest the givens

#The power input is the work cycle
W_cycle = -0.15 #kW
Q_out = 0.6 #kW

#Step 2
#Using the first law and applying this to cycles
#Q_cycle = W_cycle
#W_cycle = Q_out-Q_in
Q_in = W_cycle + Q_out
pp('Q_in','kW')

#Now find the CoP Beta

beta = abs(Q_in/W_cycle)
pp('beta','')
