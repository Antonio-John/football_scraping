# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 13:10:03 2021

@author: 44752
"""

import pandas as pd
import matplotlib.pyplot as plt
from configparser import ConfigParser

df=pd.read_csv("data/transformed/swanseacitymatches.csv")

def filter_team(df, starts_with):
    
    df_filter=df[df.opposition.str.startswith(starts_with)]
    
    return df_filter

def groupby_filtered(df, col):
    
    df_groupby=df.groupby([col]).count()
    
    return df_groupby

pne=filter_team(df, "Preston North End")
print(pne.head())
#pne_groupby=groupby_filtered(pne, "result")




