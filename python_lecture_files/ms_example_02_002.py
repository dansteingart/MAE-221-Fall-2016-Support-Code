##Author: 
##Date Started: 
##Notes: 
from pithy import *

# Step 1: Digest Given Information
p1 = 3 * 1e5 #Pa
V1 = 0.1 #m^3
V2 = 0.2 #m^3
Vs = linspace(V1,V2,100)
m = 0.4 #kg
Delu_12 = -55 #kJ/kg

n = 1.5

#make a polytropic helper function)
def pt(p,V,n): return (p*V[0]**n)/(V**n)

#make a pretty print helper function
#We give it the variable and the unit and it makes a nicely printed relationship.  Purely for display.
def pp(val,unit): print "%s = %.1f %s" %(val,eval(val),unit)

# Step 2: Write down laws
# Delta U = Q - W = m*(Delu_12). 
# Solve for Q => Q = m*(Delu_12)


# Step 3: Solve for Delta U and W

# Solve for internal energy change
DelU_12 = m*Delu_12

# Referencing example 2.1, we can solve for W

ps = pt(p1,Vs,n)
W_12 = trapz(ps,Vs)/1000 #Convert to kJ

Q_12 = W_12 + DelU_12


pp('Q_12',"kJ")
pp('W_12',"kJ")
pp('DelU_12',"kJ")

#Make a nice plot
plot(Vs,ps,'k') #plot ps vs. Vs
fill_between(Vs,ps,0,color="silver") #fill the area under the curve with silver
annotate("W_12 = %.1f kJ" % W_12,xy=(.15,.8e5),ha="center") #put the work value in the center of the plot

ylim(0,4e5)
xlim(0.05,.25)
xlabel("Volume (m^3)") #set the x label
ylabel("Pressure (Pa)") # set the y label
showme()
clf()


print "What does it mean that the heat generated is %.2f kJ? Is heat entering or leaving the system?  What can I do to achieve the condition where there is no heat transfer?" % Q_12