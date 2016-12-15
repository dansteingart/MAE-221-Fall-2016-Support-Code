##Author: Dan Steingart
##Date Started: 2016-09-14
##Notes: MS problem 2-34

from pithy import *

#Step 1: Digest the Givens
V1 = 0.2  #m^3
V2 = 1.0    #m^3
V3 = V2
p3 = 1e5  #Pa

#Step 2: fill in missing states
#p3*V3 = p1*V1 as n = 1 

p1 = V3*p3/V1
p2 = p1


#collect and plot
ps = [p1,p2,p3,p1] #this makes a list of pressures
Vs = [V1,V2,V3,V1] #this makes a list of volumes

plot(Vs,ps,'k') #plot Vs vs. Ps
xlim(0,1.5) #explicitly set x limits
ylim(0,6e5) #explicitly set y limits
xlabel("Volume (m^3)") #good people label axes!
ylabel("Pressure (Pa)")#ibid!

#label the points
for i in range(3):annotate(str(i+1),xy=(Vs[i],ps[i]))

#show me the plot!
showme()


#again it is assumed that the 3 -> 1 step is a simple linear sweep when we plot it this wway.  We should check it in the same we we checked 1_31

V31 = linspace(V3,V1,50) #create a sweep from V3 to V1 in 50 steps
p31 = V3*p3/V31 #use polytropic relation where n = 1
plot(V31,p31,'r') #plot the real line, color it red ('r')

showme()
clf()

#Now we see that the linear approximation (connecting the two dots) is a bad one if p1V1 = p3V3

#calculate in each step
W12 = p1*(V2-V1)/1000 #constant pressure
W23 = 0 #dV = 0 
W31 = p1*V1 * log(V1/V3)/1000 #polytropic work function

#print the work for each step
print "W12 = ", W12, "kJ" 
print "W23 = ", W23, "kJ"
print "W23 = ", W31, "kJ"

#print the net work
Wnet = W12+W23+W31
print "The net work is",round(Wnet,2),"kJ"