##Author: Cody Nunno
##Date Started: 2016-10-04
##Notes: 

from pithy import *

# Initial conditions
T1 = 298 # K
p1 = 101.3e3 #Pa

# Can use ideal gas law... or just Cool Props
R = 287.058 #J/kg/K
v1_igl = R*T1/p1
print 'v1 = ',v1_igl, 'm^3/kg'

v1_cp = stater('T',T1,'P',p1,'air')['V']
state1 = stater('T',T1,'P',p1,'air')
st = {}
st[1] = state1
print state_table(st)
print 'v1 = ',v1_cp, 'm^3/kg'

# Process 1: Isochoric heat addition to 1500 K
v2_igl = v1_igl
T2 = 1500 # K

p2_igl = R*T2/v2_igl
print 'p2 = ',p2_igl/1000, 'kPa'

p2_cp = stater('T',T2,'V',v1_cp,'air')['P']
print 'p2 = ',p2_cp/1000, 'kPa'

# Process 2: Isentropic, adiabatic expansion to P = 1 atm
# q=0, s2=s3
s3 = stater('T',T2,'V',v1_cp,'air')['S']
p3 = p1
v3 = stater('S',s3,'P',p3,'air')['V']
print 'v3 = ',v3, 'm^3/kg'
T3 = stater('S',s3,'P',p3,'air')['T']
print 'T3 = ',T3, 'K'

vs = [v1_cp,v1_cp,v3]
ps = [p1,p2_cp,p3]
ss = 100
p1s = linspace(p1,p2_cp,ss)
v2s = linspace(v1_cp,v3,ss)
v3s = linspace(v3,v1_cp,ss)
v1g = stater('P',p1s,'V',v1_cp,'air')['V']
p2g = stater('S',s3,'V',v2s,'air')['P']
p3g = stater('P',p1,'V',v3s,'air')['P']

for i in range(len(ps)):annotate(str(i+1),xy = (vs[i],ps[i]))

# Plot
ylim(0,6e5)
xlim(0,4)
plot(v1g,p1s,label='Process 1-2',color='blue')
plot(v2s,p2g,label='Process 2-3',color='red')
plot(v3s,p3g,label='Process 3-1',color='grey')
xlabel("Specific Volume (m^3/kg)")
ylabel("Pressure (Pa)")
legend()
showme()
clf()

q_in = stater('T',T2,'V',v1_cp,'air')['U'] - stater('T',T1,'P',p1,'air')['U']
print 'q_in = ',q_in/1000, 'kJ/kg'

w_out = -(stater('S',s3,'P',p3,'air')['U'] - stater('T',T2,'V',v1_cp,'air')['U'])
print 'w_out = ',w_out/1000, 'kJ/kg'

w_in = p1*(v1_cp-v3)
print 'w_in = ',w_in/1000, 'kJ/kg'

eta = (w_out+w_in)/q_in
print 'efficiency = ',eta
