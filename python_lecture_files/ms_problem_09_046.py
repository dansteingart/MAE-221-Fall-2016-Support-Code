##Author: Cody Nunno
##Date Started: 2016-12-01
##Notes: MS Problem 9.46

from pithy import *

m_dot = 6.0 #kg/s
k = 1.4
r_c = 10.0
cp = 1.005 #kJ/kgK
cv = cp/k #kJ/kgK
R = cp - cv #kJ/kgK

T1 = 300.0 #K
p1 = 100.0e3 #Pa
T3 = 1400.0 #K

# State 1
v1 = R*1e3*T1/p1 #m^3/kg
h1 = cp*T1 #kJ/kgK

# State 2
p2 = r_c*p1 #Pa
v2 = (p1*v1**k/p2)**(1/k) #m^3/kg
T2 = p2*v2/(1e3*R) #K
h2 = cp*T2 #kJ/kgK

# State 3
p3 = p2 #Pa
v3 = R*1e3*T3/p3 #m^3/kg
h3 = cp*T3 #kJ/kgK

# State 4
p4 = p1 #Pa
v4 = (p3*v3**k/p4)**(1/k) #m^3/kg
T4 = p4*v4/(R*1e3)
h4 = cp*T4 #kJ/kgK


out = "state,h (kJ/kg),p (Pa),T (K), v(m^3/kg)\n"

for i in range(1,4):
    out += "%i,%.2f,%.2e,%.2f,%.2e\n" % (i,eval("h%i"%i),eval("p%i"%i),eval("T%i"%i),eval("v%i"%i))

print csv_to_table(out)

W_dot_12 = m_dot*(h1-h2)
W_dot_34 = m_dot*(h3-h4)
Q_dot_23 = m_dot*(h3-h2)

eta_cycle = (W_dot_12+W_dot_34)/Q_dot_23

print "Part A"
print "Efficiency is %.2f%%"% (eta_cycle*100)
print ""

bwr = (h2-h1)/(h3-h4)

print "Part B"
print "Back work ratio is %.2f " %bwr
print ""

P_net = W_dot_12+W_dot_34

print "Part C"
print "Power is %.2f MW" % (P_net/1e3)