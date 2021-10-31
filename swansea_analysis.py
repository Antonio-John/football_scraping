# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 13:10:03 2021

@author: 44752
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("swanseacitymatches.txt")

def filter_team(df, team):
    
    df_filter=df[df["opposition"]==team]
    
    return df_filter

def groupby_filtered(df, col):
    
    df_groupby=df.groupby([col]).count()
    
    return df_groupby

pne=filter_team(df, "Preston North End")
pne_groupby=groupby_filtered(pne, "result")




