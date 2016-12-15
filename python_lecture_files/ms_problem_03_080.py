##Author: Cody Nunno
##Date Started: 2016-10-01
##Notes: 

from pithy import *

# Step 1: begin with the knowns for state 1
# R22 refridgerant
# Closed system, constant mass
m = 0.5 # kg (mass)
x1 = 1 # (quality)
p1 = 5e5 # Pa (pressure)
state1 = stater('Q',x1,'P',p1,'R22')
v1 = stater('Q',x1,'P',p1,'R22')['V']
u1 = stater('Q',x1,'P',p1,'R22')['U']

# Step 2: Find second state using known info
pv = p1*v1
p2 = 20e5 # Pa (pressure)
v2 = pv/p2 # m^3/kg (s. volume)
state2 = stater('V',v2,'P',p2,'R22')
u2 = stater('V',v2,'P',p2,'R22')['U']

# Print states, just so we know what it looks like
states = {1:state1,2:state2}
print state_table(states)

# Step 3:  Find the work
# For pV = constant, W = pV*ln(V2/V1)
W = p1*v1*m *log(v2/v1)
print "Work for this process is", W/1000, "kJ"

# Step 4: Find the heat transfer
# Q-W = dU
Q = W + m*(u2-u1)
print "Heat transfer for this process is", Q/1000, "kJ"