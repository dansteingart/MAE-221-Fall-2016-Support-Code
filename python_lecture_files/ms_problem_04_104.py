##Author: Cody Nunno
##Date Started: 2016-10-15
##Notes: MS P4.104

from pithy import *

# Step 1: State initial conditions we have, find the ones we don't
m_dot_1 = 1.5 # kg/s
p1 = 20.0e5 #Pa
T1 = 360.0+273.0 # K
V1 = 50.0 #m/s

Q2 = 1.0
p2 = 1.0e5 # Pa
V2 = 100.0 #m/s

Q3 = 0.0
p3 = p2
V3 = 100.0 #m/s

W_out = 2.2e6 # W

# Steady state, therefore m_in = m_out
# m_dot_1 = m_dot_2 + m_dot_3; m_dot_2 = m_dot_3
m_dot_2 = 0.5*m_dot_1
m_dot_3 = m_dot_2

# Step 2: develop heat out using steady state 1st law
# 0 = Q - W_out + m1(h1+v1^2/2+gz1) - m2(h2+v2^2/2+gz2) - m3(h3+v3^2/2+gz3)
h1 = stater('P',p1,'T',T1,'water')['H']
h2 = stater('P',p2,'Q',Q2,'water')['H']
h3 = stater('P',p3,'Q',Q3,'water')['H']

z2 = 0.0
z3 = z2
z1 = 10.0 # m
g = 9.81 #m/s^2

Q = W_out + m_dot_2*(h2 + V2*V2/2.0 + g*z2) + m_dot_3*(h3 + V3*V3/2.0 + g*z3) - m_dot_1*(h1 + V1*V1/2.0 + g*z1)

print "Heat transfer out of the system for the process is:",-Q/1000000,"MW"