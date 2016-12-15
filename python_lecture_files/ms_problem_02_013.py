##Author: Dan Steingart
##Date Started: 2016-09-14
##Notes: MS problem 2-13



sol = """

First write out balances for KE and PE, let's just use 1 mass for now

KE = 1/2 m*V2^2-V1^2
PE = m*g*(h2-h1)

When all of the energy is transferred
KE + PE = 0

We're told that they start from the same point, and that they start with the same initial velocity.  When we reach the maximum height by definition the velocity at this point must be 0 (otherwise it would keep moving)

V2 = 0

h1 = 0

Subbing in the balance
-1/2 m*V1^2 + m*g*h2 = 0

So m drops out nicely, and we see that

1/2 V1^2 = g*h2

So regardless of how heavy the mass is, if we achieve the same velocity to being with we will reach the same height.

Does this mean it requires the same amount of _energy_ to realize this result for the two different masses?

"""

print sol