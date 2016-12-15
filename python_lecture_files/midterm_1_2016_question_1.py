##Author: Dan Steingart
##Date Started: 2016-10-20
##Notes: Midterm Problem 1

from pithy import *

"""A simple cooling cycle operates between a target temperature of -10 C and an external sink of 25 C. It uses R22 as a working fluid and consists of two heat exchangers, a compressor, and a valve. 

The measured CoP of the cooling cycle is 5.3

If the compressor compresses a saturated vapor of R22 to 10 bar, and the fluid enters the valve as a saturated liquid, what is the isentropic efficiency of the compressor, and what is the real exit temperature?"""

#Write down what we know
Tc = 263.    #K
Th = 273+20. #K

Beta = 5.3 #Measured

#Lets assume the cycle is as follows
#######################################
#                                     #
#               (Q_h)                 #
#   3----- Heat Exchanger -----2      #
#   |                          |      #                     
#   |                          |      #
#  Valve                  Compressor  #
#   |                          |      #
#   |                          |      #
#   4------Heat Exchanger------1      #
#               (Q_c)                 #
#                                     #
#######################################


#State 1 is fully defined:
T1 = Tc
X1 = 1 #Saturated Vapor
#Look Up Enthalpy and Entropy on Table in back of exam
h1 = 246.15 #kJ/kg
s1 = 0.9424 #kJ/(kg K)
p1 = 3.54e5 #Pa

#State 2 We only know Pressure so far
p2 = 10e5 #Pa

#State 3 is fully defined
p3 = p2     #model a heat exchanger with no pressure change
X3 = 0      #Saturated Liquid
#Look Up Enthalpy and Entropy on Table in back of exam
h3 = 73.30 #kJ/kg
s3 = 0.275 #kJ/(kg K)

#State 4 is fully defined
p4 = p1 
h4 = h3

#So we know that Beta = 5.3 = Qc/(Qh-Qc)
#From 4-1 we can caclulate Qc/m
Qcbym = h1-h4
#Now we can caculate Qh
Qhbym = Qcbym/5.3 + Qcbym

#Now that we know Qh, through the upper heat exchanger
# Qhbym = h2-h3
h2 = h3+Qhbym
#Now state 2 is fully defined (p,H) and we know the output temperature
T2 = 50+273  #Estimated from Table 

#Now finds h2s by setting s2=s1 and p2 = 10 bar
h2s = 272 #kJ Estimated from Table
T2s = 40+273 #K Estimated from Table

#now solve for the isentropic effiency of a compressor

eta_s = (h1-h2s)/(h1-h2)
foo = whos(locals())


print "The exit temperature is %(T2).2f K and the isentropic efficiency of the compressor is %(eta_s).2f" % foo
