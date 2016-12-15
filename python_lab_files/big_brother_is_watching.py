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
# dist.append('1b0033000847343432313031')
# dist.append('24003a000247353138383138')

#For each Photon
for core in dist:
    #Get only the data reference for that photon
    c = client.mae221.lab5_1.find({'coreid':core}).sort('time',-1)
    
    #Print the time of last reading
    lr = str(dt.fromtimestamp(c[0]['time']-5*3600))
    lc = c[0]['coreid']
    print "Last reading: %s from %s" %(lr,lc)
    
    #Get the history for that photon
    df = pd.DataFrame(list(c)) #Make a Dataframe

    #At this point, you can apply a time filter like you did all semester long and zoom in on specific times.

    #Make nice dates
    df['date'] = [dt.fromtimestamp(i) for i in df['time']]


    #plot analog input over time
    
    for i in range(0,6):
        plot(df['date'],df['a%i' % i],'.')
    title(core)
    ylabel('analog value A0')
    
    #Bound the time to december    
    xlim([datetime.date(2016, 12, 1), datetime.date(2016, 12, 30)])

    #Show full analog range
    ylim(0,4095)

    #rotate xticks    

    xticks(rotation='vertical')
    showme()
    clf()
