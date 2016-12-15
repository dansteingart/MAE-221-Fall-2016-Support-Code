##Author: Cody Nunno
##Date Started: 2016-10-15
##Notes: MS P4.108

from pithy import *

# Step 1: Set up state conditions and outputs
#Steam/water
T1 = 600.0+273.0 # K
p1 = 2.0e6 # Pa  > 2016-10-19 DS changed from Bar to Pa, thanks Dorit!

T2 = 400.0+273.0 #K
p2 = 1.0e6 #Pa

p3 = p2

T4 = 240.0+273.0 #K
p4 = 1.0e5 #Pa

#Air
m_dot_5 = 1500.0/60.0 # kg/s
T5 = 1500 #K
p5 = 1.35e5 #Pa

T6 = 1200 #K
p6 = 1.0e5 # Pa

Wt1 = 10.0e6 # W

# Step 2: find what we need to know to determine parts a and b
# Need T3, but need mass flow rate for the steam cycle to know how much heat is transferred
# Can find this quantity using the 1st turbine
# Wt1 = m1(h1-h2)
h1 = stater('P',p1,'T',T1,'water')['H']
h2 = stater('P',p2,'T',T2,'water')['H']

m_dot_1 = Wt1/(h1-h2)

print m_dot_1, 'kg/s'

# Require both the mass flow rate and T3 for the second turbine, so all set to solve a

# Step 3: solve for T3
# For a heat exchanger: m1(h1-h2) = m3(h3-h4)
# So:
h5 = stater('P',p5,'T',T5,'air')['H']
h6 = stater('P',p6,'T',T6,'air')['H']
h3 = m_dot_5*(h5-h6)/m_dot_1 + h2

T3 = stater('P',p3,'H',h3,'water')['T']

print 'T at point 3 is', T3, 'K'

# Step 4: Find work at turbine 2
h4 = stater('P',p4,'T',T4,'water')['H']
Wt2 = m_dot_1*(h3-h4)

print 'Work at turbine 2 is', Wt2/1000, 'kW'
