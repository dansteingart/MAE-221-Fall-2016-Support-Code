##Author: Dan Steingart
##Date Started: 2016-11-11 
##Notes: MS 8.5 with some other stuff


from pithy import *
import pandas as pd

def pp(var,unit):
    print "%s=%s %s" % (var,round(eval(var),3),unit)    


W_net = 100 * 1000 #kW

state = {}
#states.append([])

eta_turbine = linspace(.1,.99,100)
#eta_turbine =.85
#State 1
T_1 = 480 + 273.
p_1 = 80*100*1000 #
state_1 = stater('P',p_1,'T',T_1,'water')
state[1] = state_1

#State 2s
p_2 = 7*100*1000 #Pa
s_2s = state_1['S']
state_2s = stater('P',p_2,'S',s_2s,'water')

#State 2 real
h_2 = state_1['H']-eta_turbine*(state_1['H']-state_2s['H'])
state_2 = stater('P',p_2,'H',h_2,'water')
state[2] = state_2
#State 3s
p_3 = 10*100*1000*0.008 #Pa
s_3s = state_2['S']
state_3s = stater('P',p_3,'S',s_3s,'water')

#State 3 real
h_3 = state_2['H']-eta_turbine*(state_2['H']-state_3s['H'])
state_3 = stater('P',p_3,'H',h_3,'water')
state[3] = state_3

#State 4
p_4 = p_3
x_4 = 0 
state_4 = stater('P',p_4,'Q',x_4,'water')
state[4] = state_4

#State 5
s_5 = state_4['S']
p_5 = p_2
state_5 = stater('P',p_5,'S',s_5,'water')
state[5] = state_5

#State 6
x_6 = 0
p_6 = p_5
state_6 = stater('P',p_6,'Q',x_6,'water')
state[6] = state_6

#state 7
p_7 = p_1
s_7 = state_6['S']
state_7 = stater('P',p_7,'S',s_7,'water')
state[7] = state_7

#solve for y
y = (state_6['H'] - state_5['H'])/(state_2['H']-state_5['H'])

#Find works
Wbym_Turbine_1 = (state[1]['H'] - state[2]['H'])/1000
Wbym_Turbine_2 = (state[2]['H'] - state[3]['H'])/1000
Wbym_Pump_1    = (state[4]['H'] - state[5]['H'])/1000
Wbym_Pump_2    = (state[6]['H'] - state[7]['H'])/1000

#Find heats
Q_in_main      = (state[1]['H'] - state[7]['H'])/1000

#find eta thermal
W_netbym   = Wbym_Turbine_1+ (1-y)*Wbym_Turbine_2 + (1-y)*Wbym_Pump_1 + Wbym_Pump_2 
Q_in_total = Q_in_main

eta_thermal = W_netbym/Q_in_total

p = 84
pp('eta_turbine[p]',"")
pp('eta_thermal[p]',"")

plot(eta_turbine,y)
showme()
clf()



#mass flow rate
m_dot = 3600*W_net / W_netbym

pp('m_dot[p]','kg/h')

#condensor transfer

Q_out = m_dot*(state[4]['H']-state[3]['H'])/3600
pp('Q_out[p]',"kW")


#plots!
plot(eta_turbine,eta_thermal,label="Siphon Reheat")


#Plot Differences for Old Case

#State 3
p_3 = p_2 #Pa
T_3 = 440+273
state_3 = stater('P',p_3,'T',T_3,'water')

#State 4s
p_4 = 10*100*0.008*1000 #Pa
s_4s = state_3['S']
state_4s = stater('P',p_4,'S',s_4s,'water')

#State 4 real
h_4 = state_3['H']-eta_turbine*(state_3['H']-state_4s['H'])
state_4 = stater('P',p_2,'H',h_4,'water')

#State 5
p_5 = p_4
x_5 = 0 
state_5 = stater('P',p_5,'Q',x_5,'water')

#State 6
s_6 = state_5['S']
p_6 = p_1
state_6 = stater('P',p_6,'S',s_6,'water')

#Find works
Wbym_Turbine_1 = (state_1['H'] - state_2['H'])/1000
Wbym_Turbine_2 = (state_3['H'] - state_4['H'])/1000
Wbym_Pump      = (state_6['H'] - state_5['H'])/1000

#Find heats
Q_in_main      = (state_1['H'] - state_6['H'])/1000
Q_in_reheat    = (state_3['H'] - state_2['H'])/1000

#find eta thermal
W_netbym   = Wbym_Turbine_1+ Wbym_Turbine_2 + Wbym_Pump
Q_in_total = Q_in_main + Q_in_reheat

eta_thermal = W_netbym/Q_in_total

#pp('eta_thermal',"")

#mass flow rate
m_dot = 3600*W_net / W_netbym

#pp('m_dot','kg/h')

#condensor transfer

Q_out = m_dot*(state_4['H']-state_5['H'])/3600
#pp('Q_out',"kW")

plot(eta_turbine,eta_thermal,label="Combuster Reheat")
legend(loc="best")
xlabel("Turbine Efficiency")
ylabel("Thermal Efficiency")


showme()
clf()

