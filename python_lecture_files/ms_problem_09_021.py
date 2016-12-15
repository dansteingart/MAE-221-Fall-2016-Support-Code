##Author: Cody Nunno
##Date Started: 2016-11-13
##Notes: 

from pithy import *

# Step 1: Write down the knowns
p1 = 95.0e3 #Pa
T1 = 300.0 #K

p2 = 7.2e6
p3 = p2
T3 = 2150.0 #K

# Step 2: Work out the cycle
R = 287.0
k = 1.4

v1 = R*T1/p1

v2 = (p1*v1**k/p2)**(1/k)
T2 = p2*v2/R

v3 = R*T3/p3

v4 = v1
p4 = p3*v3**k/(v4**k)
T4 = p4*v4/R

# Step 3: Determine the ratios
r = v1/v2
r_c = v3/v2
print 'Compression ratio:', r
print 'Cutoff ratio:', r_c

# Step 4: Find efficiency
eta = 1-1/(r**(k-1))*((r_c**k-1)/(k*(r_c-1)))
print 'Efficiency:', eta

# Step 5: Find mep
cv = 718 #J/kgK
cp = 1008 #J/kgK
u1 = cv*T1
u2 = cv*T2
u3 = cv*T3
u4 = cv*T4
w12 = u1-u2
w23 = p2*(v3-v2)
w34 = u3-u4
w41 = 0.0
q23 = cp*(T3-T2)
q41 = u1-u4
w_cycle = w12+w23+w34+w41
mep = w_cycle/(v1-v2)
print 'Mean effective pressure:', mep/1000, 'kPa'