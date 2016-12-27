##Author: Dan Steingart
##Date Started: 2016-12-12
##Notes: Solution to Midterm 3, based on example 13.8

from chempy import balance_stoichiometry
from pithy import *

#From Table A-25
hf = {} #all in kJ/kmol
hf['H2O']    = -241820
hf['CO2']    = -393520
hf['CH4']    = -274850
hf['C8H18']  = -249910
hf['C2H6']   = -84680
hf['C2H4']   =  52280  
hf['CH3OH']  = -238810 #methanol
hf['C2H5OH'] = -277690 #ethanol
hf['H2']  = 0
hf['N2']  = 0
hf['O2']  = 0

fuel = 'CH4'

#Octane Combustion
reac, prod = balance_stoichiometry({fuel, 'O2'}, {'H2O','CO2'})
reac['N2'] = 3.76*reac['O2']
prod['N2'] = reac['N2']
n_fuel = reac[fuel]
for k in prod.keys(): prod[k] = prod[k]/n_fuel
for k in reac.keys(): reac[k] = reac[k]/n_fuel

out = ""
print
print "The balanced reaction is"
for i in reac.keys(): out += " %.1f %s +" % (reac[i],i)
out = out[:-1]
out += " = "
for i in prod.keys(): out += " %.1f %s +" % (prod[i],i)
out = out[:-1]
print out

#Calculate Total Available Enthalpy per mol octane
print
dH_rxn = 0
dH_form = "dh_rxn = "
dH_runner = "dh_rxn = "
for k in reac.keys(): 
    dH_rxn += reac[k]*hf[k]
    dH_form += "dh_%s + "  % (k)
    dH_runner += "(%.2f) + " % (reac[k]*hf[k])
dH_form = dH_form[0:-2]
dH_runner = dH_runner[0:-2]
for k in prod.keys(): 
    dH_rxn += -prod[k]*hf[k]
    dH_form += " - dh_%s" % (k)
    dH_runner += " - (%.2f)" % (prod[k]*hf[k])

print dH_form
print dH_runner
print "The reaction energy is %.2f kJ/kmol of %s" % (dH_rxn,fuel)

#Find molar enthalpies for products at 298 K
Ti =298 #K
pi = 1e3 #Pa 

h_init = {}
for k in prod.keys(): h_init[k] = pr('Hmolar','T',Ti,'P',pi,k)

# Now, run a series of 10K trials to find closest value of T where the total enthalpy change matches that of the energy released from octane

Ts = linspace(Ti,6000,20000)
best = 1e13 #best difference is something huge
T_best = Ti #assume initial T_best is 298

for T in Ts: #For Each Guess calculate molar enthalpy
    h_fin = {}
    for k in prod.keys(): 
        h_fin[k] = pr('Hmolar','T',T,'P',pi,k)

    dH_guess = 0
    for k in prod.keys():
        dH_guess += prod[k]*(h_fin[k]-h_init[k])

    #we want this to be 0    
    test = dH_guess-dH_rxn 

    #if closer to 0 than last attempt, this is the current best
    if abs(test) < best: 
        best = abs(test)
        T_best = T


print "The Adiabatic Flame Temperature for an ideal AF is %.2f K for %s" % (T_best,fuel)


#Now, using the adiabatic flame temperature calculated, find the fraction of the enthalpy allocated to heating the N2

h_N2 = (pr('Hmolar','T',T_best,'P',pi,'N2')-pr('Hmolar','T',Ti,'P',pi,'N2'))*reac['N2']

#Since the first law says that we can't produce more energy by demixing and then burning, the above calculation must be the minimum enthalpy required to de-mix the N2.

print "The minimum enthalpy required to de-mix the air is %.2f kJ/kmol per mol of %s" % (h_N2,fuel)



print "The (dh_N2/dh_rxn) is %.2f %%" % ((h_N2/dH_rxn)*100)
##Author: 
##Date Started: 
##Notes: 
