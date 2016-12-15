##Author: Dan Steingart
##Date Started: 2016-10-10
##Notes: MS Example 6.4

from pithy import *

Q = -1.2 #kW
Tb = 300 #k

sdot = 0

#S_process_dot = S_rev + S_gen
#S_process_dot = Q/Tb + S_gen
#S_process_dot = 0 #steady state

#At the gearbox boundary:
S_gen = -Q/Tb

print "The entropy generated at the gearbox boundary is %.1f W/K" % (S_gen*1000)


#At the system boundary:
Tb = 293
S_gen = -Q/Tb
print "The entropy generated at the system boundary is %.1f W/K" % (S_gen*1000)