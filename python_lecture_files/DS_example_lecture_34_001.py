##Author: Dan Steingart
##Date Started: 2016-12-13
##Notes: DS Example based on MS Example 14.2, but sweeping temperature/  What we see is that 
# 1) At low T, the reaction goes to completio, which makes sense because K is higher
# 2) Increasing pressure favors the forward reaction which makes sense because there are fewer moles of product than reactant.

from pithy import *
import pandas as pd

Rbar = 8.314 #kJ/(kmol K)

h0 = {}
#From A-25, kJ/kmol
h0['CO2'] = -393520 
h0['CO']  = -110530 
h0['O2']  =  0

s0 = {}
#From A-25, kJ/kmol
s0['CO2'] = 213.69
s0['CO']  = 197.54 
s0['O2']  = 205.03

T0 = 298 #K
p1 = 1e5 #bar
p2 = 1e6 #bar

df = pd.DataFrame()
for T in linspace(T0,3000,500):
    hi = {}
    hi['CO2'] = pr('Hmolar','T',T0,'P',p1,'CO2')
    hi['CO']  = pr('Hmolar','T',T0,'P',p1,'CO')
    hi['O2']  = pr('Hmolar','T',T0,'P',p1,'O2')
    
    hf = {}
    hf['CO2'] = pr('Hmolar','T',T ,'P',p1,'CO2')
    hf['CO']  = pr('Hmolar','T',T ,'P',p1,'CO')
    hf['O2']  = pr('Hmolar','T',T ,'P',p1,'O2')
    
    
    dG0 =  h0['CO2']            - h0['CO']            -.5*h0['O2'] \
     +    (hf['CO2']-hi['CO2']) -(hf['CO']-hi['CO']) -.5*(hf['O2']-hi['O2']) \
     -  (T*s0['CO2']        -   T*s0['CO']          -.5*T*s0['O2'])
     
    lnK = -dG0/(T*Rbar)
    K = exp(-lnK)

    for p in [p1,p2]:
        z_test = linspace(0,1,1000)
        Best   = 1000
        z_best = 0
        for z in z_test:
            z1 = z/(1-z)
            z2 =(z/(2+z))**(.5)
            z3 = (p/p1)**(.5)
            test = z1*z2*z3
            if abs(K-test) < Best:
                Best = abs(K-test)
                z_best = z
        
        z = z_best

        y ={}
        y['CO']  =    2*z/(2+z)
        y['O2']  =      z/(2+z)
        y['CO2'] = 2*(1-z)/(2+z)
        out = {}
        out['z'] = z
        out['T'] = T
        out['p'] = p
        out['CO']  = y['CO'] 
        out['O2']  = y['O2'] 
        out['CO2'] = y['CO2']

        dthis = pd.DataFrame(data=out,index=[1])
        df = pd.concat([df,dthis])




cc = ['b','g','r']
keys = y.keys()
for i in range(len(keys)):
    k = keys[i]
    d = df[df['p']==p1]
    c = cc[i]
    plot(d['T'],d[k],c,label="%s %.0e Pa" %(k,p1))
    c = cc[i]+"-."
    d = df[df['p']==p2]
    plot(d['T'],d[k],c,label="%s %.0e Pa" %(k,p2))

title("CO + (1/2) O2 <-> CO2 ")
ylim(-.05,1.05)
ylabel("Mol Fraction")
xlabel("Temperature (K)")
legend(loc='best')
showme()
clf()