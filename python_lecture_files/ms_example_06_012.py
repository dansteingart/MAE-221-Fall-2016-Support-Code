##Author: Dan Steingart
##Date Started: 2016-10-15
##Notes: MS Example 6.12

"""A turbine operating at steady state receives air at a pressure of p1 = 3.0 bar and a temperature of T1  = 390 K. Air exits the turbine at a pressure of p2 = 1.0 bar. The work developed is measured as 74 kJ per kg of air flowing through the turbine. The turbine operates adiabatically, and changes in kinetic and potential energy between inlet and exit can be neglected. Using the ideal gas model for air, determine the isentropic turbine efficiency."""

from pithy import *

St = {}


#Ideal Gas Model for Air
cv = 0.717 # kj/(kg K)
R = 8.314/28.97 # kj/(kg K)
cp = cv+R
k = cp/cv

#Step 1: Set States
#known!
T1 = 390 #K
p1 = 3e5 #Pa

p2 = 1e5 #Pa
Wcvbym = 74 #"kj/kg"

#use Wcvbym cp to solve for T2
# Wcvbym = h1-h2  = cp(T1-T2)

T2 = T1-(Wcvbym/cp)
print "T2 = %.2f K" % T2

print"""
In the adiabatic case:

s2 = s1 => cp*ln(T2/T1) = R*ln(p2/p1)
(in python log = ln)
"""

T2s = T1*exp((R*log(p2/p1)/cp))

print "T2s = %.2f K" % T2s


"""There's an 'easier' way"""

T2s = T1*(p2/p1)**((k-1)/k)
print "T2s = %.2f K" % T2s

Wcv_sbym = cp*(T1-T2s)

print "Wcv_sbym = %.2f kJ/kg" % Wcv_sbym

eta_s_turbine = Wcvbym/Wcv_sbym
print "eta_s_turbine = %.2f" % eta_s_turbine
print
print "What is the rate of entropy production in the _real_ system?"

del_s = cp*log(T2/T1) - R*log(p2/p1)

print "del_s = %.3f kJ/(kg K)" % del_s
