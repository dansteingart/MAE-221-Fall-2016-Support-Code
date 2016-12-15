##Author: Dan Steingart
##Date Started: 2016-10-15
##Notes: MS Example 6_015
"""An air compressor operates at steady state with air entering at p1 5 1 bar, T1 5 208C, and exiting at p2 5 5 bar. Determine the work and heat transfer per unit of mass passing through the device, in kJ/kg, if the air undergoes a polytropic process with n 5 1.3. Neglect changes in kinetic and potential energy between the inlet and the exit. Use the ideal gas model for air."""

from pithy import *

#Step 1: write down givens and solve for extra states 
R = 8.314/28.97 #J/gK
cp = 1.015 #J/gK
cv = cp-R
k = cp/cv

#State 1
p1 = 1e5 #Pa
T1 = 20+273 #K

#State 2
p2 = 5e5 #bar

#polytropic exponent
n = 1.3 # pv^n = c

#Solve for T2
#p1v1^n = p2v2^n
#pv = RT
#T2/T1 = (p2/p1)^((n-1)/n)

T2 = (p2/p1)**((n-1)/n)*T1

print 'T2 = %.2f K' % T2

#Now, use the polytronic relationship and our handy subsitution for the ideal gas law

#Wdotcv_over_mdot = ((p2*v2)-(p1*v1))/(1-n) = n*R(T2-T1)/(n-1)

Wdotcv_over_mdot = -n*R*(T2-T1)/(n-1)
print 'Wdotcv_over_mdot = %.2f kJ/kg' % Wdotcv_over_mdot

#Now use the first law to determine heat loss

#delh = Qdotcv_over_mdot - Wdotcv_over_mdot

delh = cp*(T2-T1)

Qdotcv_over_mdot = delh + Wdotcv_over_mdot
print 'Qdotcv_over_mdot = %.2f kJ/kg' % Qdotcv_over_mdot


print
print "What happens if n = 1?"
n=1.00000000000001
T2 = (p2/p1)**((n-1)/n)*T1

print 'T2 = %.2f K' % T2

#Now, use the polytronic relationship and our handy subsitution for the ideal gas law

#Wdotcv_over_mdot = ((p2*v2)-(p1*v1))/(1-n) = n*R(T2-T1)/(n-1)

Wdotcv_over_mdot = -n*R*(T2-T1)/(n-1)
print 'Wdotcv_over_mdot = %.2f kJ/kg' % Wdotcv_over_mdot

#Now use the first law to determine heat loss

#delh = Qdotcv_over_mdot - Wdotcv_over_mdot

delh = cp*(T2-T1)

Qdotcv_over_mdot = delh + Wdotcv_over_mdot
print 'Qdotcv_over_mdot = %.2f kJ/kg' % Qdotcv_over_mdot


