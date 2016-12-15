##Author: Wenkai Liang 
##Date Started: 10/10/2016
##Notes: 

from pithy import *

T_H = 300.0 # K
T_C = 250.0 # K

beta_max = T_C/(T_H - T_C)
print " Maximum beta is ", beta_max

# since beta=Q_C/W_cycle
N_max = int(beta_max)
print 'the maximum N is ', N_max

