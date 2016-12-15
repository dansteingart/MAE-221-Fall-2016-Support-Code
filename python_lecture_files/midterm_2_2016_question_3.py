##Author: Dan Steingart
##Date Started: 2016-11-20
##Notes: 


"""Air enters the compressor of a Brayton refrigeration cycle at 1 bar, 266 K, with a volumetric flow rate of 1.42(m^3) / s. If the compressor pressure ratio is 3 and the turbine inlet temperature is 300 K, and the turbine and compressor efficiency fo 80% determine (a) the net power input, (b) the refrigeration capacity, (c) the coefficient of performance."""

from pithy import *


#Find all states, use tables
st = {}

#Flow RAte
AV = 1.4 #m/s

#State 1: After Qin, before Compressor
T1 = 266+273 #K
p1 = 1e5 #Pa
st[1] = stater('P',p1,'T',T1,'air')


#State 2: After Comp. before Qout
p2 = p1*3
s2s  = st[1]['S']
eta_c = .96
st['2s'] = stater('P',p2,'S',s2s,'air')
h2 = st[1]['H'] + (st['2s']['H']-st[1]['H'])/eta_c
st[2] = stater('P',p2,'H',h2,'air')

#State 3: After Qout before Turbine
p3 = p2
T3 = 300+273 #K, given
st[3] = stater('P',p3,'T',T3,'air')

#State 4: After Turbine before Qin
p4 = p1
s4s  = st[3]['S']
eta_t = eta_c
st['4s'] = stater('P',p4,'S',s4s,'air')
h4 = st[3]['H'] - (st[3]['H']-st['4s']['H'])*eta_t
st[4] = stater('P',p4,'H',h4,'air')

print state_table(st)

for i in range(1,5):
    x = st[i]['S']
    y = st[i]['T']
    annotate(str(i),xy=(x,y))
xlim(4e3,5e3)
ylim(100+273,1000+273)
xlabel('Entropy (J/(kg K))')
ylabel('Temperature K')
showme()
clf()

print "(a) the net power input"

mdot = AV/st[1]['V']
W_dot_in = mdot*(st[1]['H']-st[2]['H'])
print 'W_dot_in = %.2f W' % W_dot_in
W_dot_out = mdot*(st[3]['H']-st[4]['H'])
print 'W_dot_out = %.2f W' % W_dot_out
W_dot_net = W_dot_in + W_dot_out 
print 'W_dot_net = %.2f W' % W_dot_net
print ""

print "(b) the cooling capacity"
Q_dot_in = mdot*(st[1]['H'] - st[4]['H'])
print 'Q_dot_in = %.2f W' % Q_dot_in
print

print "(c) the coeefficient of performance"
beta = abs(Q_dot_in/W_dot_net)
print 'beta = %.2f ' % beta
print
