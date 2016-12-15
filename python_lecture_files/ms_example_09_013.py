##Author: Dan Steingart
##Date Started: 2016-11-15
##Notes: Modification of Problem 9.13

from pithy import *

"""Air enters a turbojet engine at 80 kPa, 266 K, and an inlet velocity of 277 m/s . The pressure ratio across the compressor is 8. The turbine inlet temperature is 1500 K and the pressure at the nozzle exit is 100 kPa, The work developed by the turbine equals the compressor work input. The diffuser, compressor, turbine, and nozzle processes are isentropic, and there is no pressure drop for flow through the combustor. For operation at steady state, determine the velocity at the nozzle exit and the pressure at each principal state. Neglect kinetic energy except at the inlet and exit of the engine, and neglect potential energy throughout."""

#Ideal Gas 
R = 8.31415/28.97
cv = 0.717
cp = cv+R
k = cp/cv

#Solve for States

#State 1 Before Diffuser
p1 = .8e5 #Pa
T1 = 266 #K
Vel1 = 277 #m/s

#State 2 After Diffuser Before Compressor
Vel2 = 0 #Crazy assumption that KE = 0 in system
#Delta h = delta Vel^2/2 = cp*(T2-T1)
T2 = (((Vel1**2/2)/cp)/1e3)+T1
#Istentropic assumption on diffuser
# s2 - s1 = 0 = cp*ln(T2/T1) - R ln(p2/p1)
p2 = p1*exp((cp/R)*log(T2/T1))

#State 3 After Compressor Before Combuster
p3 = 8*p2 #given
#Istentropic assumption on diffuser
# s2 - s1 = 0 = cp*ln(T2/T1) - R ln(p2/p1)
T3 = T2*exp((R/cp)*log(p3/p2))
Wdotcompbym = cp*(T2 - T3)

#State 4 After Combuster Before Turbine 
T4 = 1500 #K
p4 = p3 

#State 5 After Turbine Before Nozzle
p5 = p2
#assume all work from the turbine goes to compressor
Wdotturbbym = -Wdotcompbym
T5 = T4-(Wdotturbbym/cp)

#State 6 After the Nozzle
p6 = p1
#Istentropic assumption on diffuser
T6 = T5*exp((R/cp)*log(p6/p5))
#And now calculate the velocity of air coming through
Vel6 = sqrt(2*cp*(T5-T6)*1000)
print Vel6 #m/s