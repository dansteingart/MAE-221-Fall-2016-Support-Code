##Author: Dan Steingart
##Date Started: 2016-09-19
##Notes: MS Example 3.1

from pithy import *
#make a pretty print helper function
#We give it the variable and the unit and it makes a nicely printed relationship.  Purely for display.
def pp(val,unit): print "%s = %.1f %s" %(val,eval(val),unit)

#Step 1: Digest the Givens
T1 = 246.6 #K 16.63 F
T2 = 298.15 #K 77 F
p1 = 1.38e5 #bar
p2 = p1
mass = 0.0453592 #kg
#Step 2: Find the states

states = {}
states[1] = stater('T',T1,'P',p1,'ammonia')
states[2] = stater('T',T2,'P',p1,'ammonia')
print state_table(states)

#Now find the work
V1 = mass*states[1]['V']
V2 = mass*states[2]['V']

W = p1*(V2-V1)
pp('W','J')

#Now let's go a step further and find the heat input required to get this done

#Q - W = U12

U12 = mass*(states[2]['U']-states[1]['U'])
pp('U12','J')
Q = U12+W
pp('Q','J')


#Show on phase envelope
ps=[p1,p2]
Vs = [states[1]['V'],states[2]['V']]
pv_phase_envelope('ammonia',fill=True)
loglog()
plot(Vs,ps,'r')
xlabel("Volume (m^3)")
ylabel("Presure (Pa)")
showme()