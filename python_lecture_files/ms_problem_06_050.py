##Author: Wenkai Liang
##Date Started: 10-23-2016 
##Notes: Problem 6.50

from pithy import *

st = {}

#(a)
p1 = 1e5
T1 = 273+27
st[1] = stater('P',p1,'T',T1,'air')

p2 = 5e5
T2 = 273+207
st[2] = stater('P',p2,'T',T2,'air')

print state_table(st)
print "Is dS > 0?: dS =", st[2]['S']-st[1]['S'] , 'J/(gK), OK'
print 'use first law: W=U1-U2=', (st[1]['U']-st[2]['U'])/1000,'kJ/kg'


#(b)
p3 = 3*101325
T3 = 299.817
st[3] = stater('P',p3,'T',T3,'air')

p4 = 10*101325
T4 = 388.706
st[4] = stater('P',p4,'T',T4,'air')

print state_table(st)
print "Is dS > 0?: dS =", st[4]['S']-st[3]['S'],'J/kgK, not OK to do work'
print 'state1->state2: entropy has to increase if Q=0, therefore Q is out of the system'