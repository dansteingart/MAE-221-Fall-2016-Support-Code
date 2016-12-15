##Author: Cody Nunno
##Date Started: 2016-10-08
##Notes: 

from pithy import *

A = 15.0*25.0 # m^2
Q_in = 4.0*A # kW-h/day
T_H = 400.0 # K
T_C = 285.0 # K
ppkWh = 0.08 # $/kW-h

eta_max = 1-T_C/T_H
print " Maximum efficiency is ", eta_max

ss = 100
eta = linspace(0,eta_max,ss)
price = eta*ppkWh*365.0*Q_in

plot(eta,price)
xlabel("Efficiency")
ylabel("Value of Generated Electricity ($)")
showme()
clf()

#as we convert the power in a more efficienct manner we capture more value