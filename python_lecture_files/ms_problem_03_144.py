##Author: Cody Nunno
##Date Started: 2016-10-23
##Notes: MS Problem 3.144

from pithy import *

def wqp(val,unit): print "%s = %.3f %s" %(val,eval(val)/1000,unit)
def pp(val,unit): print "%s = %.3f %s" %(val,eval(val),unit)

# Step 1: Write down what we know about the states
R = 287.058 #J/kg/K
k = 1.4
#state 1
T1 = 600.0 #K
p1 = 0.5e6 # Pa

#state 2
T2 = T1
p2 = 0.4e6 # Pa

# state 3
p3 = 0.3e6 # Pa

# Step 2: Solve for the other variables at the rest of the states
# state 1
v1 = R*T1/p1

# state 2
v2 = R*T2/p2

# state 3
v3 = (p2*v2**k/p3)**(1/k)
T3 = p3*v3/R

# state 4
v4 = v1
p4 = p3
T4 = p4*v4/R

# Step 3: Plot the states
ss = 100
#Process 1-2
v12 = linspace(v1,v2,ss)
p12 = R*T1/v12
#Process 2-3
v23 = linspace(v2,v3,ss)
p23 = p2*v2**k/(v23**k)
#Process 3-4
v34 = linspace(v3,v4,ss)
p34 = linspace(p3,p4,ss)
#Process 3-4
v41 = linspace(v4,v1,ss)
p41 = linspace(p4,p1,ss)

# Label the individual states
vs = [v1,v2,v3,v4]
ps = [p1,p2,p3,p4]

for i in range(len(ps)):annotate(str(i+1),xy = (vs[i],ps[i]))

# Plot
ylim(250000,550000)
xlim(0.30,0.60)
plot(v12,p12,label='Process 1-2',color='blue')
plot(v23,p23,label='Process 2-3',color='red')
plot(v34,p34,label='Process 3-4',color='green')
plot(v41,p41,label='Process 4-1',color='yellow')
xlabel("Specific Volume (m^3/kg)")
ylabel("Pressure (Pa)")
legend()
showme()
clf()

# Step 4: Solve part a (find the work and heat transfer for each process)
cv = 718.0 #J/kgK
# Process 1-2
# Isothermal, therefore Delta U = 0
# W12 = integral(pdV) = integral(mRT/V*dV) = P1*V1*ln(V2/V1)
w12 = p1*v1*log(v2/v1)
# Constant temperature, therefore constant internal energy -> Q-W = 0
q12 = w12

# Process 2-3
# Polytropic
# W23 = (P3V3-P2V2)/(1-k)=R(T3-T2)/(1-k)
#w23 = p1*v1**k*(v2**(1-k)-v1**(1-k))/(1-k)
w23 = R*(T3-T2)/(1-k)
# k=1.4 for a polytropic process indicates an adiabatic process, therefor Q = 0
q23 = 0.0

# Process 3-4
# Constant Pressure
w34 = p3*(v4-v3)
q34 =  w34 + cv*(T4 - T3)

# Process 4-1
# Constant volume: W41 = 0
w41 = 0
q41 = cv*(T1 - T4)

# Step 5: Find the efficiency
efficiency = (w12 + w23 + w34 + w41)/(q12 + q41)

print 'Part a:'
wqp('w12','kJ/kg')
wqp('q12','kJ/kg')
wqp('w23','kJ/kg')
wqp('q23','kJ/kg')
wqp('w34','kJ/kg')
wqp('q34','kJ/kg')
wqp('w41','kJ/kg')
wqp('q41','kJ/kg')
print ''
print 'Part d:'
pp('efficiency','')
