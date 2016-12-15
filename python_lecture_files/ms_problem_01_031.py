##Author: Dan Steingart
##Date Started: 2016-09-14
##Notes: MS problem 1-31



from pithy import *

#Step 1: Write down what we know
#Constant Pressure expansion: we don't know what P1 is yet
V1 = 0.5 #m^3
V2 = 2.0 #m^3

#Constant Volume, Pressure changes
V3 = V2
p3 = 2*1e5 #Pa

#Constant Pressure compression
p4 = p3
V4 = 1.0 #m^3


#Step 2: Determine missing properties from processes
#We know P4 and V4, and we know how State 4 relates to State 1 (pV**(-1) = constant, so)

##p4*V4**(-1) = p1*V1**(-1)

p1 = p4*V4**(-1)/V1**(-1) #solve for p1
p2 = p1 #we know step 1-2 is constant pressure

#Now some fancy python stuff
ps = [p1,p2,p3,p4,p1] #make a list of pressures
Vs = [V1,V2,V3,V4,V1] #make a list of volumes


plot(Vs,ps,'k') #plot the above lists, make the curve black ('k')

#note each point
for i in range(4):annotate(str(i+1),xy=(Vs[i],ps[i]))

#explicitly set limits and label axes
ylim(5e4,2.5e5)
ylabel("Pressure (Pa)")
xlabel("Volume (m^3)")
xlim(0,2.5)

showme() #show me the plot!

#note that the 4 to 1 transition assumes something linear, we should check that.  here's a numpy trick to do that

V41 = linspace(V4,V1,20) #sweep from V4 to V1 in 20 steps
p41 = p4*V4**(-1.0)/V41**(-1.0)

plot(V41,p41,'r.') #plot the real process in red
showme()

#so the linear assumption isn't a bad one
clf() #clear the figure