##Author: Dan Steingart
##Date Started: 2016-10-10
##Notes: MS Example 6.5



from pithy import *

m_metal = 0.8/2.2  # kg
m_water = 20/2.2   # kg

Ti_metal = 1055.55 # K
Ti_water = 294.5 # K

cp_water = 4.18 # kJ/(kg K)
cp_metal = 0.41 # kJ/(kg K)


#Delta U = 0 = Delta U_water + Delta U_metal


#Determine the final tempreature
Tf = (m_water*Ti_water*cp_water+m_metal*cp_metal*Ti_metal)/(m_water*cp_water+m_metal*cp_metal)

print "Tf = %.2fK" % Tf

#Determine the entropy produced

#dS_water + dS_metal = sigma


sigma_water = m_water*cp_water*log(Tf/Ti_water) 

sigma_metal = m_metal*cp_metal*log(Tf/Ti_metal)

sigma =  sigma_water + sigma_metal

print "The entropy produced is %.2f kJ/K" % sigma 

print ""
print "Let's look at all the entropy variables"

whos(locals(),pattern="sigma")

print "note that the entropy of the metal decreases _less_ than the entropy of the water increases"