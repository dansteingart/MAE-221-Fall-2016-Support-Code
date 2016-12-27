from pymongo import MongoClient as mc
from datetime import datetime as dt
import pandas as pd
from pithy import *
from datetime import datetime as dt

#Log into database
client = mc("pithy.princeton.edu")
print client.admin.authenticate('lab', 'is_super', mechanism='SCRAM-SHA-1')


#Find All Distinct Core DS
dist = client.mae221.lab5_1.distinct('coreid')

print "These Photons have checked in with Big Brother:"

count = 1
for d in dist: 
    print "%i) %s" % (count,d)
    count += 1

print
#You can make, instead, a list of your coreids here
# dist = []
# dist.append('27001b000247343337373739')
# dist.append('2f002a000247343339373536')

#For each Photon
for core in dist:
    
    try:
        #Get only the data reference for that photon for the last 10 hours
        c = client.mae221.lab5_1.find(
            {'coreid':core,
             'time':{'$gt':time.time()-3600*10}
            }).sort('time',-1)
        
        #Print the time of last reading
        lr = str(dt.fromtimestamp(c[0]['time']))
        lc = c[0]['coreid']
        print "Last reading: %s from %s" %(lr,lc)
        
        #Get the history for that photon
        df = pd.DataFrame(list(c)) #Make a Dataframe
    
        #At this point, you can apply a time filter like you did all semester long and zoom in on specific times.
    
        #Make nice dates
        df['date'] = [dt.fromtimestamp(i) for i in df['time']]
    
    
        #plot analog input over time
        
        for i in range(0,6):
            reading = 'a%i' % i
            plot(df['date'],df[reading],label=reading)
        title(core)
        legend(loc="best")
        ylabel('analog value A0')
        
        #Bound the time to last 10 hours
        d1 = datetime.datetime.fromtimestamp(time.time()-3600*10)
        d2 = datetime.datetime.fromtimestamp(time.time())
        xlim([d1,d2])
    
        #Show full analog range
        ylim(0,4095)
    
        #rotate xticks    
    
        xticks(rotation='vertical')
        showme()
        clf()
    except Exception as E:
        print E
        print "Likely no data for ",core,"in the last 10 hours"
        
client.close()
