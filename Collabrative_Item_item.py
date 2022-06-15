# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 16:27:44 2022

@author: shaurya
"""
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse
import pandas as pd

#put nan for missing values
arr_blanks = np.array([[2,5,np.nan,4,3,5],
                                 [4,3,4,2,np.nan,3],
                                 [3,5,2,5,4,4],
                                 [5,3,5,np.nan,1,1],
                                 [4,3,4,3,1,5],
                                 [2,4,3,4,5,1]],dtype="float")
rating_arr=arr_blanks.copy()
#evaluate mean without counting missing values   
def meanCalculator(arr) :
    count=0;
    sum=0;
    for i in range(0,arr.shape[0]) :
        if not np.isnan(arr[i]) :
             count+=1
             sum+=arr[i]
             print(arr[i])
    return sum/count


#remove nan by putting 0.0
def nanRemover(arr):
    for i in range(0,arr.shape[0]) :
        for j in range(0,arr.shape[1]) :
            if np.isnan(arr[i][j]) :
                arr[i][j]=0.0
    return arr

#sorts in ascending order
def topNSelector(arr):
    arr=np.sort(arr, axis=-1, kind='mergesort', order=None)
    return (np.flip(arr)[0],np.flip(arr)[1],np.flip(arr)[2],np.flip(arr)[3])


for i in range(0,arr_blanks.shape[0]) :
    arr_blanks[i] = arr_blanks[i]-meanCalculator(arr_blanks[i])
    

nan_removed_norm_array = nanRemover(arr_blanks)
sparse_normalized = sparse.csr_matrix(nan_removed_norm_array)
similarities = np.round(cosine_similarity(sparse_normalized.transpose()),decimals=2)
print('pairwise dense output:\n {}\n'.format(similarities))



movies_movies =pd.DataFrame(similarities,columns=['Home_Alone','Witness','Untouchables','Mousehunt','Witch','Matrix'],index=['Home_Alone','Witness','Untouchables','Mousehunt','Witch','Matrix'])
user_movies =pd.DataFrame(rating_arr,index=['lalita','vaikunth','hari','ruchika','aparajita','ravi'],columns=['Home_Alone','Witness','Untouchables','Mousehunt','Witch','Matrix'])

#prediction ? 


