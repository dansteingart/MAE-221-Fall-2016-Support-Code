##Author: Cody Nunno
##Date Started: 2016-10-23
##Notes: MS Problem 5.6

from pithy import *

eta_R = 1.0
eta_I = 2.0/3.0

print """Recall that for a reversible cycle, per the K-P statement, W_net = 0, and for an irreversible cycle, W_net<0, all for a single reservoir.

If we draw our borders correctly in the figure referenced, we can convert it into a cycle with a single thermal reservoir.  We know that the hot reservoir used is the same, which allows us to simultaneously say that W_I = 2/3 W_R (through the formula for efficiency) and also to draw a system boundary around the two.  

If one reverses the reversible process, we can set up an equality such that:

W_net = W_I - W_R = -1/3 W_R

This is consistent with the Kelvin-Planck statement of the second law, which states that:

W_net = 0 (for reversible cycles)

W_net < 0 (for irreversible cycles)

Since W_net is less than 0 in this case, and we have assumed W_R to be rversible, the negative cycle work indicates that W_I must be irreversible. """
