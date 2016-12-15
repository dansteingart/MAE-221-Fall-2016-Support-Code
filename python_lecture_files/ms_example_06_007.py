##Author: Dan Steingart
##Date Started: 2016-10-10
##Notes: MS Example 6.7

from pithy import *

T1 = 70+530. #degR
T2 = 175+530. #degR
T3 = 0+530. #degR


p1 = 5.1 #atm
p2 = 1   #atm
p3 = 1   #atm

cp = 0.24 #Btu/(lb R)
R = 1.986/28.97 #Btu/(lb R)

#m1 = m2 + m3
#m3 = .6m1, m2 = .4 m1
#0 = .4 m1 cp * (T1-T2) + .6 m2 cp *(T1-T3)

delE = .4*(T1-T2)+.6*(T1-T3)
if delE == 0: 
    print "The 1st law is satisfied"
else: 
    print "The first law is not satisfied"
    exit()

Q = 0

sigmacvbymdot = .4*(cp*log(T2/T1) - R*log(p2/p1))  + .6*(cp*log(T3/T1)-R*log(p3/p1))


print "The entropy geneated is %.4f Btu/(lb R)" %  sigmacvbymdot

if sigmacvbymdot >= 0: 
    print "The second law is satisfied, the process is possible"
else: 
    print "The second law is not satisfied"
    exit()
