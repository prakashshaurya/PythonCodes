# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 15:45:40 2022

@author: shaurya
"""
import tsplib95
import pandas as pd
import numpy as np
import re
filepath = 'C:/Users/shaurya/Downloads/att532-5.csp2'
problem=''
values =[]
val1dict = dict()
val2dict = dict()
with open(filepath) as f:
    text = f.read()
    problem = tsplib95.parse(text)
    values=text.split("\n")
    
#input : list of string ,output list of integers
def valueProviderInt(li):
    ss=[]
    for i in range(0,len(li)) :
          if li[i] != '' :
            ss.append(int(li[i]))         
    return ss

#input : list of string ,output list of strings
def valueProviderStr(li):
    ss=[]
    for i in range(0,len(li)) :
          if li[i] != '' :
            ss.append((li[i]))         
    return ss



    #create dataframe from values
def dataFrameCreator1(values,val1dict) :
    for i in range(4,535) :
        ss=valueProviderInt(values[i].strip(' ').split(" "))
        val1dict[i]=ss
        data = {"DISTANCE MATRIX":[val1dict[i] for i in val1dict]} 
        df= pd.DataFrame(data)
    return df
df1=dataFrameCreator1(values,val1dict)

def dataFrameCreator2(values,val2dict) :
    for i in range(537,1068) :
        ss=valueProviderInt(values[i].strip(' ').split(" "))
        val2dict[i]=ss
        data = {"COVERAGE":[val2dict[i] for i in val2dict]} 
        df= pd.DataFrame(data)
    return df
df2=dataFrameCreator2(values,val2dict)

df1.to_string('./att_df1.txt',index = False)
df2.to_string('./att_df2.txt',index = False)