##Author: Cody Nunno
##Date Started: 2016-11-11
##Notes: 

from pithy import *

St = {}

# Step 1: Write down what we know to start
T1 = 290.0 #K
p1 = 1.0e5 #Pa
V1 = 400.0e-6 #m^3

r = linspace(2,12,25)

T3 = 2200.0 #K

k = 1.4
cp = 1005.0 #J/kgK
cv = 718.0 #J/kgK
R = 287.0

# Step 2: Solve for the cycles, simultaneously for all compression ratios
# State 1
v1 = R*T1/p1
m = V1/v1

#State 2
v2 = v1/r
p2 = p1*v1**k/(v2**k)
T2 = p2*v2/R

# State 3
v3 = v2
p3 = R*T3/v3

# State 4
v4 = r*v3
p4 = p3*v3**k/(v4**k)
T4 = p4*v4/R

# Step 3: Solve for heat addition and work
u1 = cv*T1
u2 = cv*T2
u3 = cv*T3
u4 = cv*T4
Q12 = 0.0
W12 = m*(u1-u2)
Q23 = m*(u3-u2)
W23 = 0.0
Q34 = 0.0
W34 = m*(u3-u4)
Q41 = m*(u4-u1)
W41 = 0.0
Wnet = W12+W23+W34+W41

# Step 4: Find efficiency and mep
eta = Wnet/(Q23)

mep = Wnet/(V1*(1-1/r))

# Step 5: Plot
plot(r,Q23/1000)
xlabel("Compression Ratio")
ylabel("Heat Addition, kJ")
showme()
clf()

plot(r,Wnet/1000)
xlabel("Compression Ratio")
ylabel("Net Work, kJ")
showme()
clf()

plot(r,eta)
xlabel("Compression Ratio")
ylabel("Thermal Efficiency")
showme()
clf()

plot(r,mep*1e-5)
xlabel("Compression Ratio")
ylabel("Mean Effective Pressure, bar")
showme()
clf()