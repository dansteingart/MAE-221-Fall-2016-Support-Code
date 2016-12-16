##Author: Dan Steingart
##Date Started: 2016-12-13
##Notes: MS Example 14.1

from pithy import *

"""Evaluate the equilibrium constant, expressed as ln K, for the reaction CO + (1/2) 02 = CO2 at (a) 298 K and 
(b) 2000 K. Compare with the value obtained from Table A-27."""


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

#At 298, dH = 0, s0
T0 = 298 #K
dG0 = h0['CO2']-h0['CO']-.5*h0['O2'] \
 - T0*(s0['CO2']-s0['CO']-.5*s0['O2'])

print "At 298 K"
print "dG0 is %.2f kJ/kmol" % dG0

lnK = -dG0/(T0*Rbar)
print "ln(K) is %.2f" % lnK


#At 2000K, we need to account for the change in enthalpy of the components, so
T = 2000 #K
p = 1e5
hi = {}
hi['CO2'] = pr('Hmolar','T',T0,'P',p,'CO2')
hi['CO']  = pr('Hmolar','T',T0,'P',p,'CO')
hi['O2']  = pr('Hmolar','T',T0,'P',p,'O2')

hf = {}
hf['CO2'] = pr('Hmolar','T',T ,'P',p,'CO2')
hf['CO']  = pr('Hmolar','T',T ,'P',p,'CO')
hf['O2']  = pr('Hmolar','T',T ,'P',p,'O2')


dG0 =  h0['CO2']            - h0['CO']            -.5*h0['O2'] \
 +    (hf['CO2']-hi['CO2']) -(hf['CO']-hi['CO']) -.5*(hf['O2']-hi['O2']) \
 -  (T*s0['CO2']        -   T*s0['CO']          -.5*T*s0['O2'])
 
print 
print "At 2000 K"
print "dG0 is %.2f kJ/kmol" % dG0
lnK = -dG0/(T*Rbar)
print "ln(K) is %.2f" % lnK
