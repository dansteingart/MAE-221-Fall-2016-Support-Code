##Author: Dan Steingart
##Date Started: 2016-09-19
##Notes: MS Problem 2.80

from pithy import *

#make a pretty print helper function
#We give it the variable and the unit and it makes a nicely printed relationship.  Purely for display.
def pp(val,unit): print "%s = %.3f %s" %(val,eval(val),unit)

#Step 1: Digest the givens

p3 = 140e3 #Pa
V3 = 0.028 #m^3
V2 = V3
p1 = p3

W31 = 10.5e3 #J
Wcycle = -8.3e3 #J 
W23 = 0 #J => constant volume process

#Step 2: Find the requested properties.

print "Part A) find V1"
#we know that step 3-1 is constant pressure, and we know the work done in this step, so

#W31 = p3*(V1 - V3) =>

V1 = (W31/p3)+V3
pp("V1","m^3")

print 
print "Part B) Find Q and W for process 1-2"

#since U1 = U2, and Q-W = Delta U
#Delta U = 0 so Q = W
#We know that Wcycle = W12 + W23 + W31, so we can solve
W12 = Wcycle - W23 - W31
pp("W12","J")
Q12 = W12
pp("Q12","J")

print
print "Part C) What kind of cycle is this, and what is the metric we can use to determine efficacy?"
print "Since Wcycle is negative, this must be a heat pump or cooling cycle, so we need to determine a COP"

#Since Q12 is negative, Q must be leaving the system.  So as a heat pump we can say
Qout = Q12
gamma = Qout/Wcycle
pp("gamma","")
