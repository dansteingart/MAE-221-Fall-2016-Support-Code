##Author: Dan Steingart
##Date Started: 2016-12-09
##Notes: MS Example 13.8

from pithy import *

#From Table A-25
hf0_H2O = -241820
hf0_CO2 = -393520
hf0_C8H18 = -249910

#Moles of Products that give energy
n_CO2 = 8
n_H2O = 9

#Calculate Total Available Enthalpy per mol octane
Delta_H_total = hf0_C8H18 - n_CO2*hf0_CO2 - n_H2O*hf0_H2O

print 
print "The total available enthlapy is %.1f kJ/kmol Octane" % Delta_H_total

#Moles of Products
n_CO2 = 8
n_H2O = 9
n_N2 = 47
n_O2 =  0 #perfect mixture

#Assuming we start at 298K
Ti = 298 #K
pi = 1e3 #Pa

#Find molar enthalpies for products at 298 K
h_i_CO2 = pr('Hmolar','T',Ti,'P',pi,'CO2')
h_i_N2  = pr('Hmolar','T',Ti,'P',pi,'N2' )
h_i_H2O = pr('Hmolar','T',Ti,'P',pi,'H2O')
h_i_O2  = pr('Hmolar','T',Ti,'P',pi,'O2')


# Now, run a series of 10K trials to find closest value of T where the total enthalpy change matches that of the energy released from octane

Ts = linspace(Ti,3000,10000)
best = 1e13 #best different is something huge
T_best = Ti #assume initial T_best is 298

for T in Ts: #For Each Guess calculate molar enthalpy
    h_f_CO2 = pr('Hmolar','T',T,'P',pi,'CO2')
    h_f_N2  = pr('Hmolar','T',T,'P',pi,'N2' )
    h_f_H2O = pr('Hmolar','T',T,'P',pi,'H2O')
    h_f_O2  = pr('Hmolar','T',Ti,'P',pi,'O2')

    Delta_H_guess = n_CO2  * (h_f_CO2 - h_i_CO2) + \
                    n_H2O  * (h_f_H2O - h_i_H2O) + \
                    n_N2   * (h_f_N2  - h_i_N2)  + \
                    n_O2   * (h_f_O2  - h_i_O2) 

    #we want this to be 0    
    test = Delta_H_guess-Delta_H_total 

    #if closer to 0 than last attempt, this is the current best
    if abs(test) < best: 
        best = abs(test)
        T_best = T


print "The Adiabatic Flame Temperature for an ideal AF is %.2f K" % T_best


## 400% Air
n_CO2 = 8
n_H2O = 9
n_N2 = 47*4
n_O2 =  3


Ts = linspace(Ti,3000,10000)
best = 1e13 #best different is something huge
T_best = Ti #assume initial T_best is 298

for T in Ts: #For Each Guess calculate molar enthalpy
    h_f_CO2 = pr('Hmolar','T',T,'P',pi,'CO2')
    h_f_N2  = pr('Hmolar','T',T,'P',pi,'N2' )
    h_f_H2O = pr('Hmolar','T',T,'P',pi,'H2O')
    h_f_O2  = pr('Hmolar','T',Ti,'P',pi,'O2')

    Delta_H_guess = n_CO2  * (h_f_CO2 - h_i_CO2) + \
                    n_H2O  * (h_f_H2O - h_i_H2O) + \
                    n_N2   * (h_f_N2  - h_i_N2)  + \
                    n_O2   * (h_f_O2  - h_i_O2) 

    #we want this to be 0    
    test = Delta_H_guess-Delta_H_total 

    #if closer to 0 than last attempt, this is the current best
    if abs(test) < best: 
        best = abs(test)
        T_best = T


print "The Adiabatic Flame Temperature if Air in 400%% excess %.2f K" % T_best
