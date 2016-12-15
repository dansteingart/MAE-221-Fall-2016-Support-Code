##Author: Dan Steingart
##Date Started: 2010-10-21
##Notes: MS Example 7.1

from pithy import *

"""A cylinder of an internal combustion engine contains 2450 cm3 of gaseous combustion products at a pressure of 7 bar and a temperature of 867C just before the exhaust valve opens. Determine the specific exergy of the gas, in kJ/kg. Ignore the effects of motion and gravity, and model the combustion products as air behaving as an ideal gas. Take T0 = 300 K (278C) and p0 = 1.013 bar."""

p1 = 7e5 #Pa
V1 = 0.00245 #m^3
T1 = 867 + 273 #K

T0 = 300 #K
p0 = 1.013e5 #Pa


St = {}

#Cool props says:
St[1] = stater("T",T1,'P',p1,'air')
v1 = St[1]['V']
u1 = St[1]['U']
s1 = St[1]['S']

St[0] = stater("T",T0,'P',p0,'air')
v0 = St[0]['V']
u0 = St[0]['U']
s0 = St[0]['S']

ex = (u1-u0)+p0*(v1-v0)-T0*(s1-s0)

# print (u1-u0)/1000
# print p0*(v1-v0)/1000
# print T0*(s1-s0)/1000

print "The exergy leaving the system is %.2f kJ/kg" % (ex/1000)