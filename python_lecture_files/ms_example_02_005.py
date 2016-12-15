##Author: Dan Steingart
##Date Started: 2016-09-01
##Notes: Solution to MS Example 2-5

from pithy import *

#make a pretty print helper function
#We give it the variable and the unit and it makes a nicely printed relationship.  Purely for display.
def pp(val,unit): print "%s = %.1f %s" %(val,eval(val),unit)

#Step 1: Clearly state given aspects of the problem

#A computer chip generates some heat during operation due to the sum of the resistance of its internal components.  We are told the power into the chip, the temperature of the cooling fluid, and the heat transfer coefficient.  We are asked to find the surface temperature of the chip.

h = 150 #W/(m^2 K) -> heat transfer coefficient
A = 0.005**2 #m^2 -> chip area
Tf = 273.15+20 #K -> temperature of the ambient air
W_dot = -0.225 # W



# Our first law balance, in steady state, tells us U_dot = 0 = Q_dot - W_dot =>  W_dot_in = Q_dot_out => all work is transferred to heat

# Q_dot = -h*A*(Tb-Tf) = W_dot =>  Tb = -W_dot/(h*A) + Tf

Tb = -W_dot/(h*A) + Tf

pp('Tb','K')

print "What happens if I decrease the heat transfer coefficient? to 100 W/(m^2 K)?  Why don't I want to do this?"

print "What do I have to do to control h?"

print "The surface temperature of the chip is %.2f K.  If the coolant was 30 C, would the temperature of the chip increase, or would Q_dot decrease?" % Tb