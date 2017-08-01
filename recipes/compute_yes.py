# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Recipe inputs

billboardsort = dataiku.Dataset("billboardsort")
billboardsort_df = billboardsort.get_dataframe()

# Recipe outputs
yes = dataiku.Dataset("yes")
yes.write_with_schema(pandas_dataframe)
