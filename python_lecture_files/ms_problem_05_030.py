##Author: Cody Nunno
##Date Started: 2016-10-08
##Notes: 

from pithy import *

T_c = 300.0 # K
print 'Part A:'
T_ha = 900.0 # K
eta_a = 1-T_c/T_ha
print 'Part A efficiency =', eta_a
print 'Maximum efficiency 40% or greater, therefore it is entirely possible.'
print ''

print 'Part B:'
T_hb = 500.0 # K
eta_b = 1-T_c/T_hb
print 'Part B efficiency =', eta_b
print 'Maximum efficiency exactly 40%; possible, but difficult to achieve.'
print ''

print 'Part C:'
T_hc = 375.0 # K
eta_c = 1-T_c/T_hc
print 'Part C efficiency =', eta_c
print 'Maximum efficiency less than 40%; the device is impossible.'
print ''
