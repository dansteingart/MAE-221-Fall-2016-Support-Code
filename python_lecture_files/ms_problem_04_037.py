##Author: Cody Nunno
##Date Started: 2016-10-23
##Notes: MS Problem 4.37

from pithy import *

# Step 1:  Write what is known about the states
p1 = 18.0e3 #Pa
T1 = 216.0 #K
v1 = 265.0 #m/s

T2 = 250.0 #K
q12 = 0.0 # J/kg

# Step 2: Use knowledge about diffusers to solve for velocity
cp = 1003.0 # J/kgK
h1 = cp*T1 #J/kg
h2 = cp*T2 #J/kg

v2 = (2.0*(h1-h2 + v1**2.0/2.0))**(1.0/2.0)

print 'Velocity is %.2f m/s' % v2