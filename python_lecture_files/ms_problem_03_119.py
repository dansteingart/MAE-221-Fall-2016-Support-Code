##OK TO COPY
##Author: Wenkai Liang
##Date Started: 10-03-2016
##Notes: 

from pithy import *
def pp(val,unit): print "%s = %.3f %s" %(val,eval(val),unit)
def Tp(val,unit): print "%s = %.3f %s" %(val,eval(val)-273,unit)
def pressp(val,unit): print "%s = %.3f %s" %(val,eval(val)/1e6,unit)

# (a) the mass, in kg
T1 = 273 + 27 #K
p1 = 1.0e5 #Pa
Vol = 3*4*5 #m^3
R = 287.058 #J/kg/K
# Using Ideal Gas Law
mass = p1*Vol/(R*T1)
# Using CoolProps
state1_CP = stater('T',T1,'P',p1,'air')
density_CP = state1_CP['D'] #kg/m^3
mass_CP = density_CP*Vol #kg
# Print stuff
print 'initial state:'
print state_table({1:state1_CP})
pp('mass','kg')
pp('mass_CP','kg')

# (b) the final temperature, in C, and (c) the final 
# pressure, in MPa.
# work done by the fan
# W = int(W_dot dt) = W_dot*Delta(t)
W = -1500*30*60 #J
# Using the Ideal Gas Law
# via energy balance: del U = m c_v del T = -W
# Near 300 K and increasing; assume c_v = approx. 0.72
c_v = 0.72*1000 # J/kg
T2 = T1 - W/mass/c_v # K
# Use ideal gas law proportionality to find pressure
p2 = p1*T2/T1 # Pa
# Using CoolProps
# initial internal energy
U1_CP = mass_CP*state1_CP['U'] #J
# final internal energy
U2_CP = U1_CP - W #J
u2_CP = U2_CP/mass_CP #J/kg
state2_CP = stater('U', u2_CP, 'D', density_CP, 'air')
T2_CP = state2_CP['T'] # K
p2_CP = state2_CP['P'] # Pa
# Print stuff
print ''
print 'final state:'
print state_table({2:state2_CP})
print 'Using the Ideal Gas Law:'
Tp('T2','C')
pressp('p2','MPa')
print ''
print 'Using Coolprops:'
Tp('T2_CP','C')
pressp('p2_CP','MPa')