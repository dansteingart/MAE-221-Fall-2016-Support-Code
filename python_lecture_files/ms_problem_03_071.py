##Author: Cody Nunno
##Date Started: 2016-09-29
##Notes: 

from pithy import *

# Step 1: Begin with what we know
# We don't know anything about the piston, so we'll consider the system to just be the gas inside the cylinder
p1 = 1.5e5 #Pa (pressure)
x1 = 0.20 # (quality)
state1 = stater('Q',x1,'P',p1,'water')
v1 = state1['V']
u1 = state1['U']
T1 = state1['T']
print u1

#Step 2: find the second state (where the piston stops)
v_ratio = 8.0/5.0 # ratio of v2 to v1
v2 = v_ratio*v1 # m^3/kg (s. volume)
p2 = p1 #Pa (pressure)
state2 = stater('V',v2,'P',p2,'water')
x2 = state2['Q']
T2 = state2['T']


#Step 3: find the third state where the water is fully vaporized
v3 = v2 # m^3/kg (s. volume)
x3 = 1.0 # (quality)
state3 = stater('Q',x3,'V',v3,'water')
u3 = state3['U']
T3 = state3['T']

# Print the states, for the sake of clarity
states = {1:state1,2:state2,3:state3}
print state_table(states)

#Step 4: Find work and heat transfer
#W = integral(pdV) or W/m = pdv
w = p2*(v2-v1)
print "Work for the process is:",w/1000,"kJ/kg"
# q-W = dU
q = w + (u3-u1)
print "Heat transfer for the process is:",q/1000,"kJ/kg"

#Step 5: Plot on T-v diagram
ss = 100
v2s = linspace(v1,v2,ss)
v3s = linspace(v2,v3,ss)
x3s = linspace(x2,x3,ss)

Tg2 = stater('P',p1,'V',v2s,'water')['T']
Tg3 = stater('V',v2,'Q',x3s,'water')['T']

# Label the individual states
vs = [v1,v2,v3]
Ts = [T1,T2,T3]

for i in range(len(Ts)):annotate(str(i+1),xy = (vs[i],Ts[i]))

# Plot
ylim(370,430)
xlim(0.10,0.60)
tv_phase_envelope('water')
plot(v2s,Tg2,label='Process 1-2',color='blue')
plot(v3s,Tg3,label='Process 2-3',color='red')
xlabel("Specific Volume (m^3/kg)")
ylabel("Temperature (K)")
legend()
showme()
clf()