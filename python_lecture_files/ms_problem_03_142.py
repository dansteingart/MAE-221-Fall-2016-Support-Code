##Author: Wenkai Liang
##Date Started: 10-03-2016
##Notes: 

from pithy import *
def wqp(val,unit): print "%s = %.1f %s" %(val,eval(val)/1000,unit)
def pp(val,unit): print "%s = %.3f %s" %(val,eval(val),unit)

R = 287.058 #J/kg/K
# state1
v1 = 1.0 #m^3/kg
p1 = 5.0e5 #Pa    
T1 = p1*v1/R # K
state1 = stater('V',v1,'P',p1,'air')

# state2
v2 = 5.0 #m^3/kg
p2 = 1.0e5 #Pa
T2 = p2*v2/R # K
state2 = stater('V',v2,'P',p2,'air')

# state3
v3 = 1.0 #m^3/kg
p3 = 1.0e5 #Pa
T3 = p3*v3/R # K
state3 = stater('V',v3,'P',p3,'air')
states = {1:state1,2:state2,3:state3}
print state_table(states)


# process 1-2 isothermal
# Using only the ideal gas assumption
# W12 = integral(pdV) = integral(mRT/V*dV) = P1*V1*ln(V2/V1)
w12 = p1*v1*log(v2/v1)
# Constant temperature, therefore constant internal energy -> Q-W = 0
q12 = w12
# Using CoolProps
w12_CP = R*state1['T']*log(v2/v1)
q12_CP = w12_CP

# process 2-3 constant pressure
# Using only the ideal gas assumption
# Assume cv for this process approx 0.855 kJ/kg
c_v23 = 0.855*1000 # J/kg
w23 = p2*(v3-v2)
q23 = w23 + c_v23*(T3 - T2)
# Using CoolProps
w23_CP = p2*(v3-v2)
q23_CP = w23_CP + (state3['U'] - state2['U'])

# process 3-1 constant volume
# Using only the ideal gas assumption
# Same temperature change, same cv
c_v31 = c_v23
# u1 = u2, q = u1-u3
q31 = c_v31*(T1 - T3)
# Using CoolProps
q31_CP = state1['U'] - state3['U']
# work done is 0
w31 = 0.0

# thermal efficiency
# Using only the ideal gas assumption
efficiency = (w12 + w23 + w31)/(q12 + q31)
# Using CoolProps
efficiency_CP = (w12_CP + w23_CP + w31)/(q12_CP + q31_CP)

print 'Using the Ideal Gas Law:'
wqp('w12','kJ/kg')
wqp('q12','kJ/kg')
wqp('w23','kJ/kg')
wqp('q23','kJ/kg')
wqp('w31','kJ/kg')
wqp('q31','kJ/kg')
pp('efficiency','')
print ''
print 'Using Coolprops:'
wqp('w12_CP','kJ/kg')
wqp('q12_CP','kJ/kg')
wqp('w23_CP','kJ/kg')
wqp('q23_CP','kJ/kg')
wqp('w31','kJ/kg')
wqp('q31_CP','kJ/kg')
pp('efficiency_CP','')