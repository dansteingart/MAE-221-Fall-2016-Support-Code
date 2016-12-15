##Author: Wenkai Liang
##Date Started: 2016-10-17
##Notes: MS P6.85

from pithy import *

#energy balance
p1 = 3.0e5 #Pa
T1 = 273+20 #K
state1 = stater('P',p1,'T',T1,'air')
p2 = 2.7e5 #Pa
T2 = 273+60 #K
state2 = stater('P',p2,'T',T2,'air')
p3 = 2.7e5 #Pa
T3 = 273+0 #K
state3 = stater('P',p3,'T',T3,'air')

states = {1:state1,2:state2,3:state3}
print state_table(states)

m1 = 1 #kg/s
m2 = (state1['H']-state3['H'])/(state2['H']-state3['H']) #kg/s
m3 = 1-m2 #kg/s
print 'm2=',m2, 'kg/s'
print 'm3=',m3, 'kg/s'

#entropy balance
sigma = state2['S']*m2+state3['S']*m3-state1['S']*m1
print 'entropy production=',sigma, 'J/K/s'