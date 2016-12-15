##Author: Wenkai Liang
##Date Started: 11-12-2016
##Notes: 

print 'eff=1-(Cv(T5-T1))/(Cv(T3-T2)+Cp(T4-T3))=1-(T5-T1)/(T3-T2+k(T4-T3))'
print ''
print 'r=v1/v2'
print 'rc=v4/v3'
print 'rp=p3/p2'
print ''
print 'T1=T2/r^{k-1}'
print 'T3=rp*T2'
print 'T4=rc*T3=rc*rp*T2'
print 'T5=(rc/r)^{k-1}T4=rp(rc^k/r^{k-1})T2'
print ''
print 'Substitute in'
print 'eff=1-1/(r^{k-1})[(rp*rc^k-1)/((rp-1))+k*rp(rc-1)]'