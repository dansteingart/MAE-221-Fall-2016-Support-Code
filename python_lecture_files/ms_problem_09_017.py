##Author: Cody Nunno
##Date Started: 2016-12-01
##Notes: Problem 9.17

from pithy import *

m = 4.24e-3*0.453592 #kg
cv = 0.171*4186.8 #J/kgK
k = 1.4
cp = cv*k
R = cp - cv

p1 = 14.7*6894.75729 #Pa
T1 = 540*5.0/9.0 #K
T2 = 1600*5.0/9.0 #K

# State 1
v1 = R*T1/p1
u1 = cv*T1
h1 = cp*T1

# State 2
v2 = v1
p2 = R*T2/v2
u2 = cv*T2
h2 = cp*T2

# State 3
p3 = p1
v3 = (p2*v2**k/p3)**(1/k)
T3 = p3*v3/R
h3 = cp*T3
u3 = cv*T3

out = "state,h (kJ/kg),u (kJ/kg),p (Pa),T (K), v(m^3/kg)\n"

for i in range(1,4):
    out += "%i,%.2f,%.2f,%.2e,%.2f,%.2e\n" % (i,eval("h%i"%i)/1000,eval("u%i"%i)/1000,eval("p%i"%i),eval("T%i"%i),eval("v%i"%i))

print csv_to_table(out)


#net work = Qin - Qout
qin = u2-u1
qout = h1-h3
Wnet = m*(qin + qout)
print "Wnet = %.2f J" % Wnet

# efficiency
eta = 1 + (qout/qin)
print "Efficiency is %.2f %%" % (eta*100)