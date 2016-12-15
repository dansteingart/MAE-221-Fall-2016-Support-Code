##Author: Wenkai Liang
##Date Started: 2016-10-17
##Notes: MS P6.111

from pithy import *

#(a)
St = {}
x1 = 0.0
P1 = 60e5 #Pa
St[1] = stater('Q',x1,'P',P1,'water')

T2 = 273+540 #K
P2 = 60e5 #Pa
St[2] = stater('T',T2,'P',P2,'water')

H3 = St[2]['H'] #J/kg
P3 = 40e5 #Pa
St[3] = stater('H',H3,'P',P3,'water')

T4 = 273+240 #K
P4 = 5e5 #Pa
St[4] = stater('T',T4,'P',P4,'water')

H5 = St[4]['H'] #J/kg
P5 = 1e5 #Pa
St[5] = stater('H',H5,'P',P5,'water')

x6 = 0.0
P6 = 1e5 #Pa
St[6] = stater('Q',x6,'P',P6,'water')

figure(figsize=(10,5))
#Plot Stuff
subplot(1,2,1)
ts_phase_envelope('water')
Ts = []
ss = []
for i in range(1,7):
    Ts.append(St[i]['T'])
    ss.append(St[i]['S'])
    annotate(str(i),xy=(ss[-1],Ts[-1]))
plot(ss,Ts,'r')
#xlim(6000,8000)
xlabel("Entropy (J/(kg K))")
ylabel("Temperature (K)")

subplot(1,2,2)
pv_phase_envelope('water')
ps = []
vs = []
for i in range(1,7):
    ps.append(St[i]['P'])
    vs.append(St[i]['V'])
    annotate(str(i),xy=(vs[-1],ps[-1]))
plot(vs,ps,'r')
xlabel("Volume (m^3/(kg))")
ylabel("Pressure (Pa)")
loglog()
#xlim(1e-2,1e1)
showme()
clf()

#(b)
W34 = St[3]['H']-St[4]['H']
print 'work by turbine=',W34/1000,'kJ/kg' 

#(c) and (d)
sig23 = St[3]['S']-St[2]['S']
sig34 = St[4]['S']-St[3]['S']
sig45 = St[5]['S']-St[4]['S']
print 'sigma23',sig23/1000,'kJ/kg/K' 
print 'sigma34',sig34/1000,'kJ/kg/K'
print 'sigma45',sig45/1000,'kJ/kg/K'
print 'Order: Valve 2, Valve 1, Turbine'


#(e)
# remove the valves
W = St[2]['H']-St[5]['H']
print 'work without valves=',W/1000,'kJ/kg' 
print 'Might remove only valve after the turbine, as pre-turbine valves are often used for flow control.'