##Author: Cody Nunno
##Date Started: 2016-12-15
##Notes: MS Problem 13.8

from pithy import *
"Balance using element conservation.  Number of each species in the reactants must be present in the products"
print "a) 2CH_4 + C_2H_6 + 9O_2 + 34.17333N_2 -> 4CO_2 + 7H_2O + 1.5O_2 + 34.17333N_2"

mol_CH4 = 2.0 #mol
mol_C2H6 = 1.0 #mol
mol_N2_f = 0.333333333333333333 #mol
mol_O2 = 9.0 #mol
mol_N2_a = 33.84 #mol

mol_fuel = mol_CH4+mol_C2H6+mol_N2_f
mol_air = mol_O2 + mol_N2_a

AF_mol = mol_air/mol_fuel

m_CH4 = 16.04*mol_CH4 #g
m_C2H6 = 30.07*mol_C2H6
m_N2_f = 28.01*mol_N2_f
m_O2 = 32.0*mol_O2
m_N2_a = 28.01*mol_N2_a

m_fuel = m_CH4+m_C2H6+m_N2_f
m_air = m_O2 + m_N2_a

AF_m = m_air/m_fuel

print "b) Molar A/F = %.2f, mass-based F/A = %.2f" % (AF_mol,AF_m)