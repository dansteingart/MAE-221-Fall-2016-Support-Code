##Author: Dan Steingart
##Date Started: 2016-09-19
##Notes: MS Example 3.4

from pithy import *

#NB: the 'stater' function has one odd thing to it: all inputs, even if mass normalized, are presented by CAPITAL letters

#e.g. pressure = P, quality = Q, Temperature = T, specific volume =V, etc.

#make a pretty print helper function
#We give it the variable and the unit and it makes a nicely printed relationship.  Purely for display.
def pp(val,unit): print "%s = %.1f %s" %(val,eval(val),unit)

#Step 1: Digest the Givens
states = {}

p1 = 10e5 #Pa
T1 = 400+273.15 #K  
#state 1 defined!
states[1] = stater('P',p1,'T',T1,'water')

p2 = p1
x2 = 1 #Saturated vaport state
#state 2 defined!
states[2] = stater('P',p2,'Q',x2,'water')

v3 = states[2]['V'] #m^3/kg
T3 = 150+273.15 #K
#state 3 defined!
states[3] = stater('T',T3,'V',v3,'water')


print state_table(states)
#Show on phase envelope
ps = []
vs = []
Ts = []

for i in range(1,4):
    ps.append(states[i]['P'])
    vs.append(states[i]['V'])
    Ts.append(states[i]['T'])

for i in range(1,4): annotate(str(i),xy=(vs[i-1],ps[i-1]))
pv_phase_envelope('water',fill=True)
loglog()
plot(vs,ps,'r')
xlabel("Volume (m^3)")
ylabel("Presure (Pa)")
xlim(1e-1,1e1)
ylim(1e5,1e8)
showme()
clf()

for i in range(1,4): annotate(str(i),xy=(vs[i-1],Ts[i-1]))
tv_phase_envelope('water',fill=True)
semilogx()
plot(vs,Ts,'r')
xlabel("Volume (m^3)")
ylabel("Temperature (K)")
xlim(1e-1,1e1)
ylim(273,900)

showme()


##Now find total work and heat
#q13 - w13 = u13
u13 = states[3]['U']-states[1]['U']
pp('u13','J/kg')
w13 = p1*(states[2]['V']-states[1]['V'])+0
pp('w13','J/kg')
q13 = u12+w13 
pp('q13','J/kg')
