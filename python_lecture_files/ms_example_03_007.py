##Author: Dan Steingart
##Date Started: 2016-09-19
##Notes: MS Example 3.7

from pithy import *

#NB: the 'stater' function has one odd thing to it: all inputs, even if mass normalized, are presented by CAPITAL letters

#e.g. pressure = P, quality = Q, Temperature = T, specific volume =V, etc.

#make a pretty print helper function
#We give it the variable and the unit and it makes a nicely printed relationship.  Purely for display.
def pp(val,unit): print "%s = %.1f %s" %(val,eval(val),unit)

#Step 1 Givens

m_water = 2.15       #kg of water equiv
m_metal = 0.50       #kg of water equiv
T_init  = 273 + 25   #K
T_final = 273 + 25.3 #K
V_oil   = 0.1        #mL
c_water = 4.18       #kJ/(kg K)

#Step 2 Determine available energy in oil
#DelU = Q - W = 0 = U_oil - U_water => U_oil = U_water

U_water = (m_water+m_metal)*c_water*(T_final-T_init)

u_bar_oil = U_water/V_oil

pp("u_bar_oil","(kJ/kg L)")

