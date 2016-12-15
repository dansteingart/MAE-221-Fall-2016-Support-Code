##Author: Dan Steingart
##Date Started: 2016-12-01
##Notes: MS Problem 10.43

from pithy import *

R = 8.314/28.97 
cv = 0.717
cp = cv+R
k = cp/cv


p1 = 1e5 # Pa
T1 = 300 # K
h1 = cp*T1 #take

p2 = 3.75 *p1# K
T2 = T1*exp((R/cp)*log(p2/p1))
h2 = cp*T2

p3 = p2
T3 = 350 #K
h3 = cp*T3 #K

p4 = p1
T4 = T3*exp((R/cp)*log(p4/p3))
h4 = cp*T4

out = "state,h (kJ/kg) ,p (Pa) ,T (K) \n"

for i in range(1,5):
    out += "%i,%.2f,%.2e,%.2f\n" % (i,eval("h%i"%i),eval("p%i"%i),eval("T%i"%i))

print "States:"
print csv_to_table(out)

print "A) Net Work"
W_c = h1-h2
W_t = h3-h4

W_cycle = W_c + W_t
print "W_cycle = %.2f kj/kg" % W_cycle
print

print "B) Refrigeration Capacity"
Q_in = h1-h4
print "Q_in = %.2f kj/kg" % Q_in
print

print "C) Coefficient of Performance"
beta = abs(Q_in/W_cycle)
print "beta = %.2f " % beta
print

print "D) Ideal COP"
beta_ideal = T1/(T3-T1)
print "beta_ideal = %.2f " % beta_ideal
print
