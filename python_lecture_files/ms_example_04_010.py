##Author: Dan Steingart
##Date Started: 2016-10-10
##Notes: MS Example 2016-10-10

from pithy import *
"""
An industrial process discharges 5.6e3 m3/min of gaseous combustion products at 204.4 C, 1 bar. A proposed system for utilizing the combustion products combines a heat recovery steam generator with a turbine. At steady state, combustion products exit the steam generator at 126.6 C and 1 bar and a separate stream of water enters at 275.8 kPa, and 38.9 C with a mass flow rate of 124.7 kg/min. At the exit of the turbine, the pressure is 6.9 kPA and the quality is 93%. Heat transfer from the outer surfaces of the steam generator and turbine can be ignored, as can the changes in kinetic and potential energies of the flowing streams. There is no significant pressure drop for the water flowing through the steam generator. The combustion products can be modeled as air as an ideal gas.

(a) Determine the power developed by the turbine, in kJ/min.

(b) Determine the turbine inlet temperature.

(c) Evaluating the power developed at 0.08 USD per kW-hr, determine the value of the power, in USD/year, for 8000 hours of operation annually.
"""

St = {}

#Solve for State 1 and mdot 1
AV_1  = 5.6e3/60# m^3/s
T_1   = 205 + 273 #K
P_1   = 1e5 # Pa
St[1]   = stater('P',P_1,'T',T_1,'air')
mdot_1 = AV_1/St[1]['V']

#Solve for state 2
T_2  = 126 + 273 #K
P_2  = 1e5 # Pa
St[2]  = stater('P',P_2,'T',T_2,'air')
mdot_2 = mdot_1

#Solve for state 3
T_3  = 38.9 + 273 # C
P_3  = 275.3 * 1000 # Pa
St[3]  = stater('P',P_3,'T',T_3,'water')
P_4  = P_3
mdot_3  = 124.7 /60 # kg/s

#Solve for state 5
P_5  = 6.9*1000   # Pa
x_5  = 0.93
St[5]  = stater('P',P_5,'Q',x_5,'water')


#What's missing here is how we  get from state 5 to state 3, we are missing a pump.  We need an understanding or an assumption of entropy to get this done.  If we assumpe that state 6 hows t

#Through the condenser there is no pressure drop, so:  
P_6 = P_5

#Through the pump there is no entropy production, so
Q_6 = 0

#Solve for state 6, before the pump, after the condensor
St[6] = stater('P',P_6,'Q',Q_6,'water')

#Problem A
#W = mdot1*h1 + mdot3*h3 - mdot1*h2 - mdot3*h5
Wdot_turbine = mdot_1*(St[1]['H'] + St[2]['H'])+mdot_3*(St[3]['H']-St[5]['H'])

print "The Turbine in generating: ", round(Wdot_turbine/1000,2), 'kW'

#Problem B
#Solve for State 4 to find T_4
H_4 = St[3]['H'] + (mdot_1/mdot_3)*(St[1]['H']-St[2]['H'])
St[4] = stater('P',P_4,'H',H_4,'water')
print "T4 = ", round(St[4]['T']-273,2), 'C'

#Problem C 
DpKWhr = 0.08
DpY = (Wdot_turbine/1000 * 24*365) * DpKWhr 
print "The plant is generating: ", round(DpY/1000,2), 'K$/year'

#Print a nice table
print state_table(St)

#Make an isentropic pumping process
p63 = linspace(P_6,P_3,100)
St63 = stater('P',p63,'S',St[6]['S'],'water')

#Make an isobaric heating process
T34 = linspace(St[3]['T'],St[4]['T'],100)
St34 = stater('T',T34,'P',P_3,'water')



#make T-S and P-V plots
figure(figsize=(10,5))
subplot(1,2,1)
pv_phase_envelope('water',fill=True)
for i in range(3,7):
    annotate(str(i),xy=(St[i]['V'],St[i]['P']))

plot(St34['V'],St34['P'],'r')
plot(St63['V'],St63['P'],'r')
plot([St[4]['V'],St[5]['V']],[St[4]['P'],St[5]['P']],'r')
plot([St[5]['V'],St[6]['V']],[St[5]['P'],St[6]['P']],'r')

ylabel("P (Pa)")
xlabel("V (m^/3)")
xlim(1e-4,1e3)
ylim(1e3,1e8)
loglog()

subplot(1,2,2)
ts_phase_envelope('water',fill=True)
for i in range(3,7):
    annotate(str(i),xy=(St[i]['S'],St[i]['T']))

plot(St34['S'],St34['T'],'r')
plot(St63['S'],St63['T'],'r')
plot([St[4]['S'],St[5]['S']],[St[4]['T'],St[5]['T']],'r')
plot([St[5]['S'],St[6]['S']],[St[5]['T'],St[6]['T']],'r')

ylim(273,750)
ylabel("T (K)")
xlabel("s (J/(kg K))]")
showme()
clf()

#ts_phase_envelope('water',fill=True)
for i in [3,6]:
    annotate(str(i),xy=(St[i]['S'],St[i]['T']))

# # plot(St34['S'],St34['T'],'r')
plot(St63['S'],St63['T'],'r')
# plot([St[4]['S'],St[5]['S']],[St[4]['T'],St[5]['T']],'r')
# plot([St[5]['S'],St[6]['S']],[St[5]['T'],St[6]['T']],'r')
# ylim([300,330])
# xlim([0,2000])
ylabel("T (K)")
xlabel("s (J/(kg K))")
showme(dpi=200)
clf()





