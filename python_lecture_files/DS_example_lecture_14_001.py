##Author: Dan Steingart
##Date Started: 2016-10-10 
##Notes: Shower!

from pithy import *

#make a pretty print helper function
#We give it the variable and the unit and it makes a nicely printed relationship.  Purely for display.
def pp(val,unit): print "%s = %.2f %s" %(val,eval(val),unit)

#Let's model a shower where the input temperature of the hot side is 60 C and the ground water is 15 C
#cp_water = 4.18 #J(kg/kg)

st = {}
#Hot Handle
T1 = 60.+273 #K
P1 = 1e5    #Bar
st[1] = stater('P',P1,'T',T1,'water')

#Cold Handle
T2 = 15.+273 #K
P2 = P1    #Bar
st[2] = stater('P',P2,'T',T2,'water')

#Output Target
T3 = 30. +273 #K
P3 = P1
st[3] = stater('P',P3,'T',T3,'water')

#Average shower mass flow rate
#http://www.home-water-works.org/indoor-use/showers
v3dot = (7.1) * 1.667e-5  #m^3 /s

#Find mass flow rate
rho_water =  st[1]['D']
m3dot = rho_water*v3dot 
print "The target is a temperature of %.2f K at a mass flow rate of %.2f kg/s" % (T3,m3dot) 

#now, work balance

#0 = Qcvdot - Wcvdot + sum_i (mdot_i * (hi+(Vi^2/2))+g*zi) - sum_e (mdot_e * (he+(Ve^2/2))+g*ze)


#mdot3 * h3 = mdot1*h1 + mdot2*h2
#mdot3 * cp*T3 = mdot1*cp*T1 + mdot2*cp*T2

#We know from a mass balance that
#mdot3 = mdot1 + mdot2
#1 = mdot1/mdot3 + mdot2/mdot3 
#let's call mdot1/mdot3 = X and mdot2/mdot3 (1-X)

#We now need to find the ratio of mdot1 to mdot2 and then solve for absolute values knowing the target mass flow rate

#(cp*T3) = mdot1*cp*T1/mdot3 + mdot2*cp*T2/mdot3
#cp drops out, and substitute as above
#T3 = X*T1+(1-X)*T2

print "Solving using incompresible assumption"
X = (st[2]['T']-st[3]['T'])/(st[2]['T']-st[1]['T'])
m1dot = X*m3dot
m2dot = m3dot-m1dot
pp('m1dot','kg/s')
pp('m2dot','kg/s')
print
#we can also use h
print "Solving using CoolProp"
X = (st[2]['H']-st[3]['H'])/(st[2]['H']-st[1]['H'])
m1dot = X*m3dot
m2dot = m3dot-m1dot
pp('m1dot','kg/s')
pp('m2dot','kg/s')

