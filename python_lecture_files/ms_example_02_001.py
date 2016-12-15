##Author: 
##Date Started: 
##Notes: 
from pithy import *

#In this problem we are asked to example the work done on/by the system for 3 different values of exponent n inthe polytropic process for a piston that starts at 3 Bar and has a volume expansion of 0.1 m^3.

#In addition to what the book asks, We'll also explore the benefits and detriments of numerical vs. analytical calculations.

#Step 1: Digest and make consistent the given information
#(i.e. make sure dimensions are consistent)

p1 = 3 * 1e5 #Pa
V1 = 0.1 #m^3
V2 = 0.2 #m^3

ss = 100
Vs = linspace(V1,V2,ss) #This is a special numpy function to make an array from V1 to V2 in ss steps.  This becomes important when examining the accuracy of the numerical solution
 
#make a polytropic helper function)
def pt(p,V,n): return (p*V[0]**n)/(V**n)

#Step 2: work the problem

#case 1 => n = 1.5
n1 = 1.5
p_n1 = pt(p1,Vs,n1)
plot(Vs,p_n1,label="n = %.1f" % n1)

#case 2 => n = 1
n2 = 1
p_n2 = pt(p1,Vs,n2)
plot(Vs,p_n2,label="n = %.1f" % n2)

#case 3 => n = 0
n3 = 0
p_n3 = pt(p1,Vs,n3)
plot(Vs,p_n3,label="n = %.1f" % n3)

ylim(0,4e5)
xlim(0.05,.25)
xlabel("Volume (m^3)")
ylabel("Pressure (Pa)")
legend()
showme()
clf()

#Calculate Work with Trapezoidal Rule (a numpy function imported with pithy)
W_numerical_n1 = trapz(p_n1,Vs)
W_numerical_n2 = trapz(p_n2,Vs)
W_numerical_n3 = trapz(p_n3,Vs)

#Calculate Work with Analytical Methods
W_analytical_n1 = (p1*V1-p_n1[-1]*V2)/(n1-1)
W_analytical_n2 = p1*V1*log(V2/V1)
W_analytical_n3 = p1*(V2-V1)

#Make a basic table and demonstrte dicitonaries
##Here is a basic example of something called a python dictionary in a list.  It is useful storing and sorting data
test1 = {}
test1['n']= n1
test1['W_numerical']= W_numerical_n1
test1['W_analytical']= W_analytical_n1

test2 = {}
test2['n']= n2
test2['W_numerical']= W_numerical_n2
test2['W_analytical']= W_analytical_n2

test3 = {}
test3['n']= n3
test3['W_numerical']= W_numerical_n3
test3['W_analytical']= W_analytical_n3

ns = [test1,test2,test3] #make a list


#make a csv (comma separated variable to make a table)
out = "n,W_analytical (J),W_numerical (J),Abs Difference %\n"

#now use our handy list of dictionaries
for i in ns: 
    out+= "%.1f,%.4e,%.4e,%.3f\n" % (
        i['n'],
        i['W_analytical'],
        i['W_numerical'],
        100*abs(i['W_analytical']-i['W_numerical'])/i['W_analytical']
        )

print ""
print "Now let's explore the difference between the analytical and trapz methods.  If I go back and make 'ss' smaller or larger, how will this change the absolute difference?"

print csv_to_table(out)



