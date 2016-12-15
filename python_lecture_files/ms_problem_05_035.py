##Author: Cody Nunno
##Date Started: 2016-10-08
##Notes: 

from pithy import *

Q_dot = 5.1e5*0.293071 # W = J/s
W_dot_a = 90*745.7 # W
W_dot_b = 100*745.7 # W
W_dot_c = 110*745.7 # W
T_H = 1000.0 # K
T_C = 500.0 # K
eta = 1 - T_C/T_H
print 'Maximum possible efficiency = ',eta
print ''

print 'Part A'
eta_a = W_dot_a/Q_dot
print 'Part A efficiency = ',eta_a
print 'Efficiency less than theoretical max, therefore possible'
print ''

print 'Part B'
eta_b = W_dot_b/Q_dot
print 'Part B efficiency = ',eta_b
print 'Efficiency less than theoretical max, therefore possible, but harder to achieve than previous example'
print ''

print 'Part C'
eta_c = W_dot_c/Q_dot
print 'Part C efficiency = ',eta_c
print 'Efficiency greater than theoretical max, therefore impossible'