##OK TO COPY
import numpy
import matplotlib
import time
import StringIO
import urllib
import base64
from glob import glob
matplotlib.use('agg')
from pylab import *
from CoolProp.CoolProp import PropsSI as pr
from CoolProp.CoolProp import PhaseSI as ph
from quiner import *

import inspect, re

#small change for testing purposes

##thanks stack http://stackoverflow.com/questions/592746/how-can-you-print-a-variable-name-in-python
def varname(p):
  for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
    m = re.search(r'\bvarname\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
    if m:
      return m.group(1)


def csv_to_table(csv):
    csv = csv.strip()
    out = "<table style='border-collapse:collapse;font-size:15px; border: 1px black solid;'>"
    for c in csv.split("\n"):
        out+="<tr>"
        for p in c.split(","):
            out+="<td style='margin:0;padding:5px;text-align:center;border: 1px black solid'>%s</td>" % p
        out+= "</tr>"
    out+= "</table>"
    return out

def pv_phase_envelope(substance,fill=None):
    Pc = pr('Pcrit',substance)
    Pm = pr('P_min',substance)
    Psweep = linspace(Pm,Pc,1000)
    Psweep[-1] = Pc-.01
    v_sl = 1/pr('D','Q',0,'P',Psweep,substance)
    v_sv = 1/pr('D','Q',1,'P',Psweep,substance)
    vs = array(list(v_sl)+list(v_sv)[::-1])
    Ps = array(list(Psweep)+list(Psweep)[::-1])
    plot(vs,Ps,'.2')

    if fill != None: 
        if fill == True: fill = 'silver'
        fill_between(vs,Ps,0,color=fill,alpha=.5)
        
    return vs,Ps


def ph_phase_envelope(substance,fill=None):
    Pc = pr('Pcrit',substance)
    Pm = pr('P_min',substance)
    Psweep = linspace(Pm,Pc,1000)
    Psweep[-1] = Pc-.01
    h_sl = pr('H','Q',0,'P',Psweep,substance)
    h_sv = pr('H','Q',1,'P',Psweep,substance)
    hs = array(list(h_sl)+list(h_sv)[::-1])
    Ps = array(list(Psweep)+list(Psweep)[::-1])
    plot(hs,Ps,'.2')
    
    if fill != None: 
        if fill == True: fill = 'silver'
        fill_between(hs,Ps,0,color=fill,alpha=.5)

    return hs,Ps


def ts_phase_envelope(substance,fill=None):
    Tc = pr('Tcrit',substance)
    Tf = pr('Tmin',substance)
    Tsweep = linspace(Tf,Tc,100)
    Tsweep[-1] = Tc-.1
    s_sl = pr('S','Q',0,'T',Tsweep,substance)
    s_sv = pr('S','Q',1,'T',Tsweep,substance)
    ss = array(list(s_sl)+list(s_sv)[::-1])
    Ts = array(list(Tsweep)+list(Tsweep)[::-1])
    plot(ss,Ts,'.2')
    if fill != None: 
        if fill == True: fill = 'silver'
        fill_between(ss,Ts,0,color=fill,alpha=.5)
    return ss,Ts
    
def tv_phase_envelope(substance,fill=None):
    Tc = pr('Tcrit',substance)
    Tf = pr('Tmin',substance)
    Tsweep = linspace(Tf,Tc,100)
    Tsweep[-1] = Tc-.1
    v_sl = 1/pr('D','Q',0,'T',Tsweep,substance)
    v_sv = 1/pr('D','Q',1,'T',Tsweep,substance)
    vs = array(list(v_sl)+list(v_sv)[::-1])
    Ts = array(list(Tsweep)+list(Tsweep)[::-1])
    plot(vs,Ts,'.2')
    if fill != None: 
        if fill == True: fill = 'silver'
        fill_between(vs,Ts,0,color=fill,alpha=.5)

    return vs,Ts


def stater(arg1,arg2,arg3,arg4,arg5):
    out = {}
    arg1 = arg1.upper()
    arg3 = arg3.upper()
    terms = ['T','H','U','S','Q','P','D']

    #allow volume calcs
    if arg1 == 'V': 
        arg1 = 'D'
        arg2 = 1/arg2
    if arg3 == 'V': 
        arg3 = 'D'
        arg4 = 1/arg4


    for t in terms:
        out[t]     = pr(t,arg1,arg2,arg3,arg4,arg5)
    
    ##weird bug that cody and nikita caught
    bad = "V,D,Q".split(",")
    
    if (arg1 in bad) and (arg3 in bad): 
        #"this might be borked"
        arg1 = 'D'
        arg2 = out['D']
        arg3 = 'T'
        arg4 = out['T']

    for t in terms:
        out[t]     = pr(t,arg1,arg2,arg3,arg4,arg5)

    out['V']     = 1/out['D']
    try:
        out['phase'] = ph(arg1,arg2,arg3,arg4,arg5)
    except: out['phase'] = "NA"
    out['substance'] = arg5
    return out


def state_table(ll):
    k = ll.keys()
    k.sort()
    h = ll[k[0]].keys()
    h.sort()
    sty = """<style>
    table
    {
        font-size:12px;
        
    }
    
    td
    {
        padding:5px;
    }
    </style>"""
    
    ud = {'D':'(kg/m^3)', 'H':'(J/kg)','P':'(Pa)','Q':'','S':'(J/(K kg))','T':'(K)', 'V':'(m^3/kg)','U':'(J/kg)','phase':'','substance':''}
    
    print sty
    tab = "<table>"
    tab = tab + "<tr>"
    tab+='<th>State</th>'
    for i in h: tab+='<th>%s %s</th>' % (i,ud[i])
    tab += '</tr>'
    for j in k:
        l = ll[j]
        tab += '<tr>'
        tab += '<td>%s</td>' % str(j)
        for i in h: 
            if (i == "Q") & (l[i] == -1): l[i] = "N/A"
            try: tab+='<td>%.2E</td>' % float(l[i])
            except: tab+='<td>%s</td>' % str(l[i])
        tab += '</tr>'
    tab += "</table>"
    return tab  


fig, ax = plt.subplots()

#Figure Defaults
#rcParams['font.family'] = "Arial"


#hack to make things worth from PIL

def showint():
    print mpld3.fig_to_d3(fig).replace("\n","\r")

def himg(fn):
    print "<img src='%s'>" % fn 

def showimg(im,tip=".png",width=None,dpi=150):
    tim = str(int(time.time()))    
    #imname = imname.replace("/","-")
    image = 'images/pithy_img_'+str(int(time.time()*1000))+tip
    im.save(image,dpi=dpi)
    
    if width != None:
        print "<img src='%s' style='width:%s'>" % (image,str(width)),
    else: print '##_holder_##:',"/"+image
    

def showme(tip="png",kind="static",width=None,height=None,inline=False,dpi=80):
    tim = str(int(time.time()))	
    image = 'images/pithy_img_'+str(int(time.time()*1000))+"."+tip
    w = ""
    h = ""
    if width != None: w = "width:"+str(width)+"px;"
    if height != None: h = "height:"+str(height)+"px;"
    s = "style='%s%s'" %(w,h)
    #strang = '<img '+s+' src=/'+image+'>'
    if kind == "static": 
        print imager64(tip=tip,dpi=dpi,style=s),
        if not inline: print ""

    else: 
        savefig(image,dpi=dpi,bbox_inches="tight")
        print '##_dynamic_##:',kind,':',tim,':',"/"+image




def imager64(tip="png",dpi=80,style=None):
    imgdata = StringIO.StringIO()
    savefig(imgdata,dpi=dpi,tip=tip,bbox_inches="tight")
    imgdata.seek(0)  # rewind the data
    preload = 'data:image/%s;base64,'% tip 
    if tip == "svg":
        preload = 'data:image/svg+xml;;base64,' 
    uri =  preload+urllib.quote(base64.b64encode(imgdata.buf))
    return '<img %s src = "%s"/>' % (style,uri)

#A smoothing function I use
def smooth(x,window_len=11,window='flat'):
    if x.ndim != 1:
        raise ValueError, "smooth only accepts 1 dimension arrays."

    if x.size < window_len:
        raise ValueError, "Input vector needs to be bigger than window size."


    if window_len<3:
        return x


    if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise ValueError, "Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'"


    s=numpy.r_[x[window_len-1:0:-1],x,x[-1:-window_len:-1]]
    #print(len(s))
    if window == 'flat': #moving average
        w=numpy.ones(window_len,'d')
    else:
        w=eval('numpy.'+window+'(window_len)')

    y=numpy.convolve(w/w.sum(),s,mode='valid')
    
    y = list(y)
    #account for windowing shift 2012-08-02
    for j in range(0,int(window_len)):
        y.pop(0)

    
    return array(y)





def strrip(string,ff,fl):
    part1 = string.find(ff)
    part2 = string.find(fl)
    return string[part1+len(ff):part2]

#line # hack from http://code.activestate.com/recipes/145297-grabbing-the-current-line-number-easily/
def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

def refresh(interval = 5):
    print "<meta http-equiv='refresh' content='%i'>" % interval





clf()

if __name__ == "__main__":
    print rcParams['figure.figsize']
    print rcParams['figure.dpi']
    
    a = linspace(0,1,100)
    for i in logspace(-1,1,10):
        plot(a,a**i)
    showme()
    clf()

