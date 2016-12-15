##Author: Dan Steingart
##Date Started: 2016-09-19
##Notes: A simple quality calculation and phase diagram examples

from pithy import *

#NB: the 'stater' function has one odd thing to it: all inputs, even if mass normalized, are presented by CAPITAL letters

#e.g. pressure = P, quality = Q, Temperature = T, specific volume =V, etc.

#Step 1: Digest the Givens
p = 1e5 #Pa, 1 bar
T = 373 #K 99.7 K
V = 0.1 #m^3
m = 0.5 #kg


#Step 2: Determine quality
#First determine specific volume of system
v = V/m #m^3/kg

#From the Steam tables in book (A-3)
vf = 1.0432e-3 # m^3/kg
vg = 1.694  #m^3/kg

#Determine quality
x_A3 = (v-vf)/(vg-vf) 

print "From table A3 the quality is %.3f" % x_A3

#Let's check against the pithy (coolprops) steam tables
state = stater('T',T,'D',1/v,'water')
x_coolprops = state['Q']
print "From coolprops the quality is %.3f" % x_coolprops

st = {1:state}
print
print "The full state via coolprops"
print state_table(st)

#Let's examine the physical meaning of "quality" by making phase diagrams at different conditions

pv_phase_envelope('water',fill=True)
for T1 in [300,350,373,500]:
    vs = logspace(-3,2,300)
    st = stater('T',T1,'V',vs,'water')
    ps = st['P']
    plot(vs,ps,label='%.1f K' % T1)

title("Various Isotherms and the pV Phase Envelope for Water")
loglog()
legend()
xlim(1e-4,1e3)
ylim(1e3,1e8)
ylabel('Pressure (Pa)')
xlabel('Volume (m^3)')
showme()
clf()



tv_phase_envelope('water',fill=True)
for P1 in [1e5,1e6,1e7]:
    vs = logspace(-3,2,300)
    st = stater('P',P1,'V',vs,'water')
    Ts = st['T']
    plot(vs,Ts,label='%.0f kPa' % (P1/1000))

title("Various Isobars and the TV Phase Envelope for Water")
semilogx()
legend()
xlim(1e-4,1e3)
ylim(280,800)
ylabel('Temperature (K)')
xlabel('Volume (m^3)')
showme()
clf()

