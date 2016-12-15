##Author: Cody Nunno
##Date Started: 2016-10-01
##Notes: 

from pithy import *
def pp(val,unit): print "%s = %.3f %s" %(val,eval(val),unit)

# Step 1: Find the initial and final pressures in English units
# F =kx, and F_p = p*A
k = 200 #lbf/in
k_SI = k*175.127 #N/m
d1 = 20 #in
x1 = d1*0.0254 #m
d2 = 16 #in
x2 = d2*0.0254 #m
F1 = k*d1 #lbf
F_p1 = F1 #lbf
A = 20 #in^2
p1_eng = F_p1/A #lbf/in^2
print "Part a"
pp('p1_eng','lbf/in^2')
F2 = k*d2 #lbf
F_p2 = F2 #lbf
p2_eng = F_p2/A #lbf/in^2
pp('p2_eng','lbf/in^2')

# Step 2: Find the full states, using SI units
print " "
print "We're going to find the states"
# State 1
V1_eng = A*d1 # in^3 (volume)
p1 = p1_eng*6894.76 # Pa (pressure)(with conversion from lbf/in^2)
T1 = (1000+459.67)*5/9 # K (temperature)(with conversion for F -> K)
state1 = stater('T',T1,'P',p1,'water')
v1 = stater('T',T1,'P',p1,'water')['V'] # m^3/kg (s. volume)
u1 = stater('T',T1,'P',p1,'water')['U']

# State 2
V2_eng = A*d2 # in^3 (volume)
p2 = p2_eng*6894.76 # Pa (pressure)(with conversion from lbf/in^2)
v2 = v1*V2_eng/V1_eng # m^3/kg (s. volume)
state2 = stater('V',v2,'P',p2,'water')
u2 = stater('V',v2,'P',p2,'water')['U']

# Print states, just so we know what they look like
states = {1:state1,2:state2}
print state_table(states)

# Step 3: Find the system mass, in English units
print " "
print "Part b"
V1 = V1_eng*1.63871e-5 # m^3 (volume)
V2 = V2_eng*1.63871e-5 # m^3 (volume)

m = V1/v1 # kg (mass)
m_eng = m*2.20462 # lbm (mass, in English units)
pp('m_eng','lbm')

#Step 4: Find work and heat transfer
print " "
print "Part c"
# We can represent work as a force over distance as well.  So W = integral(Fdx) = integral(kxdx) = 1/2 kx^2 from 2 to 1
W = k_SI*(x2*x2-x1*x1)/2 #J
W_eng = W*0.000947817 # BTU
print "Work for this process is",W_eng,"BTU"

print " "
print "Part d"
#Q - W = dU
Q = W + m*(u2-u1)
Q_eng = Q*0.000947817 # BTU
print "Heat transfer for this process is",Q_eng,"BTU"
