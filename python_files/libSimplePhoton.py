# This is a basic library for interacting with the particle code in labs 1 and 2
# Below the main is a basic example of how to read and set data
from commands import getoutput as go
import json
import time
from glob import glob
import os
import SSE


class simplePhoton():
    def __init__(self,name):
        self.name = name
        self.particle = SSE.name_lookup[name]
        self.ac = open("/home/labroot/ac").read().strip()


    def setOutput(self,bit,value):
        '''set digital pin number bit to value, where value = 1 is HIGH and value = 0 is LOW'''
        return go('curl -s https://api.particle.io/v1/devices/%s/setOutput \
         -d access_token=%s \
         -d "args=%i%i"' % (self.particle,self.ac,bit,value))


    def setOutputs(self,arr):
        '''set all digital pins at once, where 1 is high and 0 is low'''
        if len(arr) != 4:
            return "need exactly four bits"
        else:
            value = ""
            for a in arr: value += str(a)
            return go('curl -s https://api.particle.io/v1/devices/%s/setOutputs \
         -d access_token=%s \
         -d "args=%s"' % (self.particle,self.ac,value))

    def getState(self):
        '''Get current data from sparks'''
        '''This calls spark by the core ID'''
        data = go("curl -s -G https://api.spark.io/v1/devices/%s/lab_data -d access_token=%s" % (self.particle,self.ac))
        data = json.loads(data)
        st = data['result']
        data['result'] =  json.loads(st)
        data['result']['time'] = time.time()
        return data['result']


    def getHistory(self,date=None):
        '''This pulls history by spark name'''
        import pandas as pd
        fils = glob("/files/%s*.csv" % self.name)
        fils.sort()
        # print fils
        f = fils[-1]
        if date != None:
            ft = "/files/%s_%s.csv" % (self.name,str(date))
            if os.path.isfile(ft): f = ft
            else: print "No file at that date, defaulting to most recent data"
            
        df = pd.read_csv(f)
        return df


if __name__ == "__main__":
    b = simplePhoton('GrumpyGourd')
    # b.setOutput(0,0) #set output 0 to low
    # b.setOutput(1,0) #set output 1 to low
    # b.setOutputs([0,0,0,0]) #set outputs 0 through 3 to low
    a = b.getHistory() #get data
    print a #print dictionary