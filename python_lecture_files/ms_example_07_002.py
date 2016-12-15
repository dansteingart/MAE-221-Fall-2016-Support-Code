##Author: Dan Steingart
##Date Started: 2016-10-24
##Notes: MS Example 7.2

from pithy import *

"""Water initially a saturated liquid at 150C (423.15 K) is contained in a piston-cylinder assembly. The water is heated to the corresponding saturated vapor state in an internally reversible process at constant temperature and pressure. For T0 = 20C (293.15 K), p0 = 1 bar, and ignoring the effects of motion and gravity, determine per unit of mass, each in kJ/kg, (a) the change in exergy, (b) the exergy transfer accompanying heat transfer, (c) the exergy transfer accompanying work, and (d) the exergy destruction."""

T1 = 423.15 #K
x1 = 0
T2 = T1
x2 = 1


T0 = 293.15 #K
p0 = 1e5    #Pa

St = {}

St[1] = stater('T',T1,'Q',x1,'water')
St[2] = stater('T',T2,'Q',x2,'water')
St[0] = stater('T',T0,'p',p0,'water')

ex12 = (St[2]['U'] - St[1]['U']) + \
        p0*(St[2]['V'] - St[1]['V']) - \
        T0*(St[2]['S'] - St[1]['S'])
        
    
print "a) the exergy change is %.2f kJ/kg" % (ex12/1000)

#Now calculate the fraction of exergy related to heat

#Qm = u + W/m

Qbym = (St[2]['U'] - St[1]['U']) + \
        St[1]['P']*(St[2]['V'] - St[1]['V'])

Eqbym = (1- T0/T1)*Qbym

print "b) the exergy transfer accompanying heat transfer is %.2f kJ/kg" % (Eqbym/1000)


#Now calculate the fraction of exergy related to work

Wbym = St[1]['P']*(St[2]['V'] - St[1]['V'])
Ewbym = Wbym - p0*(St[2]['V'] - St[1]['V'])

print "c) the exergy transfer accompanying work is %.2f kJ/kg" % (Ewbym/1000)

#Now calculate the exergy destruction

e_d = -ex12 +Eqbym - Ewbym

print "c) the exergy destruction is %.2f kJ/kg" % (e_d/1000)


