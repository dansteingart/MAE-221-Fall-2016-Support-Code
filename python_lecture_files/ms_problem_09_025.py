##Author: Cody Nunno
##Date Started: 2016-12-01
##Notes: Problem 9.25

from pithy import *

k = 1.4 
cp = 1.005 #kJ/kgK
cv = .717 #kJ/kgK
R = cp-cv

# State 1
T1 = 340.0 #K
p1 = 100e3 #Pa
v1 = 0.9758 #m^3/kg
u1 = cv*T1 #kJ/kg

# State 2
T2 = 1030.7 #K
p2 = 4850.3e3 #Pa
v2 = 0.06098 #m^3/kg
u2 = cv*T2 #kJ/kg
h2 = cp*T2 #kJ/kg

# State 3
T3 = 2061.4 #K
p3 = p2 #Pa
v3 = 0.1220 #m^3/kg
u3 = cv*T3 #kJ/kg
h3 = cp*T3 #kJ/kg

# State 4
T4 = 897.3 #K
p4 = 263.9e3 #Pa
v4 = v1 #m^3/kg
u4 = cv*T4 #kJ/kg

out = "state,u (kJ/kg),p (Pa),T (K), v(m^3/kg)\n"

for i in range(1,5):
    out += "%i,%.2f,%.2e,%.2f,%.2e\n" % (i,eval("u%i"%i),eval("p%i"%i),eval("T%i"%i),eval("v%i"%i))

print csv_to_table(out)



# Dead State
T0 = 300.0 #K
p0 = 100.0e3 #Pa
v0 = R*T0/p0 #m^3/kg
u0 = cv*T0 #kJ/kg

# Part A
w12 = u1-u2 #kJ/kg
q12 = 0 #kJ/kg
w23 = p2*(v3-v2)/1e3 #kJ/kg
q23 = h3-h2 #kJ/kg
w34 = u3-u4 #kJ/kg
q34 = 0 #kJ/kg
w41 = 0 #kJ/kg
q41 = u1-u4 #kJ/kg
print "Part A"
print "q12 =",q12,"kJ/kg"
print "w12 =",w12,"kJ/kg"
print "q23 =",q23,"kJ/kg"
print "w23 =",w23,"kJ/kg"
print "q34 =",q34,"kJ/kg"
print "w34 =",w34,"kJ/kg"
print "q41 =",q41,"kJ/kg"
print "w41 =",w41,"kJ/kg"

# Part B
e1 = (u1-u0)*1e3 + p0*(v1-v0) - T0*(cp*log(T1/T0)-R*log(p1/p0)) #J/kg
e2 = (u2-u0)*1e3 + p0*(v2-v0) - T0*(cp*log(T2/T0)-R*log(p2/p0)) #J/kg
e3 = (u3-u0)*1e3 + p0*(v3-v0) - T0*(cp*log(T3/T0)-R*log(p3/p0)) #J/kg
e4 = (u4-u0)*1e3 + p0*(v4-v0) - T0*(cp*log(T4/T0)-R*log(p4/p0)) #J/kg

eq12 = (1 -T0/T2)*q12*1e3 - (1 -T0/T1)*q12*1e3
eq23 = (1 -T0/T3)*q23*1e3 - (1 -T0/T2)*q23*1e3
eq34 = (1 -T0/T4)*q34*1e3 - (1 -T0/T3)*q34*1e3
eq41 = (1 -T0/T1)*-q41*1e3 - (1 -T0/T4)*-q41*1e3

ew12 = w12*1e3 - p0*(v2-v1)
ew23 = w23*1e3 - p0*(v3-v2)
ew34 = w34*1e3 - p0*(v4-v3)
ew41 = w41*1e3 - p0*(v1-v4)

# Part B
e1 = (u1-u0)*1e3 + p0*(v1-v0) - T0*(cp*log(T1/T0)-R*log(p1/p0)) #J/kg
e2 = (u2-u0)*1e3 + p0*(v2-v0) - T0*(cp*log(T2/T0)-R*log(p2/p0)) #J/kg
e3 = (u3-u0)*1e3 + p0*(v3-v0) - T0*(cp*log(T3/T0)-R*log(p3/p0)) #J/kg
e4 = (u4-u0)*1e3 + p0*(v4-v0) - T0*(cp*log(T4/T0)-R*log(p4/p0)) #J/kg

eq12 = (1 -T0/T2)*q12*1e3 - (1 -T0/T1)*q12*1e3
eq23 = (1 -T0/T3)*q23*1e3 - (1 -T0/T2)*q23*1e3
eq34 = (1 -T0/T4)*q34*1e3 - (1 -T0/T3)*q34*1e3
eq41 = (1 -T0/T1)*-q41*1e3 - (1 -T0/T4)*-q41*1e3

ew12 = w12*1e3 - p0*(v2-v1)
ew23 = w23*1e3 - p0*(v3-v2)
ew34 = w34*1e3 - p0*(v4-v3)
ew41 = w41*1e3 - p0*(v1-v4)

print ""
print "Part B"
print "eq12 =",eq12/1e3,"kJ/kg"
print "ew12 =",ew12/1e3,"kJ/kg"
print "eq23 =",eq23/1e3,"kJ/kg"
print "ew23 =",ew23/1e3,"kJ/kg"
print "eq34 =",eq34/1e3,"kJ/kg"
print "ew34 =",ew34/1e3,"kJ/kg"
print "eq41 =",eq41/1e3,"kJ/kg"
print "ew41 =",ew41/1e3,"kJ/kg"