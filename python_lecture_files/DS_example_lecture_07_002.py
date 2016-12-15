##Author: Dan Steingart
##Date Started: 2016-09-26
##Notes: Let's Get Critical

from pithy import *

#NB: the 'stater' function has one odd thing to it: all inputs, even if mass normalized, are presented by CAPITAL letters

#e.g. pressure = P, quality = Q, Temperature = T, specific volume =V, etc.

#Let's examine the physical meaning of "quality" by making phase diagrams at different conditions

Tc = pr('Tcrit','water')
print Tc

pv_phase_envelope('water',fill=True)
for T1 in [300,373,500,Tc,800]:
    vs = logspace(-3,2,300)
    st = stater('T',T1,'V',vs,'water')
    ps = st['P']
    plot(vs,ps,label='%.1f K' % T1)

title("Various Isotherms and the pV Phase Envelope for Water")
loglog()
legend()
xlim(1e-4,1e3)
ylim(1e3,1e9)
ylabel('Pressure (Pa)')
xlabel('Volume (m^3/kg)')
showme()
clf()



tv_phase_envelope('water',fill=True)

pc = pr('Pcrit','water')
print pc

for P1 in [1e5,1e6,1e7,2.2e7,3e7]:
    vs = logspace(-3,2,300)
    st = stater('P',P1,'V',vs,'water')
    Ts = st['T']
    plot(vs,Ts,label='%.0f kPa' % (P1/1000))

title("Various Isobars and the TV Phase Envelope for Water")
semilogx()
legend()
xlim(1e-4,1e3)
ylim(280,900)
ylabel('Temperature (K)')
xlabel('Volume (m^3/kg)')
showme()
clf()

