##Author: Dan Steingart
##Date Started: 2016-12-13
##Notes: MS Example 14.2

from pithy import *


Rbar = 8.314 #kJ/(kmol K)

h0 = {}
#From A-25, kJ/kmol
h0['CO2'] = -393520 
h0['CO']  = -110530 
h0['O2']  =  0

s0 = {}
#From A-25, kJ/kmol
s0['CO2'] = 213.69
s0['CO']  = 197.54 
s0['O2']  = 205.03


#At 2500K, we need to account for the change in enthalpy of the components, so
T0 = 298 #K
T  = 2500 #K
p1 = 1e5 #bar
p2 = 1e6 #bar
hi = {}
hi['CO2'] = pr('Hmolar','T',T0,'P',p1,'CO2')
hi['CO']  = pr('Hmolar','T',T0,'P',p1,'CO')
hi['O2']  = pr('Hmolar','T',T0,'P',p1,'O2')

hf = {}
hf['CO2'] = pr('Hmolar','T',T ,'P',p1,'CO2')
hf['CO']  = pr('Hmolar','T',T ,'P',p1,'CO')
hf['O2']  = pr('Hmolar','T',T ,'P',p1,'O2')


dG0 =  h0['CO2']            - h0['CO']            -.5*h0['O2'] \
 +    (hf['CO2']-hi['CO2']) -(hf['CO']-hi['CO']) -.5*(hf['O2']-hi['O2']) \
 -  (T*s0['CO2']        -   T*s0['CO']          -.5*T*s0['O2'])
 
print 
print "At %i K" % T
print "dG0 is %.2f kJ/kmol" % dG0
lnK = -dG0/(T*Rbar)
print "ln(K) is %.2f" % lnK
K = exp(-lnK)
print "K is %.2f" % K
print
for p in [p1,p2]:
    print "Test at P = %.2e Pa" % p
    z_test = linspace(0,1,1000)
    Best   = 1000
    z_best = 0
    for z in z_test:
        z1 = z/(1-z)
        z2 =(z/(2+z))**(.5)
        z3 = (p/p1)**(.5)
        test = z1*z2*z3
        if abs(K-test) < Best:
            Best = abs(K-test)
            z_best = z
    
    z = z_best
    print "z = %.3f" % z
    y ={}
    y['CO']  =    2*z/(2+z)
    y['O2']  =      z/(2+z)
    y['CO2'] = 2*(1-z)/(2+z)
    for k in y.keys(): print "Fraction %s = %.3f" % (k,y[k])
    print
    
