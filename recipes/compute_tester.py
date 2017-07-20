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

response=requests.get("https://api.musixmatch.com/ws/1.1/album.tracks.get?format=jsonp&callback=callback&album_id=10266231&apikey=75a92c53aece5428a5e239011843a4fd").text

data_json = response.split("(")[1].strip(");")


parsed_json = json.loads(data_json)


df=pd.io.json.json_normalize(parsed_json)


# Recipe outputs
tester = dataiku.Dataset("tester")
tester.write_with_schema(df)
