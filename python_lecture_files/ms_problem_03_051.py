##Author: Cody Nunno
##Date Started: 2016-09-25
##Notes: MS Problem 3.51

from pithy import *

def pp(val,unit): print "%s = %.2f %s" %(val,eval(val),unit)

# Step one: read in the given conditions and find the first state
x1 = .5052 #(quality)
T1 = 273-20 #K (temperature)

state1 = stater('Q',x1,'T',T1,'R22')
st = {}
st[1] = state1


# Step two: seek the second state.  
# We know the pressure, but we require a second state.  Where do we get the next set of information?  Note the rigid and closed container, meaning volume and mass are the same between processes, therefore density is the same between processes.  So:

rho2 = state1['D'] # kg/m^3
p2 = 6e5 # Pa; 1e5 Pa = 1 bar
state2 = stater('D',rho2,'P',p2,'R22')
st[2] = state2
print state_table(st)

# Step three: determine heat energy transfer into the system (q)
# Need to use the first law of thermodynamics to determine changes in energy. No kinetic or potential energy changes for this system, and there is no change in volume in this case, therefore there is no work done on or by the system.  The only changes which occur are in internal energy and heat energy.  So: (Delta)U = Q or (Delta)u = q
Du = state2['U'] - state1['U']
q = Du/1000
pp('q','kJ/kg')
