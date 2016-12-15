##Author: Dan Steingart
##Date Started: 2016-10-20
##Notes: Midterm Problem 2

from pithy import *

"""A cycle in a piston cylinder involving air modeled as an ideal gas proceeds as follows:

State 1 - 2: Adiabatic compression from 1 bar at 295 K to 10 bar
State 2 - 3: Constant pressure heating from v2 to v3 = 3v2
State 3 - 4: Adiabatic expansion to v1
State 4 - 1: Constant volume cooling to T1

a) Sketch the process on a P-V and T-S diagram

b) Make a table listing P,V and T for all four states assuming that cv=0.717 kJ/(kg K) and R = 0.287 kJ/(kg K)

c) Is this a power cycle or heat pump? Calculate the thermal efficiency or the coefficient performance, accordingly
"""

R = 0.287
cv = 0.717
cp = cv+R
k = cp/cv

vartab = ""

#NB: you didn't need to calculate entropy, I am just doing for sake of plot.

#State 1
T1 = 295
p1 = 1e5
v1 = R*T1/p1
s1 = 0 #make reference point

#State 2
#Use adiabatic process that pv^k = constant to get T2
p2 = 10e5
T2 = T1*(p2/p1)**((k-1)/k) 
v2 = R*T2/p2
s2 = s1 #Adiabatic/closed = isentropic
#You could have also used
# 0 = cp*log(T3/T2)-R*log(p3/p2) and solved for T

#State 3
v3 = 3*v2
p3 = p2
T3 = p3*v3/R
s3 = s2 + cv*log(T3/T2)+R*log(v3/v2) 

v4 = v1
T4 = T3*(v3/v4)**(k-1)
p4 = R*T4/v4
s4 = s3

#bundle
Ts = [T1,T2,T3,T4,T1]
ss = [s1,s2,s3,s4,s1]
ps = [p1,p2,p3,p4,p1]
vs = [v1,v2,v3,v4,v1]

#make table
print "State\tT (K)\tP (Pa)\t\tv (m^3/kg)"
for i in range(4): print "%i\t\t%.2f\t%.2e\t\t%.2e" % (i+1,Ts[i],ps[i],vs[i])

figure(figsize=(10,4))

#plots
print
print "If you drew it like this, or with the proper curves, you'd get full credit either way"
subplot(1,2,1)
for i in range(4):annotate(str(i+1),xy=(ss[i],Ts[i]))
plot(ss,Ts,'k--')
ylabel("Temperature")
xlabel("Specific Entropy")
xticks([])
yticks([])
xlim(-.1,max(ss)*1.1)

subplot(1,2,2)
for i in range(4):annotate(str(i+1),xy=(vs[i],ps[i]))
plot(vs,ps,'k--')
yticks([])
xticks([])
ylabel("Pressure")
xlabel("Specific Volume")
xlim(0,1e-3)
ylim(.5e5,1.2e6)
showme()
clf()

#Calculate eta
#Delta U = Q - W
Qh_by_m = cv*(T3-T2) + p3*(v3-v2)
Qc_by_m = cv*(T4-T1)

print Qc_by_m
print Qh_by_m
eta = 1-(Qc_by_m)/(Qh_by_m)

print "This is a heat engine and the thermal efficeincy is %.2f" % eta

