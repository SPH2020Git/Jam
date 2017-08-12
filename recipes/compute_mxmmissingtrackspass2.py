# -*- coding: utf-8 -*-
import dataiku
import json
import requests
import pandas as pd
import flatten_json
from flatten_json import flatten
from pandas.io.json import json_normalize
import gzip
from IPython.display import display
import grequests
import ast
import matplotlib


# Recipe inputs

df = dataiku.Dataset("mxmtrackidsmissingforapi")
missingtracks = df.get_dataframe()

artistslist=missingtracks['artist_simplified'].tolist()
songslist=missingtracks['song_simplified'].tolist()

thekey="75a92c53aece5428a5e239011843a4fd"
thetracks=pd.DataFrame()
for idx, val in enumerate(songslist):
        if idx<1001:
            theartist='"'+artistslist[idx]+'"'
            thetitle='"'+songslist[idx]+'"'
            print(theartist+thetitle)
            response=requests.get("https://api.musixmatch.com/ws/1.1/matcher.track.get?format=jsonp&callback=callback&q_artist="+theartist+"&q_track="+thetitle+"&apikey="+thekey).text
            responseclean = response.split("(")[1].strip(");")
            if responseclean[-1]!="}":
                continue
            data_json = json.loads(responseclean)
            parsed_json=pd.io.json.json_normalize(data_json)
            thetracks=thetracks.append(parsed_json)

# Recipe outputs
mxmmissingtrackspass2 = dataiku.Dataset("mxmmissingtrackspass2")
mxmmissingtrackspass2.write_with_schema(thetracks)
