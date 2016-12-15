##Author: Dan Steingart 
##Date Started: 2016-12-01
##Notes: Clapeyron Equation Example

from pithy import *


#Make a P_T Diagram
Ts = linspace(290,900,1000)
Psat = stater('T',Ts,'Q',0,'water')['P']
Pcrit = pr("Pcrit",'water')
Tcrit = pr("Tcrit","water")
plot(Ts,Psat,'k')
plot(Tcrit,Pcrit,'ro')

#Label Regions of Liquid/Vapor/Critical
fill_between(Ts,Psat,Pcrit,color='b',alpha=.2,linewidth=1)
fill_between(Ts,Psat,0    ,color='g',alpha=.2,linewidth=1)
fill_between([300,Tcrit],3e7,Pcrit ,color='r',alpha=.2,linewidth=0)
fill_between([Tcrit,800],3e7,0,color='r',alpha=.2,linewidth=0)

annotate("Liquid",xy=(350,1e7))
annotate("Vapor",xy=(575,.5e7))
annotate("Critical",xy=(700,2.5e7))

ylabel("Pressure (Pa)")
xlabel("Temperature (K)")
xlim(300,800)
ylim(min(Psat),3e7)
showme()
clf()

#Now Test the Clapeyron Relationship

##Calcualate dP/dT
dP = diff(Psat)
dT = diff(Ts)
dPdT = dP/dT

#Pick a Test Temperature and Find spot in index

T_test = 600 #K

#Find the closest match to T_test
ind = abs((Ts-T_test)).argmin()
T_test = Ts[ind]
dPdT_T_test = dPdT[ind-1]

#Grab vf and vg from table
vf_T_test = stater('T',T_test,'Q',0,'water')['V']
vg_T_test = stater('T',T_test,'Q',1,'water')['V']

#apply the clapyron equation
dH_T_test = dPdT_T_test * T_test*(vg_T_test-vf_T_test)

print "The Clausius Clapyron Assumption says dH_vap = %.2f kJ/kg at T = %2.f K" % (dH_T_test/1000,T_test)

#pull hf and hg from the table
hf_T_test = stater('T',T_test,'Q',0,'water')['H']
hg_T_test = stater('T',T_test,'Q',1,'water')['H']

dH_T_real = hg_T_test-hf_T_test


print "The Tables say dH_vap = %.2f kJ/kg at T = %2.f K" % (dH_T_real/1000,T_test)



error = abs((dH_T_real-dH_T_test)/dH_T_real)*100

print "The error between the two is %.2f %%" % error