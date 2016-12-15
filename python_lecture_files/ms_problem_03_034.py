##Author: Cody Nunno
##Date Started: 2016-09-25
##Notes: MS Problem 3.34

from pithy import *

# This is a symbolic problem, but for better illustration of how to use the properties, and for greater ease of tracing the paths in the case of work, it has also been worked using explicit states.

p1 = 1e5 # Pa
T1 = 400 # K
state1 = stater('T',T1,'P',p1,'water')
v1 = state1['V']
print 'v1 = ', v1, 'm^3/kg, p1 = ', p1/1000, 'kPa'

# Process 1-2
# This process is at constant temperature, such that p2 = 2*p1, so:
p2 = 2*p1 #Pa
T2 = T1
state2 = stater('T',T2,'P',p2,'water')
v2 = state2['V']
print 'v2 = ', v2, 'm^3/kg, p2 = ', p2/1000, 'kPa'

# Process 1-3
# This process is at constant volume, such that p3 = 2*p1, so:
p3 = 2*p1 #Pa
v3 = v1
state3 = stater('V',v3,'P',p3,'water')
T3 = state3['T']
print 'v3 = ', v3, 'm^3/kg, p3 = ', p3/1000, 'kPa'

# Process 1-4
# This process is at constant pressure, such that V4 = 2*V1, so:
v4 = 2*v1 #Pa
p4 = p1
state4 = stater('V',v4,'P',p4,'water')
T4 = state4['T']
print 'v4 = ', v4, 'm^3/kg, p4 = ', p4/1000, 'kPa'

# Process 1-5
# This process is at constant temperature, such that V5 = 2*V1, so:
v5 = 2*v1 #Pa
T5 = T1
state5 = stater('T',T5,'V',v5,'water')
p5 = state5['P']
print 'v5 = ', v5, 'm^3/kg, p5 = ', p5/1000, 'kPa'

# Now, we need to plot each process on the p-V diagram, and shade to indicate the work done
ss = 100
d = zeros(ss)

# Process 1-2
v2s = linspace(v2,v1,ss)
pg2 = stater('T',T1,'V',v2s,'water')['P']
plot(v2s,pg2,label='Process 1-2',color='blue')
fill_between(v2s,pg2,d,color='blue',alpha=.5)

# Process 1-3
v3s = linspace(v3,v1,ss)
T3s = linspace(T3,T1,ss)
pg3 = stater('T',T3s,'V',v3s,'water')['P']
plot(v3s,pg3,label='Process 1-3',color='green')
fill_between(v3s,pg3,d,color='green',alpha=.5)

# Process 1-4
p4s = linspace(p4,p1,ss)
T4s = linspace(T4,T1,ss)
vg4 = stater('T',T4s,'P',p4s,'water')['V']
plot(vg4,p4s,label='Process 1-4',color='red')
fill_between(vg4,p4s,d,color='red',alpha=.5)

# Process 1-5
v5s = linspace(v5,v1,ss)
pg5 = stater('T',T5,'V',v5s,'water')['P']
plot(v5s,pg5,label='Process 1-5',color='grey')
fill_between(v5s,pg5,d,color='grey',alpha=.5)

ps = [p1,p2,p3,p4,p5]
vs = [v1,v2,v3,v4,v5]

for i in range(len(ps)):annotate(str(i+1),xy = (vs[i],ps[i]))

ylim(0,2.5e5)
xlim(0,5)
xlabel("Volume (m^3/kg)")
ylabel("Pressure (Pa)")
legend()
showme()
clf()

# Finally, we need to determine whether the work done is positive or negative.  The work is determined by the integral from state 2 to state 1 (upper and lower limits) or pdV.  p in this context must be represented in terms of volume here, therefore, whether the volume at state two is greater or less than the volume at state one solely determines the sign of the work, as the difference will always be postive or negative following that.  So:

print """
In process 1-2, work is done on the vapor.  
In process 1-3, no change in volume is observed, therefore no work is done.
In processes 1-4 and 1-5, work is done by the system."""
