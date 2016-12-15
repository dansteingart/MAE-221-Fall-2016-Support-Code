##Author: Dan Steingart 
##Date Started: 2016-11-14
##Notes: MS Example 9.11

"""A regenerative gas turbine with intercooling and reheat operates at steady state. Air enters the compressor at 100 kPa, 300 K with a mass flow rate of 5.807 kg/s. The pressure ratio across the two-stage compressor is 10. The pressure ratio across the two-stage turbine is also 10. The intercooler and reheater each operate at 300 kPa. At the inlets to the turbine stages, the temperature is 1400 K. The temperature at the inlet to the second compressor stage is 300 K. The isentropic efficiency of each compressor and turbine stage is 80%. The regenerator effectiveness is 80%. Determine (a) the thermal efficiency, (b) the back work ratio, (c) the net power developed, in kW, (d) the total rate energy is added by heat transfer, in kW."""

from pithy import *

R = 8.3144/28.97  #J/(kg(K))
cv = 0.717 ##J/(kg(K))
cp = cv+R
k = cp/cv

vdot = 5 # m^3/s
eta_s = .8 #isentropic effieciency of the turbine/compressor

#State 1 from givens
p1 = 1e5 #Pa
T1 = 300 #K
#Use pv = RT to find v1
v1 = R*T1/p1

#now find mdot
mdot = vdot/v1 

#State 2: 
p2 = 3*p1
T2s = T1*exp((R/cp)*log(p2/p1))
T2 = T1+(T2s-T1)/eta_s
v2 = R*T2/p2

#State 3:
T3 = T1
p3 = p2
v3 = R*T3/p3

#State 4:
p4 = 10*p1
T4s = T3*exp((R/cp)*log(p4/p3))
T4 = T3+(T4s-T3)/eta_s
v4 = R*T4/p4

#State 6:
p6 = p4
T6 = 1400 #K
v6 = R*T6/p6

#State 7
p7 = 3*p1
T7s = T6*exp((R/cp)*log(p7/p6))
T7 = T6 - (T6-T7s)*eta_s
v7 = R*T7/p7

#State 8
p8 = p7
T8 = 1400 #K
v8 = R*T8/p8

#State 9
p9  = p1
T9s = T8*exp((R/cp)*log(p9/p8))
T9  = T8 - (T8-T9s)*eta_s
v9 = R*T9/p9

#State 5:
p5 = p4
T5 = eta_s*(T9-T4)+T4
v5 = R*T5/p5

def make_table():
    out = "State,T (K),P (Pa),v(m^3/kg)\n"
    for i in range(1,10):
        out += "%s," % i
        for j in ['T','p','v']:
            get = "%s%i" % (j,i)
            try: out += "%.1e," % eval(get)
            except Exception as E: 
                print
                out += ","
        out = out[:-1]+"\n"

    return csv_to_table(out)
print make_table()

#Determine Work/Heat

W_comp_1 = mdot*cp*(T1-T2)
W_comp_2 = mdot*cp*(T3-T4)
W_turb_1 = mdot*cp*(T6-T7)
W_turb_2 = mdot*cp*(T8-T9)
Q_comb_1 = mdot*cp*(T6-T5)
Q_comb_2 = mdot*cp*(T8-T7)

W_comp_T = W_comp_1 + W_comp_2
W_turb_T = W_turb_1 + W_turb_2
Q_comb_T = Q_comb_1 + Q_comb_2

Q_in = Q_comb_T
W_cycle = W_comp_T + W_turb_T

eta = W_cycle/Q_in
bwr = -W_comp_T/W_turb_T

print "eta = %.2f" % eta
print "bwr = %.2f" % bwr
print "W_cycle = %.2f MW" % (W_cycle/1e6)


