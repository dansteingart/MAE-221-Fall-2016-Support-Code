##Author: Dan Steingart
##Date Started: 2016-09-01
##Notes: Solution to MS Example 2-4

from pithy import *

#make a pretty print helper function
#We give it the variable and the unit and it makes a nicely printed relationship.  Purely for display.
def pp(val,unit): print "%s = %.3f %s" %(val,eval(val),unit)

#Step 1: Clearly state given aspects of the problem

#A gearbox has work in and out, and there is some power loss due to something in the workings of the gear box.  We don't care what that something is right now, we just want to quantify how much power we are losing.  We are told

h = 0.171 #kW/(m^2 K) -> heat transfer coefficient
A = 1 #m^2 -> gearbox area
Tb = 300 #K -> temperature at the outer surface of the gearbox
Tf = 293 #K -> temperature of the ambient air
W_dot_in = -60 # kW


#Our first law balance, in steady state, tells us U_dot = 0 = Q_dot - W_dot =>  W_dot_in + W_dot_out = Q_dot

#We are given enough information to detrmine Q_dot, so we rearrange W_dot_out = Q_dot - W_dot_in

pp('W_dot_in','kW')
Q_dot = -h*A*(Tb-Tf)
pp('Q_dot','kW')
W_dot_out = Q_dot - W_dot_in
pp('W_dot_out','kW')

print
print "So, we lose %.1f%% of the work in through heat generation" % (100*Q_dot/W_dot_in)

print "If the temperature of the ambient was 300K instead of 293K, would this box run at 100% efficiency?"

print ""

print "Does radiation move any heat?  If we assume the emissitivity is 0.8..."

eps = 0.8
sigma = 5.67e-8 # (10 8W/m^2 * K^4) 

Q_dot_radiation = -eps*sigma*A*(Tb**4-Tf**4)/1000
pp('Q_dot_radiation','kW')

print "Yes, there is some radiative heat transfer and it is %.3f%% of the total heat transferred" % (100*Q_dot_radiation/(Q_dot_radiation+Q_dot))

print "" 

print "How hot would the gearbox have to get such that the radiation accounted for half the heat transfer?  Can I ever get to that temperature with this work input?"

