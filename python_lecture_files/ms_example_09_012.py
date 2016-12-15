##Author: Dan Steingart
##Date Started: 2016-11-15
##Notes: Example 9.12

from pithy import *


"""A combined gas turbine vapor power plant has a net power output of 45 MW. Air enters the compressor of the gas turbine at 100 kPa, 300 K, and is compressed to 1200 kPa. The isentropic efficiency of the compressor is 84%. The condition at the inlet to the turbine is 1200 kPa, 1400 K. Air expands through the turbine, which has an isentropic efficiency of 88%, to a pressure of 100 kPa. The air then passes through the interconnecting heat- recovery steam generator and is finally discharged at 400 K. Steam enters the turbine of the vapor power cycle at 8 MPa, 400 C, and expands to the condenser pressure of 8 kPa. Water enters the pump as saturated liquid at 8 kPa. The turbine and pump of the vapor cycle have isentropic efficiencies of 90 and 80%, respectively.
(a) Determine the mass flow rates of the air and the steam, each in kg/s; the net power developed by the gas turbine and vapor power cycle, each in MW; and the thermal efficiency."""

#Work the Cycle.  Using coolprops b/c I can.

st = {}

#State One, Air Entering Compressor
T1 = 300 #K
p1 = 1e5 #Pa
st[1] = stater('T',T1,'P',p1,'air')

#State Two, After comp before comb 
p2 = 12*p1 #given, Pa
s2s = st[1]['S']
eta_comp = .84
st['2s'] = stater('S',s2s,'P',p2,'air')
h2 = st[1]['H'] + (st['2s']['H']-st[1]['H'])/eta_comp
st[2] = stater('H',h2,'P',p2,'air')

#State Three, After comb before turb 
p3 = p2 #given, Pa
T3 = 1400 #K
st[3] = stater('T',T3,'P',p3,'air')

#State Four, After turb before exchanger 
p4 = p1 #given, Pa
s4s = st[3]['S'] #K
eta_turb_1 = .88
st['4s'] = stater('S',s4s,'P',p4,'air')
h4 = st[3]['H'] - (st[3]['H']-st['4s']['H'])*eta_turb_1
st[4] = stater('H',h4,'P',p4,'air')

#State Five, After  exchanger 
p5 = p4 #given, Pa
T5 = 400 #K, given
st[5] = stater('T',T5,'P',p5,'air')

#State 6, Rankine Cycle, after Exchanger before Turbine 2
T6 = 400+273 #K
p6 = 8e6 #MPa
st[6] = stater('T',T6,'P',p6,'water')

#State 7, Rankine Cycle, after Turbine 2 before condenser
p7 = 8e3 #MPa
s7s = st[6]['S']
st['7s'] = stater('P',p7,'S',s7s,'water')
eta_turb_2 = .9
h7 = st[6]['H'] - (st[6]['H']-st['7s']['H'])*eta_turb_2
st[7] = stater('H',h7,'P',p7,'water')

#State 8, Rankine Cycle, after condenser before pump
x8 = 0 #Given
p8 = p7
st[8] = stater('Q',x8,'P',p8,'water')

#State 9, Rankine Cycle, after  pump before exchanger
p9 = p6
s9s = st[8]['S']
eta_pump = .8
st['9s'] = stater('Q',x8,'P',p8,'water')
h9 = st[8]['H'] + (st['9s']['H']-st[8]['H'])/eta_pump
st[9] = stater('H',h9,'P',p9,'water')

#Find Ratio of mass flow rates using heat exchanger
ratio = (st[4]['H']-st[5]['H'])/(st[6]['H']-st[9]['H'])

Wnet = 45e6 #W, Given)

#short hand to make the next part easier

h1 = st[1]['H']
h2 = st[2]['H']
h3 = st[3]['H']
h4 = st[4]['H']
h5 = st[5]['H']
h6 = st[6]['H']
h7 = st[7]['H']
h8 = st[8]['H']
h9 = st[9]['H']

m_dot_air = Wnet/((h3-h4)+(h1-h2)+ratio*((h6-h7)+(h8-h9)))
print "m_dot_air = %.2f kg/s" % m_dot_air
m_dot_water = m_dot_air*ratio
print "m_dot_water = %.2f kg/s" % m_dot_water

W_dot_brayton = m_dot_air*((h3-h4)+(h1-h2))
print "W_dot_brayton = %.2f MW" % (W_dot_brayton/1e6)
W_dot_rankine = m_dot_water*((h6-h7)+(h8-h9))
print "W_dot_brayton = %.2f MW" % (W_dot_rankine/1e6)
Q_in = m_dot_air*((h3-h2))
print "Q_in = %.2f MW" % (Q_in/1e6)
eta = Wnet/Q_in
print "eta = %.2f" % (eta)

print state_table(st)