##Author: Dan Steingart
##Date Started: 2016-11-13
##Notes: MS Example 9.6

"""Air enters the compressor of an ideal air-standard Brayton cycle at 100 kPa, 300 K, with a volumetric flow rate of 5 m3/s. The compressor pressure ratio is 10. The turbine inlet temperature is 1400 K. Determine (a) the thermal efficiency of the cycle, (b) the back work ratio, (c) the net power developed, in kW. The turbine/compressor isentropic effiency is 80%"""

from pithy import *

R = 8.3144/28.97  #J/(kg(K))
cv = 0.717 ##J/(kg(K))
cp = cv+R
k = cp/cv

vdot = 5 # m^3/s
eta_s = .8 #isentropic effieciency of the turbine/compressor

#State 1 from givens
p1 = 1e5 #Pa
T1 = 300 #K
#Use pv = RT to find v1
v1 = R*T1/p1

#now find mdot
mdot = vdot/v1 

# State 2
# we are told that
p2 = 10*p1
# assume compressor is isentropic to start
# s2-s1 = 0 = cp*ln(T2/T1) - R*ln(p2/p1)
T2s = T1*exp((R/cp)*log(p2/p1))
v2s = R*T2s/p2

#Now find real state 2
#assume constant cp
#eta = (h2s-h1)/(h2-h1) = (T2s-T1)/(T2s-T1)
T2 = (T2s-T1)/eta_s+T1
v2 = R*T2/p2

#State 3
#We are told
T3 = 1400 #K
p3 = p2
v3 = R*T3/p3

#State 4
p4 = p1 #exhaust to atmosphere
#Istentropic first
T4s = T3*exp((R/cp)*log(p4/p3))

#Now find real state 4
#assume constant cp
T4 = T3-(T3-T4s)*eta_s
v4 = R*T4/p4


#Now find W,Q based on enthalpic analysis
Wcomp = mdot*cp*(T1-T2) 
Wturb = mdot*cp*(T3-T4)
Qcomb = mdot*cp*(T3-T2)

eta = (Wcomp+Wturb)/(Qcomb) 
print "a) eta = %.2f" % eta

bwr = abs(Wcomp/Wturb)
print "b) bwr = %.2f" % bwr

Wcycle = Wcomp+Wturb

print "c) Wcycle = %.3f MW" % (Wcycle/1e6)

