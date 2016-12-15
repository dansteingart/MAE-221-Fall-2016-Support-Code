##Author: Dan Steingart
##Date Started: 2016-11-11
##Notes: Example 8.3

"""
Steam is the working fluid in an ideal Rankine cycle with superheat and reheat. Steam enters the first-stage turbine at 8.0 MPa, 480 C, and expands to 0.7 MPa. It is then reheated to 440 C before entering the second-stage turbine, where it expands to the condenser pressure of 0.008 MPa. The net power output is 100 MW. Determ#ine (a) the thermal efficiency of the cycle, (b) the mass flow rate of steam, in kg/h, (c) the rate of heat transfer Qout from the condensing steam as it passes through the condenser, in MW. Discuss the effects of reheat on the vapor power cycle.
"""

from pithy import *

#Write out givens: 

W_dot = 100*1000*1000 #W

states = {}

#start with state 1 before first turbine
p1 = 8e6 #Pa
T1 = 480 + 273 #K
states[1] = stater('P',p1,'T',T1,'water')

#state 2: leaving turbine one, entering reheat
p2 = 7e5 #Pa
#we are not told otherwise: turbine is isentropic:
s2 = states[1]['S']
states[2] = stater('P',p2,'S',s2,'water')

#state 3: leaving reheat, entering turbine 2
T3 = 440+273 #given above
p3 = p2 #no pressure drop through heat exchanger
states[3] = stater('P',p3,'T',T3,'water')

#state 4: leaving turbine two, entering condenser
p4 = 0.008e6 #Pa
#we are not told otherwise: turbine is isentropic:
s4 = states[3]['S']
states[4] = stater('P',p4,'S',s4,'water')

#state 5 leaving condenser, entering pump
p5 = p4 #no pressure drop through heat exchanger
x5 = 0  #we are not told otherwise, so we assume we are just condensing to a saturated liqui
states[5] = stater('P',p5,'Q',x5,'water')

#state 6: leaving pump, entering boiler
p6 = p1 #Pa
#we are not told otherwise: pump is isentropic:
s6 = states[5]['S']
states[6] = stater('P',p6,'S',s6,'water')


#We have defined all states with the given information
print state_table(states)

print "Part a) The Thermal Efficiency of the Cycle"

#Boiler
Q61_by_m = states[1]['H'] - states[6]['H'] 

#Reheat
Q23_by_m = states[3]['H'] - states[2]['H'] 

#Turbine 1
W12_by_m = states[1]['H'] - states[2]['H'] 

#Turbine 2
W34_by_m = states[3]['H'] - states[4]['H'] 

#Pump
W56_by_m = states[5]['H'] - states[6]['H'] 

eta = (W12_by_m+W34_by_m+W56_by_m)/(Q61_by_m+Q23_by_m)
print "%.3f" % eta
print ""

print "Part b) The Mass Flow Rate of the cycle"
m_dot = W_dot / (W12_by_m+W34_by_m+W56_by_m)
print "%.3e kg/s" % m_dot 
print "%.3e kg/h" % (m_dot*3600) 
print ""

print "Part c) Q_out for the cycle"
Q_45_by_m = states[5]['H'] - states[4]['H'] 
Q_out = Q_45_by_m * m_dot
print "%.2f MW" % (Q_out/1e6) 


##Extra Stuff
figure(figsize=(10,3))
subplot(1,2,1)
pv_phase_envelope('water',fill=True)
for n in range(1,7): annotate('%i'%n,xy=(states[n]['V'],states[n]['P']))
loglog()
xlabel("Volume (m^3/kg)")
ylabel("Pressure (Pa)")

subplot(1,2,2)
ts_phase_envelope('water',fill=True)
for n in range(1,7): annotate('%i'%n,xy=(states[n]['S'],states[n]['T']))
xlim(0,10000)
ylim(250,800)
xlabel("Entropy (kJ/(kg K))")
ylabel("Temperature (K)")

showme()
clf()





