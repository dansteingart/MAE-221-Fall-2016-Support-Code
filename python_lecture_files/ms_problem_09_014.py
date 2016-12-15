##Author: Cody Nunno
##Date Started: 2016-12-01
##Notes: 9.14

from pithy import *

bore = 3.7*0.0254 #m
stroke = 3.4*0.0254 #m
V1 = 3.14159265359*(bore/2)**2*stroke/0.84
V2 = 0.16*V1

p1 = 14.5*6894.75729 #Pa
T1 = (60.0+459.67)*5.0/9.0 #K
T3 = 5200.0*5.0/9.0 #K

#Use cold air standard
R = 8.314/28.9 #kJ/kgK
cv = 0.717
cp = cv+R
k = cp/cv

# State 1
v1 = R*1e3*T1/p1 #m^3/kg
u1 = cv*T1 #kJ/kg

# State 2
v2 = V2/V1*v1 #m^3/kg
p2 = p1*v1**k/(v2**k) #Pa
T2 = p2*v2/(R*1e3) #K
u2 = cv*T2 #kJ/kg

# State 3
v3 = v2 #m^3/kg
p3 = R*1e3*T3/v3 #Pa
u3 = cv*T3 #kJ/kg

# State 4
v4 = v1 #m^3/kg
p4 = p3*v3**k/(v4**k) #Pa
T4 = p4*v4/(R*1e3) #K
u4 = cv*T4 #kJ/kg

out = "state,u (kJ/kg),p (Pa),T (K), v(m^3/kg)\n"

for i in range(1,5):
    out += "%i,%.2f,%.2e,%.2f,%.2e\n" % (i,eval("u%i"%i),eval("p%i"%i),eval("T%i"%i),eval("v%i"%i))

print csv_to_table(out)


# Work and heat in
win = u1-u2
wout = u3-u4
qin = u3-u2

wnet = win + wout
m = V1/v1
Wnet = wnet*m*4 #all 4 cylinders
print "Wnet = %.2f kJ" % Wnet

rpm = 2400.
cycps = rpm/60/2
power = Wnet*cycps
print "power = %.2f kW " % (power) 