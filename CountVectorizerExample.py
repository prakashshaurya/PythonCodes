# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 21:42:31 2022

@author: shaurya

To learn CountVectorizer functionality
"""
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity 
#####  define documents ######
document = ["This is the first document.","This document is the second document.","And this is the third one.","Is this the first document?",]
tf_idf_vectorizer = TfidfVectorizer()
tf_idf_sparse=tf_idf_vectorizer.fit_transform(document)
tf_idf_dense = tf_idf_sparse.todense()


##### QUERY VECTOR PROCESSING #######
vectorizer = CountVectorizer()
##### create sparse matrix #######
sparse_matrix = vectorizer.fit_transform(document)
##### transform sparse matrix to dense array #######
dense_array=(sparse_matrix.toarray())
##### represent as dataframe #####
df= pd.DataFrame(dense_array,columns=vectorizer.get_feature_names_out())
##### define idf array #####
idf = np.zeros((dense_array.shape[1],1))
#####define idf array ######
doc_number = dense_array.shape[0]
term_number = dense_array.shape[1]
def termFrequencyAdder(arr):
    """
    purpose : to evaluate idf array

    Parameters
    ----------
    arr : dense matrix which comes from tansforming vectorizer generated sparse matrix

    Returns
    -------
    idf : returns numpy array of idf

    """
    for j in range(0,arr.shape[1]) :
        sum =0
        for i in range(0,arr.shape[0]) :
            if arr[i][j]>0 :
              sum+=1
        idf[j]=np.log2(doc_number/sum)
    return idf

idf = termFrequencyAdder(dense_array)
idf_df = pd.DataFrame(idf,index=vectorizer.get_feature_names_out())

query = "third document"
query_vectorizer = CountVectorizer()
query_Sparse = query_vectorizer.fit_transform([query])
query_dense = query_Sparse.toarray()
query_df = pd.DataFrame(query_dense,columns=query_vectorizer.get_feature_names_out())
query_vector = pd.DataFrame(np.zeros((1,term_number)),columns=tf_idf_vectorizer.get_feature_names_out())

for i in query_df.columns :
    query_vector[i] = query_df[i]
    
query_array_tfidf =np.zeros((1,term_number))

for i in range(0,query_array_tfidf.shape[0]) :
    for j in range(0,query_array_tfidf.shape[1]) :
        print(i,j)
        query_array_tfidf[i][j] = np.array(query_vector)[i][j]*np.array(idf_df).T[i][j]

document_suggestion = cosine_similarity(query_array_tfidf,tf_idf_dense)
document_suggestion_dataframe = pd.DataFrame(np.array(document_suggestion),columns=['d1','d2','d3','d4'])
rslt_df = document_suggestion_dataframe.sort_values(by = 0, axis = 1,ascending = False)
