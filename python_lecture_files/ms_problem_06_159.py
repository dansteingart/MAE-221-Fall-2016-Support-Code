##Author: Wenkai Liang
##Date Started: 2016-10-23
##Notes: 
from pithy import *

St = {}

#Set States
T2 = 60+273 #K
p2 = 9e5
St[2] = stater('T',T2,'P',p2,'R134a')

U1 = St[2]['U'] - 5170*60/7
p1 = 2.4e5 #Pa
St[1] = stater('U',U1,'P',p1,'R134a')

x3 = 0
p3 = p2 #Pa
St[3] = stater('Q',x3,'P',p3,'R134a')

h4 = St[3]['H']
p4 = p1 #Pa
St[4] = stater('P',p4,'H',h4,'R134a')

print state_table(St)

# (a)
q_in = St[1]['H'] - St[4]['H']
q_out = St[2]['H'] - St[3]['H']
w_c = 5.17*1000.0/(7.0/60.0) #kJ/kg
cop = q_out/w_c
print 'cop=',cop

# (b)
#If the throttling valve is replaced by an isentropic turbine, only the value of h4 will change.
s4 = St[3]['S']
p4 = p1 #Pa
St[4] = stater('P',p4,'S',s4,'R134a')

print state_table(St)

q_in = St[1]['H'] - St[4]['H']
q_out = St[2]['H'] - St[3]['H']
w_t = St[3]['H'] - St[4]['H']
print 'Turbine recovery work =', w_t/1000, 'kJ/kg'
cop = q_out/(w_c-w_t)
print 'cop=',cop
