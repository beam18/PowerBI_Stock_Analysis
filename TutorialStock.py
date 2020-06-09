# -*- coding: utf-8 -*-
"""
Created on Thu May 14 13:57:54 2020

@author: kittipong.neamchalon
"""

import pandas as pd
from pandas_datareader import data

s = ["SCC","SCB","SAWAD","RATCH","PTTGC","PTTEP","PTT"]

stocks = list(map(lambda e: e+'.bk',s))

df = data.DataReader(stocks, data_source="yahoo", start="2020-01-01")

ds = df.stack().reset_index()

ds