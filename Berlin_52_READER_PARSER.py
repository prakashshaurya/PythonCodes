# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 15:05:36 2022
purpose : to view and present the content of berlin52.tsp file.
dependency :tsplib95 , pandas , numpy
IDE :use spyder and variable explorer for best interpretations.
@author: shaurya
"""

import tsplib95
import pandas as pd
import numpy as np
import re
# to collect values 
values=[]
#to collect values to create column1 of dataframe
val1dict = dict()
#to collect values to create column2 of dataframe
val2dict = dict()
#input file path
filepath = 'C:/Users/shaurya/Downloads/berlin52.tsp'
problem=''
with open(filepath) as f:
    text = f.read()
    problem = tsplib95.parse(text)
def openTSP(filepath) :
    with open(filepath) as f:
        text = f.read()
        problem = tsplib95.parse(text)
        values=(text.splitlines())
        return values

def valueProvider(li):
    ss=[]
    for i in range(0,len(li)) :
         if li[i] != '' :
            ss.append(float(li[i]))         
    return ss


#create dataframe from values
def dataFrameCreator(values,val1dict,val2dict) :
    for i in range(0,len(values)) :
        ss=valueProvider(values[i].strip(' ').split(" "))
        val1dict[i]=ss[0]
        val2dict[i]=ss[1]
    data = {"VALUE1":[val1dict[i] for i in val1dict],
            "VALUE2":[val1dict[i] for i in val2dict],} 
    df= pd.DataFrame(data)
    return df

values=openTSP(filepath)
df=dataFrameCreator(values,val1dict,val2dict)
df.to_string('./Berlin52.txt',index = False)
print(df)