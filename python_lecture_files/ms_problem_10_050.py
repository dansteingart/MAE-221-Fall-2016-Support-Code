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

p4 = p3
T4 = 320 #K
h4 = cp*T4

p5 = p1
T5 = T4*exp((R/cp)*log(p5/p4))
h5 = cp*T5

p6 = p5
h6 = h1-h3+h4
T6 = h6/cp
out = "state,h (kJ/kg) ,p (Pa) ,T (K) \n"

for i in range(1,7):
    out += "%i,%.2f,%.2e,%.2f\n" % (i,eval("h%i"%i),eval("p%i"%i),eval("T%i"%i))

print "States:"
print csv_to_table(out)

print "A) Coldest Temp"
print "T5 = %.2f K" % T5
print 

print "B) Net Work"
W_c = h1-h2
W_t = h4-h5

W_cycle = W_c + W_t
print "W_cycle = %.2f kj/kg" % W_cycle
print

print "C) Refrigeration Capacity"
Q_in = h4-h6
print "Q_in = %.2f kj/kg" % Q_in
print

print "D) Coefficient of Performance"
beta = abs(Q_in/W_cycle)
print "beta = %.2f " % beta
print
