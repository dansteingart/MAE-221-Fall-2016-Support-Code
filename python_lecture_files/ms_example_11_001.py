##Author: Dan Steingart
##Date Started: 2016-11-05
##Notes: MS Example 11 001

from pithy import *

m_co = 4 #kg
T   = 273-50
D = 0.2 #m
L = 1 #M
V = (pi*D**2/4)*L
v = V/m_co
Rbar = 8134
R = Rbar/(12+16)
vbar = v/(12.+16.)*1000
#Tabular Value
p_table = stater('T',T,'v',v,'CO')['P']
print "p_table = %.2f Bar" % (p_table/1e5)

#Ideal Gas Value
p_IDG = R*T/v
print "p_IDG = %.2f Bar" % (p_IDG/1e5)


#from Table A-24
a = 1.475
b = 0.0395
vc = 3*b #per book
p_VDW = Rbar*T/(vbar-b) + (a/vbar**2)

print "p_VDW = %.2f Bar" % (p_VDW/1e5)

