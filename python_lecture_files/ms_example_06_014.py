##Author: Dan Steingart
##Date Started: 2016-10-15
##Notes: MS Example 6.14

"""For the compressor of the heat pump system in Example 6.8, determine the power, in kW, and the isentropic efficiency using data from property tables"""


from pithy import *

St = {}

#Set States
T1 = 273-5 #K
p1 = 3.5e5 #Pa
St[1] = stater('T',T1,'P',p1,'R22')

#Real State 2
T2 = 75+273 #K
p2 = 14e5
St[2] = stater('T',T2,'P',p2,'R22')

#Isentropic State 2
s2s = St[1]['S']
p2 = 14e5
St['2s'] = stater('S',s2s,'P',p2,'R22')

print state_table(St)

delh12s = St['2s']['H'] - St[1]['H']
delh12 = St[2]['H'] - St[1]['H']

#now caclulate isentropic effiency
eta_s = delh12s/delh12

print "The isentropic effiency is %.2f" % eta_s