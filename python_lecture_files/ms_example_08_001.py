##Author: Dan Steingart
##Date Started: 2016-11-11 
##Notes: MS Example 8.1 and 8.2

from pithy import *
def pp(var,unit): print "%s=%s %s" % (var,round(eval(var),3),unit)    

#From the problem we are told the output power target
W_net = 100 * 1000*1000 #W
eta_turbine = linspace(.75,1,100) #this is what we'll do to explore efficiency as a function of turbine efficiciency
state = {} #set up state dictionary

#State 1 - Entering Turbine
x_1 = 1
p_1 = 80e5 #kpA
state[1] = stater('P',p_1,'Q',x_1,'water')

#State 2s - Assume a perfect Turbine
p_2 = 0.008 * 1000*1000 #pA
s_2s = state[1]['S']
state['2s'] = stater('P',p_2,'S',s_2s,'water')

#State 2 real - Leaving Turbine for Real, entering Cooler
h_2 = state[1]['H']-eta_turbine*(state[1]['H']-state['2s']['H'])
state[2] = stater('P',p_2,'H',h_2,'water')

#State 3 Leaving Cooler entering pupmp
p_3 = p_2
x_3 = 0 
state[3] = stater('P',p_3,'Q',x_3,'water')

#State 4 LEaving pump entering boiler
s_4 = state[3]['S']
p_4 = p_1
state[4] = stater('P',p_4,'S',s_4,'water')

#Find works
Wbym_Turbine_1 = state[1]['H'] - state[2]['H']
Wbym_Pump      = state[3]['H'] - state[4]['H']

#Find heats
Q_in_main      = state[1]['H'] - state[4]['H']
Q_out_main     = state[2]['H'] - state[3]['H']
#find eta thermal
W_netbym   = Wbym_Turbine_1+ Wbym_Pump
Q_in_total = Q_in_main 

eta_thermal = W_netbym/Q_in_total
eta_carnot = 1 - state[3]['T']/state[1]['T']

p = abs(eta_turbine-.85).argmin()

pp('eta_carnot','')

print "For a turbine efficiency of %.2f, the system thermal efficiency is %.2f" % (eta_turbine[p],eta_thermal[p])

#mass flow rate
m_dot = 3600*W_net / W_netbym

print "For the isentropic case, the mass flow rate is %.2f kg/h" % m_dot[-1]

#condensor transfer
print "For the 0.85 turbine efficincy case the mass flow rate is %.2f kg/h" % m_dot[p]
#condensor transfer

Q_out = m_dot*(state[2]['H']-state[3]['H'])/3600
print "For the isentropic turbine, Qout is %.2f MW" % (Q_out[-1]/1e6)

print "For the 0.85 isentropic turbine, Qout is %.2f MW" % (Q_out[p]/1e6)

plot(eta_turbine,eta_thermal)
axhline(eta_carnot,color="red",linestyle="--")
annotate("Carnot Efficiency",xy=(.99,.44),ha="right")
annotate("System Thermal Efficiency",xy=(.99,.32),ha="right")
xlabel("Turbine Efficiency")
ylabel("Thermal Efficiency")
xlim([.75,1])
showme()
clf()

print "State 3 =", state[3]['T'],"K"
print "State 4 = ",state[4]['T'],"K"


