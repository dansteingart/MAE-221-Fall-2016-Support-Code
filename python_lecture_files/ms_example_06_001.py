##Author: Dan Steingart
##Date Started: 2016-10-01
##Notes: MS Example 6.1

from pithy import *

St = {}

#Set States
#Saturated Liquid
T1 = 150+273
x1 = 0
St[1] = stater('T',T1,'Q',x1,'water')

T2 = T1
x2 = 1
St[2] = stater('T',T2,'Q',x2,'water')

P = St[1]['P'] # P1 = P2
T = St[1]['T'] # T1 = T2

print state_table(St)

#Q - W = Delta U
#delta S = delta S_rev + delta S_gen = delta S_rev (all reversible)

W_over_m = P*(St[2]['V']-St[1]['V'])
Q_over_m = T*(St[2]['S']-St[1]['S'])
delta_u_table =  St[2]['U'] - St[1]['U']
delta_u_first_law = Q_over_m - W_over_m

print 'Delta U from table = %.2f kJ/kg' % (delta_u_table/1000)
print 'Q/m - W/m = %.2f kJ/kg' % (delta_u_first_law/1000)

figure(figsize=(10,5))

#Plot Stuff
subplot(1,2,1)
ts_phase_envelope('water')
Ts = []
ss = []
for i in range(1,3):
    Ts.append(St[i]['T'])
    ss.append(St[i]['S'])
    annotate(str(i),xy=(ss[-1],Ts[-1]))
fill_between(ss,200,Ts[0],color='r',alpha=.2)
annotate("Q/m",xy=(4500,300),ha="center")
plot(ss,Ts,'r')
ylim(273,700)

xlabel("Entropy (J/(kg K))")
ylabel("Temperature (K)")

subplot(1,2,2)
pv_phase_envelope('water')
ps = []
vs = []

for i in range(1,3):
    ps.append(St[i]['P'])
    vs.append(St[i]['V'])
    annotate(str(i),xy=(vs[-1],ps[-1]))
plot(vs,ps,'r')
fill_between(vs,1000,ps[0],color='r',alpha=.2)
annotate("W/m",xy=(2e-2,40000),ha="center")
xlabel("Volume (m^3/(kg))")
ylabel("Pressure (Pa)")
loglog()
xlim(1e-4,1e1)
ylim(1e3,1e8)
showme()
clf()