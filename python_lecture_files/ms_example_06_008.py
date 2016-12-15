##Author: Dan Steingart
##Date Started: 2016-10-10
##Notes: MS Example 6.8
"""Components of a heat pump for supplying heated air to a dwelling are shown in the schematic below. At steady state, Refrigerant 22 enters the compressor at  5 C, 3.5 bar and is compressed adiabatically to 75 C, 14 bar. From the compressor, the refrigerant passes through the condenser, where it condenses to liquid at 28 C, 14 bar. The refrigerant then expands through a throttling valve to 3.5 bar. The states of the refrigerant are shown on the accompanying T-s diagram. Return air from the dwelling enters the condenser at 20 C, 1 bar with a volumetric flow rate of 0.42 m3/s and exits at 50 C with a negligible change in pressure. Using the ideal gas model for the air and neglecting kinetic and potential energy effects, (a) determine the rates of entropy production, in kW/K, for control volumes enclosing the condenser, compressor, and expansion valve, respectively. (b) Discuss the sources of irreversibility in the components considered in part (a)."""

from pithy import *

St = {}

#Set States
T1 = 273-5 #K
p1 = 3.5e5 #Pa
St[1] = stater('T',T1,'P',p1,'R22')

T2 = 75+273 #K
p2 = 14e5
St[2] = stater('T',T2,'P',p2,'R22')

T3 = 28+273 #K
p3 = 14e5 #Pa
St[3] = stater('T',T3,'P',p3,'R22')

h4 = St[3]['H']
p4 = p1 #Pa
St[4] = stater('P',p4,'H',h4,'R22')

T5 = 20 + 273. #K
p5 = 1e5 #Pa
St[5] = stater('T',T5,'P',p5,'air')

T6 = 50 + 273. #K
p6 = p5
R = 8.314/28.97  # J/kg L
St[6] = stater('T',T6,'P',p6,'air')


AV_air = .42 #m^3/s
mdot_air = AV_air * p5/(R*T5) / 1000
cp_air = 1.005 #kJ/kj K
print state_table(St)

#Condenser
#first solve for m_r22
mdot_r22 = mdot_air*cp_air*(T6-T5)/((St[2]['H']-St[3]['H'])/1000)

#now, solve for entropy created 
sigma_air = cp_air*log(T6/T5)
sigma_r22_cond = (St[3]['S']-St[2]['S'])/1000
sigmadot_cond = mdot_air*sigma_air+mdot_r22*sigma_r22_cond
#Compressor
sigmadot_comp = mdot_r22 * (St[2]['S']-St[1]['S'])/1000
#Valve
sigmadot_valve = mdot_r22 * (St[4]['S']-St[3]['S'])/1000



#Print the results in kW/k
results = whos(locals(),pattern="poof")

keys = []
for k in results.keys():
    if k.find("sigmadot") > -1: keys.append(k)

losses = sorted(keys,key = lambda k: results[k])
losses.reverse()

for l in losses:
    print "%s = %.6f kW/k" % (l,results[l])