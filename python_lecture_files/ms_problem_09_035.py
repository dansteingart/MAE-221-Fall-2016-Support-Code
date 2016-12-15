##Author: Wenkai Liang
##Date Started: 11-12-2016
##Notes: 
from pithy import *

R = 8.31415 # J/(mol K)
M_air = 28.97 # g/mol
R_air = R/M_air # J/(g K)
k = 1.4 #heat ratio
cv = R_air/(k-1) #J/(mol K)
cp = cv + R_air #J/(mol K)

r = 9.  #V1/V2

#Starting Condition
T1 = 300 #K
P1 = 1e5 #Pa
v1 = R_air*T1/P1 * 1000 

T2 = T1*exp(-(R_air/cv)*log(1/r))
P2 = P1*(T2/T1 *(r))
v2 = R_air*T2/P2 * 1000 

print 'T2=',T2,'K'
print 'P2=',P2/1000,'kPa'

Q23=1400*2/3
Q34=1400/3

#(a)
T3=Q23/cv+T2
v3=v2
T4=Q34/cp+T3
v4=v3*T4/T3
print 'T3=',T3,'K'
print 'T4=',T4,'K'

#(b)
v5=v1
T5=(v4/v5)**(k-1)*T4
print 'T5=',T5,'K'
Q51=cv*(T5-T1)
W=Q23+Q34-Q51
print 'W=',W,'kJ/kg'

#(c)
eff=W/(Q23+Q34)
print 'eff=',eff

#(d)
mep=W/(v1-v2)
print 'mep=',mep,'kPa'


