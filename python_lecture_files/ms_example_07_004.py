##Author: Dan Steingart
##Date Started: 2016-10-20
##Notes: MS Example 7.4

from pithy import *

"""For the gearbox of Examples 2.4 and 6.4(a), develop a full exergy accounting of the power input. Let T0 = 293 K."""

def pp(val,unit): print "%s = %.3f %s" %(val,eval(val),unit)


#What we knew
W_dot_in  = -60 #kW
h = 0.171 #kW/(m^2 K) -> heat transfer coefficient
A = 1 #m^2 -> gearbox area
Tb = 300. #K -> temperature at the outer surface of the gearbox
Tf = 293. #K -> temperature of the ambient air

Q_dot = -h*A*(Tb-Tf)


W_dot_out = Q_dot - W_dot_in

pp('W_dot_in','kW')
pp('Q_dot','kW')
pp('W_dot_out','kW')

E_q_dot = (1-Tf/Tb)*Q_dot
pp('E_q_dot','kW')

print """What's the exergy destroyed?"""

W_dot_net = Q_dot

E_d_dot = E_q_dot-W_dot_net
pp('E_d_dot','kW')

print
print "OR we can look at the Ed as the exergy loss related to irreversible entropy (friction) of the gearbox, from example 6.4"

S_dot_gen = -Q_dot/Tb
To = Tf
E_d_dot = To*S_dot_gen
pp('E_d_dot','kW')
