##Author: Dan Steingart
##Date Started: 2016-12-01
##Notes: MS Problem 10.55

from pithy import *

R = 8.314/28.97 
cv = 0.717
cp = cv+R
k = cp/cv

#State 1: LEave Engine Enter Heat Exchnager
p1 = 2.5e5 # Pa
T1 = 400 # K
h1 = cp*T1 #take 0 K as reference

#State 2: Leave Heat Exchanger Enter Turbine 
p2 = p1
T2 = 325 #K
h2 = cp*T2

mdot = 2 #kg/s

#State 3: LEave Turbine Enter Cabin
eta_t = .8
p3  = 1e5 #Pa
T3s = T2*exp((R/cp)*log(p3/p2))
h3s = cp*T3s
h3  = h2-(h2-h3s)*eta_t
T3 = h3/cp

out = "state,h (kJ/kg) ,p (Pa) ,T (K) \n"

for i in range(1,4):
    out += "%i,%.2f,%.2e,%.2f\n" % (i,eval("h%i"%i),eval("p%i"%i),eval("T%i"%i))

print "States:"
print csv_to_table(out)

print "A) Find Turbine Power"
W_dot_t = mdot*(h2-h3)
print "W_dot_t = %.2f kW" % W_dot_t
print

print "B) Find Heat Removed from Input Stream"
Q_cv_he = mdot*(h2-h1)
print "Q_cv_he = %.2f kW" % Q_cv_he