from commands import getoutput as go
import json
import time
import os
from glob import glob
import pandas as pd

class motorPhoton():
    def __init__(self,name=None):
        self.particle = name
        self.ac = open("/home/labroot/ac").read().strip()
        
    def getNames(self):
        return go('curl -s https://api.particle.io/v1/devices?access_token=%s' % self.ac)

    def setOutput(self,bit,value):
        if value == 0:
            out = str(bit)+str(0)+str(0).rjust(3,"0")
        else :
            out = str(bit)+str(1)+str(255).rjust(3,"0")
        return go('curl -s https://api.particle.io/v1/devices/%s/setMotor \
         -d access_token=%s \
         -d "args=%s"' % (self.particle,self.ac,out))

    def setMotor(self,motor,mode,pwm):
        if (motor == 2) and (pwm > 200):
            pwm = 200
            print "Warning! TE device should not be set past 200, setting it to 200 for you."
        out = str(motor)+str(mode)+str(pwm).rjust(3,"0")
        return go('curl -s https://api.particle.io/v1/devices/%s/setMotor \
         -d access_token=%s \
         -d "args=%s"' % (self.particle,self.ac,out))

    def setMotors(self,m1,m2,m3):
        out = str(m1).rjust(3,"0")+str(m2).rjust(3,"0")+str(m3).rjust(3,"0")
        return go('curl -s https://api.particle.io/v1/devices/%s/setMotors \
         -d access_token=%s \
         -d "args=%s"' % (self.particle,self.ac,out))
         
    def getData(self):
        # data = go("curl -s -G https://api.spark.io/v1/devices/%s/lab_data -d access_token=%s" % (self.particle,self.ac))
        # # print data
        # data = json.loads(data)
        # st = data['result']
        # data['result']         = json.loads(st)
        # data['result']['time'] = time.time()
        # data = pd.DataFrame(data['result'])
        return self.getHistory().iloc[-1]
    
    def getHistory(self,date=None):
        import pandas as pd
        print go("pwd")
        fils = glob("/files/%s*.csv" % self.particle)
        # print fils
        fils.sort()
        f = fils[-1]
        if date != None:
            ft = "/files/%s_%s.csv" % (self.particle,str(date))
            if os.path.isfile(ft): f = ft
            else: print "No file at that date, defaulting to most recent data"
            
        df = pd.read_csv(f,error_bad_lines=False)
        return df


if __name__ == "__main__":
    b = motorPhoton("MischievousMelon")
    foo = b.getHistory()
    # exit()
    
    #print foo['a0'] * 3
    
    print "here"
    
    print b.getHistory("2016-11-09")
     
    # b.setMotor(2,1,200)
    # b.setMotors(1,1,1)
    # time.sleep(2)
    # b.setMotor(2,0,128)
    # print "motor off"
    # exit()
    #seems ok?
    #everyonce and while it doesn't return aresult.  did you flash motorphoton on the particle?  
    
    #Nope. I guess that's a good idea. Thought it was an additional plug-in already coded....
    
    
    #it's a different set of commands.  enables PWM, removes the thermocouple (basically the PWM takes the pins we used for the MAX31855).
    
    #https://github.com/dansteingart/MAE-221-Fall-2015-Support-Code
    
    #https://github.com/dansteingart/MAE-221-Fall-2015-Support-Code/blob/master/week_5_to_8_spark_code_motor.ino
    
    # print b.setMotor(0,1,255)
    # print b.setMotor(1,1,255)
    # time.sleep(10)
    # print b.setMotors(0,0,0)
    # print b.setMotors(1,0,0)
    
