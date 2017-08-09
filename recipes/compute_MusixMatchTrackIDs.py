# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from IPython.display import display
import datetime
from dateutil.parser import parse

with open("/Users/seanhanlon/Downloads/mxm_779k_matches.txt") as file:
    lines = []
    for line in file:
        # The rstrip method gets rid of the "\n" at the end of each line
        lines.append(line.rstrip().split(","))
        
#create dataframe from dataset that maps the Million Song Database with the MusixMatch repository
mxmdata=pd.DataFrame(lines)
mxmdata=mxmdata[mxmdata.index>17]

#Create dataset with metadata that spills over to multiple columns
spillrows=pd.DataFrame()
for i in range(1,len(mxmdata.columns)):
    spillrows=spillrows.append(mxmdata[mxmdata[i].notnull()])
    
#Remove duplicated records (some rows were duplicated in the procedure above)
spillrows['index'] = spillrows.index
spillrows= spillrows.drop_duplicates(subset='index')
spillrows= spillrows.drop('index', axis =1)

#split the text string in the first column into multiple columns
mxmdata=pd.DataFrame(mxmdata[0].str.split('<SEP>'))

# mxmdata.to_dict()
mxmdata=mxmdata[0].apply(pd.Series)

# rename the columns 
mxmdata=mxmdata.rename(columns={0: 'msd_trackid',\
                                      1: 'msd_artist',\
                                      2: 'msd_title',\
                                      3: 'mxm_trackid',\
                                      4: 'mxm_artist',\
                                      5: 'mxm_title'})

#create a merge data set with all of the additional variable fields, and remove the first column since I opened that column in the cell above
spillrows=spillrows.drop([0],1)
for i in range(0,len(spillrows.columns)+1):
    spillrows=spillrows.rename(columns={i: 'spillover'+str(sum(i+len(mxmdata.columns)-1))})

# Merge the overflow rows onto the dataset where the music text is split:
mxmdata=pd.concat([mxmdata, spillrows], axis=1)

# Recipe outputs
musixMatchTrackIDs = dataiku.Dataset("MusixMatchTrackIDs")
musixMatchTrackIDs.write_with_schema(mxmdata)