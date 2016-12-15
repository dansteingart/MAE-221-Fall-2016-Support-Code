##Author: Dan Steingart
##Date Started: 2016-09-14
##Notes: MS problem 1-30


from pithy import *

#Step One: Collect and Digest Given Information from Problem Statement

g = 9.81 #m/s^2
m_piston = 24.5 #kg
m_shaft = 0.5 #kg
A_shaft = 0.8*(.01)**2 #m
D_piston = .10 #m
p_gas = 3*1e5 #Pa
p_atm = 1e5 #Pa

##Step Two: We're asked for forces, so let's calculate areas so we can back pressure into Force"

#Calculate the piston area
A_piston = (D_piston/2)**2 * 3.1415


#Now let's calculate all of the forces present


F_atm = p_atm*(A_piston-A_shaft)  #This calculation assumes that the area of the shaft is not being effected by the atmospheric pressure.  The book's answer key makes this assumption but I don't quite buy it.  So if you choose to just assume

F_atm_alt = p_atm*A_piston

#This is fine.


F_piston = m_piston * g
F_shaft  = m_shaft  * g
F_gas = p_gas* A_piston


F = F_gas - F_piston-F_shaft - F_atm
F_alt = F_gas - F_piston - F_shaft - F_atm_alt  

print
print "If we assume that the shaft area does not see atmospheric pressure then the force required to realize the state is", F, "N"

print 
print "If we assume that the shaft area does see atmospheric pressure then the force required to realize the state is", F_alt, "N"

print


print "Showing all values for debugging purposes"
whos(locals())

