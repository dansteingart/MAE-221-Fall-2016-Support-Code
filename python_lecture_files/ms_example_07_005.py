##Author: Dan Steingart
##Date Started: 2016-10-20
##Notes: MS Example 7.5

from pithy import *

"""Superheated water vapor enters a valve at 500 lbf/in^2, 500 F and exits at a pressure of 80 lbf/in^2. The expansion is a throttling process. Determine the exergy destruction per unit of mass flowing, in Btu/lb. Let T0 = 77F, p0 = 1 atm."""



def pp(val,unit): print "%s = %.3f %s" %(val,eval(val),unit)


#Step 1, What we know, in sensible units
p1 = 3.447e+6 #Pa
T1 = 533 #K

p2 = 551581 #Pa

To = 295 #K
po = 1.014e5 # Pa

#Step 2, define states

st = {}
st[1] = stater('T',T1,'P',p1,'water')

st[2] = stater('H',st[1]['H'],'P',p2,'water')

st[0] = stater('T',To,'P',po,'water')

print state_table(st)

#Now calcaute the Exergy Destruction

#0 = Heat rate (0) + Work (0) + change in exergy - Energy Destroyed

#All exergy is destroyed, so

E_dotbym_dot = -To*(st[1]['S']-st[2]['S'])/1000
pp('E_dotbym_dot','kJ/kg')