##Author: Dan Steingart
##Date Started: 2016-11-11
##Notes: Examples 8.4

from pithy import *

def pp(var,unit):
    print "%s=%s %s" % (var,round(eval(var),3),unit)    


W_net = 100 * 1000 #kW

eta_turbine = linspace(.75,.99,100)

state = {}
#State 1
T_1 = 480 + 273.
p_1 = 80*100*1000 #Pa
state[1] = stater('P',p_1,'T',T_1,'water')

#State 2s
p_2 = 7*100*1000 #Pa
s_2s = state[1]['S']
state['2s'] = stater('P',p_2,'S',s_2s,'water')

#State 2 real
h_2 = state[1]['H']-eta_turbine*(state[1]['H']-state['2s']['H'])
state[2] = stater('P',p_2,'H',h_2,'water')

#State 3
p_3 = p_2 #kpA
T_3 = 440+273
state[3] = stater('P',p_3,'T',T_3,'water')

#State 4s
p_4 = 10*100*0.008 *1000 #Pa
s_4s = state[3]['S']
state['4s'] = stater('P',p_4,'S',s_4s,'water')

#State 4 real
h_4 = state[3]['H']-eta_turbine*(state[3]['H']-state['4s']['H'])
state[4] = stater('P',p_2,'H',h_4,'water')

#State 5
p_5 = p_4
x_5 = 0 
state[5] = stater('P',p_5,'Q',x_5,'water')

#State 6
s_6 = state[5]['S']
p_6 = p_1
state[6] = stater('P',p_6,'S',s_6,'water')

#Find works
Wbym_Turbine_1 = (state[1]['H'] - state[2]['H'])/1000
Wbym_Turbine_2 = (state[3]['H'] - state[4]['H'])/1000
Wbym_Pump      = (state[6]['H'] - state[5]['H'])/1000

#Find heats
Q_in_main      = (state[1]['H'] - state[6]['H'])/1000
Q_in_reheat    = (state[3]['H'] - state[2]['H'])/1000

#find eta thermal
W_netbym   = Wbym_Turbine_1+ Wbym_Turbine_2 + Wbym_Pump
Q_in_total = Q_in_main + Q_in_reheat

eta_thermal = W_netbym/Q_in_total
e85 = abs(eta_turbine-.85).argmin()
pp('eta_turbine[e85]','')
pp('eta_thermal[e85]','')



#mass flow rate
m_dot = 3600*W_net / W_netbym

pp('m_dot[e85]','kg/h')

#condensor transfer

Q_out = m_dot*(state[4]['H']-state[5]['H'])/(3600*1000*1000)
pp('Q_out[e85]',"MW")




plot(eta_turbine,eta_thermal)
xlabel("Turbine Efficiency")
ylabel("Thermal Efficiency")

showme()
clf()

