from pithy import *



##fit based on SH Fit
##SH = [-0.00227767697972 , 0.00149400196236 , -0.000154074429382 , 6.32371281938e-06 ] #much better fit

##Much much better fit DS 2016-11-28 see epcos_calibrate
SH = [1.11708184e-03,2.37689485e-04,-3.14958029e-07,9.74828722e-08]


def Steinhart_Hart(R,A,B,C,D):
    T = 1/(A+B*log(R)+ C*log(R)**2 + D*log(R)**3)
    return T#-273.15
    
def epcos6850(A,res):
    Vn = 4095
    Rt = Vn*(res/A - res/Vn)
    return Steinhart_Hart(Rt ,SH[0],SH[1],SH[2],SH[3])-273

def usp10982(A,res):
    Vn = 4095
    Rt = Vn*(res/A - res/Vn)
    z = [ -5.31102462e-90,2.08145376e-84,-3.47746695e-79,3.07689622e-74,-1.30806301e-69,  -8.41244808e-66,   3.92873659e-60,  -1.59312460e-55,-3.27177767e-51,6.60751181e-46,-3.72813235e-41,1.30485380e-36,  -3.22043711e-32,5.85323113e-28,-7.95575941e-24,8.09898689e-20,-6.12865908e-16,3.39705510e-12,-1.35143184e-08,3.77958863e-05,-7.55932368e-02,1.35228121e+02]
    p = poly1d(z)
    return p(Rt)


def nibthermistor(A,res):
    Vn = 4095
    Rt = Vn*(res/A - res/Vn)
    A =  1.03210e-3
    B =  2.38710e-4 
    C =  1.58*10e-7
    T =  1/(A+B*log(Rt)+ C*log(Rt)**2)
    return T-273.15
    
def etape(A,res):
    Vn = 4095
    Rtape = Vn*(res/A - res/Vn)
    level = 519/35-(11*Rtape)/1750
    return level