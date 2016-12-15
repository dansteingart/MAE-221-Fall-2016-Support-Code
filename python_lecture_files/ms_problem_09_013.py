##Author: Cody Nunno
##Date Started: 2016-11-13
##Notes: 

from pithy import *

# Step 1: State what is known
p1 = 1.0e5 #Pa
T1 = 310.0 #K

r = 10.0

T3 = 2200.0 #K

n = 1.3
R = 287.0 #J/kgK

# Step 2: Work out the cycle
v1 = R*T1/p1

v2 = v1/r
p2 = p1*v1**n/(v2**n)
T2 = p2*v2/R

v3 = v2
p3 = R*T3/v3

v4 = v1
p4 = p3*v3**n/(v4**n)
T4 = p4*v4/R

# Step 3: Find Qs and Ws
cp = 1005 #J/kgK
cv = 718 #J/kgK
# Process 1-2
u1 = cv*T1
u2 = cv*T2
w12 = (p2*v2-p1*v1)/(1-n)
q12 = u2-u1 + w12
# Process 2-3
u3 = cv*T3
w23 = 0
q23 = u3-u2
# Process 3-4
u4 = cv*T4
w34 = (p4*v4-p3*v3)/(1-n)
q34 = u4-u3 + w34
# Process 4-1
w41 = 0
q41 = u1-u4

print 'q12 is', q12/1000, 'kJ/kg'
print 'w12 is', w12/1000, 'kJ/kg'
print 'q23 is', q23/1000, 'kJ/kg'
print 'w23 is', w23/1000, 'kJ/kg'
print 'q34 is', q34/1000, 'kJ/kg'
print 'w34 is', w34/1000, 'kJ/kg'
print 'q41 is', q41/1000, 'kJ/kg'
print 'w41 is', w41/1000, 'kJ/kg'
print 'wnet is', (w12+w23+w34+w41)/1000, 'kJ/kg'
print 'qin is', (q23+q34)/1000, 'kJ/kg'

# Step 4: Find efficiency and mep
eta = 1-(-q12-q41)/(q34+q23)
print 'Efficiency is:', eta
w_cycle = w34+w12
mep = w_cycle/(v1*(1-(1/r)))
print 'Mean effective pressure is:', mep/1000, 'kPa'