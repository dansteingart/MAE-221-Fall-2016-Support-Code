##Author: Dan Steingart
##Date Started: 2016-09-19
##Notes: MS Example 3.12

from pithy import *

#NB: the 'stater' function has one odd thing to it: all inputs, even if mass normalized, are presented by CAPITAL letters

#e.g. pressure = P, quality = Q, Temperature = T, specific volume =V, etc.

#make a pretty print helper function
#We give it the variable and the unit and it makes a nicely printed relationship.  Purely for display.
def pp(val,unit): print "%s = %.1f %s" %(val,eval(val),unit)

# Step 1 Givens
cp = 1.014
cv = 0.717
k = cp/cv
R = cv*(k-1)

n = k

T1 = 295 #K
p1 = 1e5 #Pa
p2 = 5e5 #Pa

# Step 2 Determine the work and heat transfer per unit mass

# Qbym - Wbym = Delta_u = cp*(T2-T1)

# We can get T2 by => (T2/T1) = (p2/p1)^(n-1)/n

T2 = T1*(p2/p1)**((n-1)/n)
pp("T2","K")

Delta_u = cv*(T2-T1)
pp("Delta_u","kJ/(kg K)")

Wbym = R*(T2-T1)/(1-n)
pp("Wbym","kJ/(kg K)")

Qbym = Delta_u + Wbym
pp("Qbym","kJ/(kg K)")

#Let's solve analtically

print """
Let's solve analtically
Delta_u = cv*(T2-T1) = R*(T2-T1)/(k-1)
Wbym = R*(T2-T1)/(1-k)
Qbym - Wbym = Delta_u 
Qbym = R*(T2-T1)/(1-k) + R*(T2-T1)/(k-1) = 0
"""