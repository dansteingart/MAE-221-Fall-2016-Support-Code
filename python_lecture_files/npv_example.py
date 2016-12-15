##OK TO COPY
from pithy import *

rate = .01
c_out = 1000
c_in = 100


def tnpv(rate):
    a = [-c_out]
    npvs = []
    for i in range(30):a.append(c_in)
    for i in range(len(a)): 
        npvs.append(npv(rate,a[0:i+1]))
    ts = range(1,len(npvs)+1)
    return ts,npvs

ttp = []
rates = arange(0,10,1.5)*.01
for rate in rates:
    a = tnpv(rate)
    for i in a[1]:
        if i > 0:
            ttp.append(a[1].index(i))
            break
        
    plot(a[0],a[1],label="discount = %s%%"% (str(rate*100)))

axhline(0,color='k',linestyle="--")
annotate("time to profit",xy=(0.3,10))
title("NPV vs. Time; c_in = \$%i/year; c_initial = \$%i" %(c_in,c_out))
ylabel("NPV ($)")
xlabel("Time (years)")
legend(loc="best")
showme()
clf()




