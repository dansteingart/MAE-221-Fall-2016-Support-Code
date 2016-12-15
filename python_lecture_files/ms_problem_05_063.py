##Author: Wenkai Liang
##Date Started: 10/10/2016
##Notes: 

from pithy import *

# temperatures
T_C = 273.0+9.0 #K
T_H = 273.0+21.0 #K

#(a)  the amount of energy that the heat pump receives over time
W = 1490.0*3600.0 #kJ
Q_out = 120000.0*14.0*24.0 #kJ
Q_in = Q_out - W
print 'Q_in = %.2e MJ' % Q_in

#(b)  the heat pumps coefficient of performance.
cop = Q_out/(Q_out - Q_in)
print 'cop = ', round(cop,2)

#(c)  the coefficient of performance of a reversible heat pump 
cop_max = T_H/(T_H - T_C)
print 'cop_max = ', cop_max

