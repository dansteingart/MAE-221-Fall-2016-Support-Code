##Author: Dan Steingart
##Date Started: 2016-10-20
##Notes: MS Example 7.3

from pithy import *

"""The wall of an industrial drying oven is constructed by sandwiching 0.066 m-thick insulation, having a thermal conductivity k = 0.05e-3   (kW/(m K)), between thin metal sheets. At steady state, the inner metal sheet is at T1 = 575 K and the outer sheet is at T2 = 310 K. Temperature varies linearly through the wall. The temperature of the surroundings away from the oven is 293 K. Determine, in kW per m2 of wall surface area, (a) the rate of heat transfer through the wall, (b) the rates of exergy transfer accompanying heat transfer at the inner and outer wall surfaces, and (c) the rate of exergy destruction within the wall. Let T0 = 293 K."""

kappa = 0.05e-3 # kW/(m K)
L = 0.066 #m

T1 = 575. #K
T2 = 310. #K
T0 = 293. #K

#Calculate Heat Transfer Through Wall
QbyA = -kappa*(T2-T1)/L
print "a) The heat transfer through the oven is %.2f kW/m^2" % QbyA

#Calculate the Exergy Transfer
Eq1byA = (1-T0/T1)*QbyA
Eq2byA = (1-T0/T2)*QbyA
print "b) The Exergy transfer associated with the heat transfer is %.2f kW/m^2 at the inner surface and %.2f (kW/m^2) at the outer surface" % (Eq1byA,Eq2byA)

#Calculate Exergy Destruction

EdbyA = Eq1byA-Eq2byA
print "c) The Exergy destruction between the inner surface and the outer surface is %.2f (kW/m^2)" % (EdbyA)
