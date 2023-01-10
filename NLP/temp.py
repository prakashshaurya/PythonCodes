# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import conllu
import pyconll
import re

#open file
file = open("C:/Users/shaurya/Desktop/hi-train.txt" , "r",encoding="utf8")

#read data
text = file.read()

#split data by new line
data = text.split("\n")

#define sentence container 
sentences =[]
keyList =[]

def keyIsolator(str)  :
        p = re.compile(r"^#.*domain=hi$") #return list containing single string
        str= p.findall(str)[0]          #collecting string from list
        key = str.split()[2]
        return key

def keyDetector(str) :
    return bool(re.search(r"^#.*domain=hi$", str) )


def keyListMaker(str,keyList):
       if keyDetector(str) :
            keyList.append([keyIsolator(str)]) 
            


def removeEmptyString(data,sentences):
    for i in range(0,len(data)-1) :
        if len(data[i])>0 :
           sentences.append(data[i]) 
    return sentences

def mapMaker(str):
    return str.split("_ _")

def csvWriter(keyList,MapKey,MapValue) :
   pass
########################### preprocessing task ################################

sentences =   removeEmptyString(data,sentences)
MapKey=[]
MapValue=[]
 
   
    
tempMapValue =[]
tempMapKey=[]

for i in range(0, len(sentences)):
    if keyDetector(sentences[i]) :
        if len(tempMapKey)>0 :
            MapKey.append([tempMapKey[i] for i in range(0,len(tempMapKey)-1)])
        tempMapKey.clear()
        if len(tempMapValue)>0 :
            MapValue.append([tempMapValue[i] for i in range(0,len(tempMapValue)-1)])
        tempMapValue.clear()
        keyListMaker(sentences[i],keyList)
    else :
        tempMapKey.append(mapMaker(sentences[i])[0])
        tempMapValue.append(mapMaker(sentences[i])[1])
        
##########3merge final string#############################        

MapKey.append([tempMapKey[i] for i in range(0,len(tempMapKey)-1)])       
MapValue.append([tempMapValue[i] for i in range(0,len(tempMapValue)-1)])

csvWriter(keyList,MapKey,MapValue) 

         
