##Author: Dan Steingart
##Date Started: 2016-09-19
##Notes: MS Example 3.3

from pithy import *
#make a pretty print helper function
#We give it the variable and the unit and it makes a nicely printed relationship.  Purely for display.
def pp(val,unit): print "%s = %.1f %s" %(val,eval(val),unit)

#Step 1: Digest the Givens
V = 0.283168 #m^3
T1 = 373.15 # K
x1 = 1
p2 = 1.38e5 #Pa

#Step 2: Find the states
states = {}
states[1] = stater('T',T1,'Q',x1,'water')
v1 = states[1]['V']
p1 = states[1]['P']
v2 = v1
states[2] = stater('P',p2,'V',v1,'water')

#Now, since the state is defined, and we know the volume of the container, let's determine the mass

mass = V/states[1]['V']

print state_table(states)

##Now find work _in_
#Q - W = U12
Q = 0 #J, Well insulated no work it
pp('Q','J')
U12 = mass*(states[2]['U']-states[1]['U'])
pp('U12','J')
W12 = -U12
pp('W12','J')

#Show on phase envelope
ps=[p1,p2]
vs = [states[1]['V'],states[2]['V']]

pv_phase_envelope('water',fill=True)
loglog()
plot(vs,ps,'r')
xlabel("Volume (m^3)")
ylabel("Presure (Pa)")
showme()
