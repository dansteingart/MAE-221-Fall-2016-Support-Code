##Author: Dan Steingart
##Date Started: 2016-12-01
##Notes: MS Problem 9.60

from pithy import *

R = 8.314/28.97 
cv = 0.717
cp = cv+R
k = cp/cv

#State 1: Before Compressor
T1 = 300 #K
p1 = 1e5 #Pa
h1 = cp*(T1-0) # Abs 0 as reference
s1 = 0 #as reference

#State 2: After Comp before Reheat
p2 = 12*p1
T2s = T1*exp((R/cp)*log(p2/p1))
h2s = cp*(T2s-T1)+h1
eta_c = .8
h2  = h1+(h2s-h1)/eta_c
T2 = (h2-h1)/cp+T1

#State 4: After combustor, before turbine
p4 = p2 #PA
T4 = 1450 #K
h4 = cp*(T4)

#State 5: After turbine, before reheat
eta_t = .8
p5 = p1
T5s = T4*exp((R/cp)*log(p5/p4))
h5s = h4-cp*(T4-T5s)
eta_c = .8
h5  = h4-(h4-h5s)*eta_t
T5 = T4-(h4-h5)/cp
p6 = p1

#Solve for state 3  and 6(x,y in book)
# 1 = (h3-h2)/(h5-h2)
p3 = p2
h3 = h5
h6 = h2
T6 = T2
T3 = T5

out = "state,h (kJ/kg) ,p (Pa) ,T (K) \n"

for i in range(1,7):
    out += "%i,%.2f,%.2e,%.2f\n" % (i,eval("h%i"%i),eval("p%i"%i),eval("T%i"%i))

print "Part A) States:"
print csv_to_table(out)


print "Part B) Flow Rate Determination"
Wdotcycle  = 10000 #kW
Wdottbym = h4-h5 #Turbine Work
Wdotcbym = h1-h2 #Turbine Work
mdot = Wdotcycle/(Wdottbym+Wdotcbym)
print "mdot = %.2f kg/s" % mdot
print 

print "Part C) Determine Qin"
Qdotin = mdot*(h4-h3)
print "Qdotin = %.2f kW" % Qdotin
print 

print "Part D) Thermal Efficiency"
eta = Wdotcycle/Qdotin
print "eta = %.2f" % eta
print 

