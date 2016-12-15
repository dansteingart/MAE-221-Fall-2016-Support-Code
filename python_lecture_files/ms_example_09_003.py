##Author: Dan Steingart
##Date Started: 2016-11-05
##Notes: MS Example 9.3

from pithy import *

r = 18.   #compression ratio
rp = 1.5 #pressure ratio
rc = 1.2 #cutoff ratio

R = 8.31445 #J/(K mol)
M = 28.97   #g/mol
R_air = R/M #J/(g K)
k = 1.4
cv = R_air/(k-1)
cp = cv+R_air

#Use cold air standard analysis
T1 = 300 #K
P1 = 1e5 #Pa
v1 = R_air*T1/P1
s1 = 0

#Step 1-2 Isentropic Compression 
#T2 = T1*exp(-(R_air/cv)*log(1/r)) = T1*(r)**(k-1)
T2 = T1*(r)**(k-1)
P2 = P1*(T2/T1)*(r)
v2 = R_air*T2/P2
s2 = s1

#Step 2-3 constant volume heating 
P3 = rp*P2
T3 = rp*T2
v3 = R_air*T3/P3


#Step 3-4 constant pressure heating 
T4 = rc*T3
v4 = rc*v3
P4 = R_air*T4/v4


#Step 4-5 Isentropic Expansion to v5 = v1 
T5 = T4*(rc/r)**(k-1)
P5 = P1*T5/T1
v5 = R_air*T5/P5

vs = [v1,v2,v3,v4,v5,v1]
Ps = [P1,P2,P3,P4,P5,P1]

for i in range(5):
    annotate(str(i+1),xy=(vs[i],Ps[i]))

plot(vs,Ps,'k')
xlabel("Volume (m^3/kg)")
ylabel("Pressure (Pa)")
loglog()
showme()
clf()

print "T (K) ,P (Pa)"
print "%.2f,%.2e" % (T1,P1)
print "%.2f,%.2e" % (T2,P2)
print "%.2f,%.2e" % (T3,P3)
print "%.2f,%.2e" % (T4,P4)
print "%.2f,%.2e" % (T5,P5)
print ""
QH  = cv*(T3-T2)+cp*(T4-T3)
QC = cv*(T5-T1)
Wcycle = QH-QC
eta = 1- QC/QH
print "eta = %.2f" % eta
print "QH = %.2f kJ/kg" % QH
print "Wcycle = %.2f kJ/kg" % Wcycle
