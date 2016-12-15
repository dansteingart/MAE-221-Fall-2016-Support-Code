##Author: Dan Steingart
##Date Started: 2016-09-26
##Notes: Test All Approximations Part 2

from pithy import *

#NB: the 'stater' function has one odd thing to it: all inputs, even if mass normalized, are presented by CAPITAL letters

#e.g. pressure = P, quality = Q, Temperature = T, specific volume =V, etc.

#Let's test the accuracy of the u(T,p) = uf(T) approximation

p = 1e4
Ts = linspace(274,400,300)
st_utp = stater('P',p,'T',Ts,'water')
st_uft = stater('Q',0,'T',Ts,'water')
plot(Ts,st_utp['U'],label="$u(T,p)$")
plot(Ts,st_uft['U'],label="$u_{f}(T)$")
#plot(Ts,st_utp['H'],label="$h(T,p)$")
#plot(Ts,st_uft['H'],label="$h_{f}(T)$")
legend(loc="best")
ylabel("u (J/(kg K))")
xlabel("T (K)")
showme()
clf()

