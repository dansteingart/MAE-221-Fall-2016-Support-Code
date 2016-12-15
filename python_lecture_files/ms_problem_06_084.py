##Author: Wenkai Liang
##Date Started: 2016-10-17
##Notes: MS P6.84

from pithy import *

# mass balance
m1 = 4. #kg/s
m3 = 5. #kg/s
m4 = 3. #kg/s
m2 = m3+m4-m1 #kg/s
print 'm2=',m2, 'kg/s'

# energy balance
W = 1174.9e3 # W
h1 = 3382.4e3 # J/kg
h3 = 2870.5e3 # J/kg
h4 = 3273.4e3 # J/kg
h2 = (W-m1*h1+m3*h3+m4*h4)/m2 # J/kg
print 'h2=',h2/1000, 'kJ/kg'

# entropy balance
p2 = 1.0e5 # Pa
s2 = stater('P',p2,'H',h2,'water')['S'] #kJ/kgK
print 's2=',s2/1000, 'kJ/kgK'
s1 = 8.6926e3 #kJ/kgK
s3 = 7.5066e3 #kJ/kgK
s4 = 7.8985e3 #kJ/kgK
sigma = m3*s3+m4*s4-m1*s1-m2*s2
print 's production=',sigma/1000, 'kJ/K/s'
print 'negative, impossible!'