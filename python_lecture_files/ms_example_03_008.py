##Author: Dan Steingart
##Date Started: 2016-09-19
##Notes: MS Example 3.8

from pithy import *

#NB: the 'stater' function has one odd thing to it: all inputs, even if mass normalized, are presented by CAPITAL letters

#e.g. pressure = P, quality = Q, Temperature = T, specific volume =V, etc.

#make a pretty print helper function
#We give it the variable and the unit and it makes a nicely printed relationship.  Purely for display.
def pp(val,unit): print "%s = %.1f %s" %(val,eval(val),unit)

# Step 1 Givens

# Process 1-2: Constant specific volume 
# Process 2-3: Constant temperature expansion 
# Process 3-1: Constant pressure compression

T1 = 300  #K
p1 = 1e5  #Pa
p2 = 2e5  #Pa
m  = 0.45 #kg
R  = 28.97 #(kJ/kg K)

# Step 2 Find
# a) p and V at each state

# Use Ideal Gas law to finish state 1
# pV = mRT
V1 = m*R*T1/p1

# Now constant volume step
V2 = V1
T2 = p2*V2/(m*R)

# Now a constant temperature step
T3 = T2
p3 = p1
V3 = m*R*T3/p3

# Now plot
ps = [p1,p2,p3,p1]
Vs = [V1,V2,V3,V1]

plot(Vs,ps)
# ylim(5e4,2.5e5)
# xlim(3e-4,8e-4)
xlabel("Volume (m^3)")
ylabel("Pressure (Pa)")
showme()
clf()

# This isn't right....

# p3V3/T3 = p2V2/T2
V23 = linspace(V2,V3,100)
p23 = p2*V2/V23
ps = [p1,p2]+list(p23)+[p3,p1]
Vs = [V1,V2]+list(V23)+[V3,V1]
plot(Vs,ps)
xlabel("Volume (m^3)")
ylabel("Pressure (Pa)")
# ylim(5e4,2.5e5)
# xlim(3e-4,8e-4)
showme()
clf()

#We already know T2, so
pp("T2","K")

v3 = V3/m
pp("v3","m^3/kg")
