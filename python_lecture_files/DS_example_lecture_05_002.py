##Author: Dan Steingart
##Date Started: 2016-09-20
##Notes: Phase Diagrams Generated from Cool Props for Different Substances

from pithy import *


print "Let's see how U changes with T for water"
Ts = linspace(300,450,500)
p = 1e5 #Pa
sts = stater('T',Ts,'P',p,'water')
U = sts['U']

title("Water")
title("Water @ P = %.1f Pa" %p)
plot(Ts,U,'k')
xlabel("T (K)")
ylabel("u (J/kg)")
showme()
clf()

print 
print "Now limit to just liquid"
title("Water @ P = %.1f Pa" %p)
Ts = linspace(300,370,500)
p = 1e5 #Pa
sts = stater('T',Ts,'P',p,'water')
U = sts['U']

plot(Ts,U,'k')
xlabel("T (K)")
ylabel("u (J/kg)")
showme()
clf()

#Let's try to back out a slope
FIT = polyfit(Ts,U,1)[0]
print "so the curve fit tells us that the slope is %.3f kJ/(kg K)" % (FIT/1000)
print "This familiar?"
print "Now let's look at h"

#Now let's examine H
H = sts['H']

plot(Ts,H,'k')
xlabel("T (K)")
ylabel("h (J/kg)")
showme()
clf()

#Let's try to back out a slope
FITH = polyfit(Ts,H,1)[0]
print "so the curve fit tells us that the slope is %.3f kJ/kg" % (FITH/1000)
print "Why are h and u the same?"

print
print "Now let's see how internal energy changes with pressure"
ps = logspace(3,7,500)

for i in [350,373,400]:
    T = i #Pa
    sts_p = stater('T',T,'P',ps,'water')
    U_p = sts_p['U']
    v_p = sts_p['V']
    
    # print stater('T',300,'P',1e5,'water')
    # print stater('T',300,'P',1e6,'water')eeee
    
    plot(ps,U_p,label='%i K' % T)
semilogx()
legend()
title("Water at T = 373 K")
xlabel("Pressure (Pa)")
ylabel("Internal Energy (J/kg)")
showme()
clf()