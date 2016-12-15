##Author: 
##Date Started: 
##Notes: 
from pithy import *

#make a pretty print helper function
#We give it the variable and the unit and it makes a nicely printed relationship.  Purely for display.
def pp(val,unit): print "%s = %.1f %s" %(val,eval(val),unit)

#In this problem, the same scenario is drawn, but with two different system boundaries.

#Adding to the mess we have english units.  let's convert off that bat

p_atm = 1e5 #Pa (14.7 psi)
m_piston = 45.36 #kg (100 lbs)
A_piston = 0.092903 #m^2 (1ft^2)
m_air = 0.27 #kg (.6 lb)
DelV_12 =  0.045 #m^3 ((1.6 ft3)
Delu_12 = 41868 #J/kg (18 btu/lb)
g = 9.81 #m/s^2
#In part A, we just take air as the system.  Excluding the piston.

print "Part A) Since the piston is _not_ in the system, we are not moving anything othe than the air."

DelKE = 0 #no mass moving other than air
DelPE = 0 #no mass moving other than air

# DelU_12 = Q-W

# Since we know the mass of air, and Delu_12,

DelU_12 = m_air*Delu_12 # in J
pp('DelU_12','J')

# To calculate work, we need the total pressure.  

# p = p_atm + p_piston

p_piston = m_piston*g/A_piston

p = p_atm + p_piston

W_12 = p*DelV_12
pp('W_12','J')

Q_12 = W_12 + DelU_12
pp('Q_12','J')

print 
print "Part B) Now the piston is in the system.  We have to account for a change in potential energy"

DelKE = 0  # ->No velocity at either state 
DelPE = DelV_12 / A_piston *m_piston * g
pp('DelPE','J')
p = p_atm

DelU_12 = m_air*Delu_12 # in J
pp('DelU_12','J')

W_12 = p*DelV_12
pp('W_12','J')

Q_12 = W_12 + DelU_12 + DelPE
pp('Q_12','J')

print

print """Note that either way, the heat required to complete the operation is the same.  This is as is should be: the system selection should change the manner in which you analyze the energy transfers, but it should not change the overall result.

Now, what are the advantages and disadvantages of both approaches.  For the rest of the course we will use the former approach.  Can you think of a few reasons why this is more useful?"""