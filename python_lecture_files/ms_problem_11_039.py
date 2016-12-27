##Author: Cody Nunno
##Date Started: 2016-12-15
##Notes: MS Problem 11.39

from pithy import *

m = 80.0 #kg
v_i = 1.0911e-3 #m^3/kg
v_f = 1.0002e-3 #m^3/kg
Del_h = 333.4e3 #J/kg
T2 = -2.0 + 273.0
T1 = 273  
g = 9.8 #m/s^2
F = m*g #N

Del_p = (Del_h)/(v_f-v_i)*log(T2/T1)
print "Psat @ -2 C = %.2f bar" %(Del_p/1e5)

#The pressure exerted on the chair by the atmosphere is

# p = patm + F/A
p_atm = 1e5
# 

A = F/(Del_p - p_atm)

print "The minimum total area is %.3f cm^2" % (A*1e4) 