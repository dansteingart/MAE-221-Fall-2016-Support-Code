##Author: Dan Steingart
##Date Started: 2016-09-19
##Notes: MS Problem 2.46
from pithy import *

#make a pretty print helper function
#We give it the variable and the unit and it makes a nicely printed relationship.  Purely for display.
def pp(val,unit): print "%s = %.1f %s" %(val,eval(val),unit)

#Step 1: Digest the givens
A = 70 * (.01)**2# m^2
Tb = 340 #K
Tf = 300 #K
h_low = 25 #W/(m^2 K)
h_high = 250 #W/(m^2 K)

#Step 2: Find the bounds for Q
Q_dot_low = -h_low*A*(Tb-Tf)
Q_dot_high = -h_high*A*(Tb-Tf)

pp('Q_dot_low','W')
pp('Q_dot_high','W')

print "These values assume that the processor is consuming at least 7 W or 70 W, respectively.  <b>There cannot be more heat removed from the chip than the processor is consuming!</b>"