##Author: Dan Steingart
##Date Started: 2016-10-10
##Notes: MS Example 4.4

from pithy import *

"""Steam enters a turbine operating at steady state with m_dot = 4600 kg/h.  At the inlet the pressure is 60 Bar at 400 C with a velocity of 10 m/s.   At the exit, the pressure is 0.1 bar with a quality of 0.9 at 30 m/s.  Calculate the rate of heat transfer and the surroundings in kW, if the turbine produces 1000 kW."""

m1dot = 4600 #kg/h
p1 = 60 *100 * 1000 #bar to Pa
T1 = 600+273 #K
V1 = 10 # m/s

p2 = .1 * 100 * 1000 #bar to Pa
x2 = 0.9
V2 = 100 #m/s

Wdotcv = 1000 * 1000 #kW to W
#What is the heat loss

State_1 = stater('P',p1,'T',T1,'water')
State_2 = stater('P',p2,'Q',x2,'water')

deltaH = State_2['H'] - State_1['H'] 

deltaKE = (V2**2 - V1**2)/2

Qdotcv = Wdotcv+m1dot*(deltaH+deltaKE)*(1/3600.)

whos(locals())

print
print "The Kinectic Energy change is %.2f %% of the total energy transfer" % (abs(deltaKE/(deltaH+deltaKE))*100)