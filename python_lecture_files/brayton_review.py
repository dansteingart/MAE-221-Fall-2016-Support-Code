##Author: Cody Nunno
##Date Started: 2016-12-01
##Notes: 

from pithy import *

# Start with known states
T1 = 300.0 #K
T3 = 1700.0 #K
p1 = 101.3e3 #Pa
r_p = 15.0
m_dot = 200.0 #kg/s
k = 1.4
R = 287 #J/kgK
cp = 1005.0 #J/kgK
#Use cold air standard
#Solve for all state properties

# Round 1: assume a perfect system
print "Part 1"
#State 1: compressor entrance
print "State 1"
v1 = R*T1/p1
print "v1 = ",v1,"m^3/kg"
h1 = cp*T1
print "h1 =",h1/1000.0,"kJ/kg"
print ""

#State 2: heat exchanger/combustor entrance
print "State 2"
p2 = r_p*p1
print 'p2 =',p2/1e6,"MPa"
print "p2v2^k = p1v1^k"
v2s = (p1*v1**k/p2)**(1/k)
print "v2 = ",v2s,"m^3/kg"
T2s = p2*v2s/R
print "T2 =",T2s,"K"
h2s = cp*T2s
print "h2 =",h2s/1000,"kJ/kg"
ds12s = cp*log(T2s/T1) - R*log(p2/p1)
print "ds12 =",ds12s,"J/kgK"
print "Effectively no change in entropy, small change likely due to cold air assumption"
W_dot_cs = m_dot*(h1-h2s)
print "W_dot_c =",W_dot_cs/1e6,"MW"
print ""

"Side note: In class, we breezed past a question regarding why work done by the fluid is not considered in the combustor.  The answer is that the work and heat considered are work done inside of the control volume, which does not include the flow work exchanged with internal energy in the fluid.  This is encompassed through the use of enthalpy, which accounts for this flow work, which does not effect the usable work totals for the compressor/turbine, nor the heat gained through the heat exchanger."
#State 3: pre-compressor
print "State 3"
p3 = p2
print "p3 =",p3/1e6,"MPa"
v3 = R*T3/p3
print "v3 = ",v3,"m^3/kg"
h3 = cp*T3
print "h3 =",h3/1000,"kJ/kg"
ds23 = cp*log(T3/T2s) - R*log(p3/p2)
print "ds23 =",ds23,"J/kgK"
Q_dot_in_s = m_dot *(h3-h2s)
print "Q_dot_in_2 =",Q_dot_in_s/1e6,"MW"
print ""

#State 4: exhaust
print "State 4"
p4 = p1
print "p4 =",p4/1e3,"kPa"
v4s = (p3*v3**k/p4)**(1/k)
print "v4 = ",v4s,"m^3/kg"
T4s = p4*v4s/R
print "T4 =",T4s,"K"
h4s = cp*T4s
print "h4 =",h4s/1000,"kJ/kg"
W_dot_ts = m_dot*(h3-h4s)
print "W_dot_t =",W_dot_ts/1e6,"MW"
print ""
eta_s = (W_dot_ts+W_dot_cs)/Q_dot_in_s
print "Efficiency is ", eta_s*100,"%"
print ""

# Round 2: no such thing as a perfect system
print ""
print "Part 2"
# Need to recalculate States 2 and 4 accounting for entropic losses
eta_t = 0.90
eta_c = 0.85

print "State 4"
h4 = h3 - eta_t*(h3-h4s)
print "h4 =",h4/1000,"kJ/kg"
T4 = h4/cp
print "T4 =",T4,"K"
v4 = R*T4/p4
print "v4 = ",v4,"m^3/kg"
print ""

print "State 2"
h2 = h1 + (h2s-h1)/eta_c
print "h2 =",h2/1000,"kJ/kg"
T2 = h2/cp
print "T2 =",T2,"K"
v2 = R*T2/p2
print "v2 = ",v2,"m^3/kg"
print ""

ds12 = cp*log(T2/T1) - R*log(p2/p1)
print "ds12 =",ds12,"J/kgK"
ds34 = cp*log(T4/T3) - R*log(p4/p3)
print "ds34 =",ds34,"J/kgK"
print ""

W_dot_c = m_dot*(h1-h2)
print "W_dot_c =",W_dot_c/1e6,"MW"
W_dot_t = m_dot*(h3-h4)
print "W_dot_t =",W_dot_t/1e6,"MW"
Q_dot_in = m_dot *(h3-h2)
print "Q_dot_in =",Q_dot_in/1e6,"MW"
eta = (W_dot_t+W_dot_c)/Q_dot_in
print "Efficiency is ", eta*100,"%"

# Round 3: regenerate to regain some lost efficiency
print ""
print "Part 3"
eta_he = 0.75
hx = h2 + eta_he*(h4-h2)
print "hx =",hx/1000,"kJ/kg"
Q_dot_in_reg = m_dot *(h3-hx)
print "Q_dot_in =",Q_dot_in_reg/1e6,"MW"
eta_reg = (W_dot_t+W_dot_c)/Q_dot_in_reg
print "Efficiency is ", eta_reg*100,"%"