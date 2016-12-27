##Author: Cody Nunno
##Date Started: 2016-12-14
##Notes: MS Problem 11.33

from pithy import *

# Generate temperature space
Ts = linspace(290.0,1000.0,711)
Psat = stater('T',Ts,'Q',0,'water')['P']

# Calcualate dP/dT
dP = diff(Psat)
dT = diff(Ts)
dPdT = dP/dT

T_use = 50.0+273.0 #K

#Find the closest match to T_use
ind = abs((Ts-T_use)).argmin()
T_use = Ts[ind]
dPdT_T_use = dPdT[ind-1]

#Grab vf and vg from table
vf_T_use = stater('T',T_use,'Q',0,'water')['V']
vg_T_use = stater('T',T_use,'Q',1,'water')['V']

#Apply the Clapeyron equation
dH_T_use = dPdT_T_use * T_use*(vg_T_use-vf_T_use)
dU_T_use = dH_T_use - Psat[ind]*(vg_T_use-vf_T_use)
dS_T_use = dPdT_T_use * (vg_T_use-vf_T_use)

#Pull real f and g states from the table
hf_T_real = stater('T',T_use,'Q',0,'water')['H']
hg_T_real = stater('T',T_use,'Q',1,'water')['H']
dH_T_real = hg_T_real-hf_T_real

uf_T_real = stater('T',T_use,'Q',0,'water')['U']
ug_T_real = stater('T',T_use,'Q',1,'water')['U']
dU_T_real = ug_T_real-uf_T_real

sf_T_real = stater('T',T_use,'Q',0,'water')['S']
sg_T_real = stater('T',T_use,'Q',1,'water')['S']
dS_T_real = sg_T_real-sf_T_real

# Find errors as percentages
error_h = abs((dH_T_real-dH_T_use)/dH_T_real)*100
error_u = abs((dU_T_real-dU_T_use)/dU_T_real)*100
error_s = abs((dS_T_real-dS_T_use)/dS_T_real)*100

print "a) dh_use = %.2f MJ/kg vs dh_real = %.2f MJ/kg" % (dH_T_use/1e6,dH_T_real/1e6)
print " Percentage difference is: %.1f" % error_h, "%"
print "b) du_use = %.2f MJ/kg vs du_real = %.2f MJ/kg" % (dU_T_use/1e6,dU_T_real/1e6)
print " Percentage difference is: %.1f" % error_u, "%"
print "c) ds_use = %.2f kJ/kg vs ds_real = %.2f kJ/kg" % (dS_T_use/1e3,dS_T_real/1e3)
print " Percentage difference is: %.1f" % error_s, "%"