##Author: Dan Steingart
##Date Started: 2016-09-19
##Notes: MS Example 3.2

from pithy import *
#make a pretty print helper function
#We give it the variable and the unit and it makes a nicely printed relationship.  Purely for display.
def pp(val,unit): print "%s = %.1f %s" %(val,eval(val),unit)

#Step 1: Digest the Givens
p1 = 1e5 #Pa
x1 = 0.5
p2 = 1.5e5 #Pa
V = 0.5 # m**3

#Step 2: Find the states
states = {}
states[1] = stater('P',p1,'Q',x1,'water')

#Now, since the state is defined, and we know the volume of the container, let's determine the mass

mass = V/states[1]['V']

states[2] = stater('P',p2,'V',states[1]['V'],'water')
states[3] = stater('Q',1,'V',states[1]['V'],'water')

print state_table(states)


#Show on phase envelope
ps=[p1,p2,states[3]['P']]
Vs = [states[1]['V'],states[2]['V'],states[3]['V']]
pv_phase_envelope('water')
loglog()
plot(Vs,ps,'r')
xlabel("Volume (m^3)")
ylabel("Presure (Pa)")
showme()

