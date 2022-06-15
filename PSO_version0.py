# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 22:44:45 2022

@author: shaurya
"""
import numpy as np
import math
import random
import matplotlib.pyplot as plt

#Global Variables 
particle_size =10
c1=1.5
c2=2.0
w=.75
iterations = 500
fitness_value = np.zeros((iterations,particle_size,1))
global_best_value = np.zeros((iterations,particle_size,2))
local_best_value = np.zeros((iterations,particle_size,2))
position = np.zeros((iterations,particle_size,2))
velocity = np.zeros((iterations,particle_size,2))
lower_bound=-5
upper_bound= 5

"""
objective_function : 
input : position of particles ,  
output: fitness value
"""
def objective_function(x1,x2):
    return ((100*(x2-x1**2)**2))+(1-x1)**2
"""
populationEvaluator : 
input : array of particles , (8x2) 
output: value of particles executed over objective function ,(8x1)"""

def populationEvaluator(arr):
    f_x=np.array([objective_function(arr[i][0],arr[i][1] ) for i in np.arange(0,arr.shape[0])],dtype='f').reshape(particle_size,1)
    return f_x

"""find global min value """
def findGLobalBestParticle(arr,i):
   min_value = fitness_value[i].min()
   row_index=(np.where(fitness_value[i]==min_value))
   best_fit_row =row_index[0][0]
   return(position[i][best_fit_row][0],position[i][best_fit_row][1])
"""
checkBoundsOnSwarm : 
input : paricle array
output: restores if value to permissble ranges
"""
def checkBoundsOnSwarm(arr) :
    for i in range(0,arr.shape[0]) :
        if arr[i][0]>upper_bound :
            arr[i][0]=upper_bound
        if arr[i][0]<lower_bound :
            arr[i][0]=lower_bound
        if arr[i][1]>upper_bound :
            arr[i][1]=upper_bound
        if arr[i][1]<lower_bound :
            arr[i][1]=lower_bound
    return arr

def findLocalBestParticle (previous,next,local_best,fitness_array):
    for i in range(0,previous.shape[0]):
        if fitness_array[i]>=fitness_array[i+1] :
            local_best[i][0] =next[i][0]
            local_best[i][1] =next[i][1]
        else :
            local_best[i][0] =next[i][0]
            local_best[i][1] =next[i][1]
    return local_best
    
#########################Initialization of Swarm #############################


""" intialize position for starting i.i. first value in the tensor 
should have random values in[-5,5] and [-5,5] ,initial velocity (0,0)
"""

for i in range(0,particle_size):
    for j in range(0,2):
        position[0][i][0] = np.random.uniform(-5,5)
        position[0][i][1] = np.random.uniform(-5,5)
        
velocity[0][0]=0.0
fitness_value[0] = populationEvaluator(position[0])
global_best = findGLobalBestParticle(position[0],0)
global_best_value[0]=global_best
local_best_value[0]=position[0]
r1=np.random.uniform(0,1)
r2=np.random.uniform(0,1)
#velocity update
for i in range(0,particle_size):
    velocity[1][i][0] = w*velocity[0][i][0] + c1*r1*(local_best_value[0][i][0]-position[0][i][0]) + c2*r2*(global_best_value[0][i][0]-position[0][i][0])  
    velocity[1][i][1] = w*velocity[0][i][1] + c1*r1*(local_best_value[0][i][1]-position[0][i][1]) + c2*r2*(global_best_value[0][i][1]-position[0][i][1])  
#position update
for i in range(0,particle_size):
    position[1][i][0] = velocity[1][i][0] +position[0][i][0]
    position[1][i][1] = velocity[1][i][1] +position[0][i][1]
checkBoundsOnSwarm(position[1])     




fitness_value[1] = populationEvaluator(position[1])
global_best = findGLobalBestParticle(position[1],1)
global_best_value[1]=global_best
print(global_best)
r1=np.random.uniform(0,1)
r2=np.random.uniform(0,1) 
for j in range(0,particle_size) :
    if fitness_value[1][j][0] < fitness_value[0][j][0]:
        local_best_value[1][j][0]= position[1][j][0]
        local_best_value[1][j][1]= position[1][j][1]
    if fitness_value[1][j][0] >= fitness_value[0][j][0]:
        local_best_value[1][j][0]= position[0][j][0]
        local_best_value[1][j][1]= position[0][j][1]
#velocity update
for i in range(0,particle_size):
    velocity[2][i][0] = w*velocity[1][i][0] + c1*r1*(local_best_value[1][i][0]-position[1][i][0]) + c2*r2*(global_best_value[1][i][0]-position[1][i][0])  
    velocity[2][i][1] = w*velocity[1][i][1] + c1*r1*(local_best_value[1][i][1]-position[1][i][1]) + c2*r2*(global_best_value[1][i][1]-position[1][i][1])  
#position update
for i in range(0,particle_size):
    position[2][i][0] = velocity[2][i][0] +position[1][i][0]
    position[2][i][1] = velocity[2][i][1] +position[1][i][1]
checkBoundsOnSwarm(position[2]) 

### iteration 2 to upwards #########

for k in range(2,iterations-1) :
    fitness_value[k] = populationEvaluator(position[k])
    global_best = findGLobalBestParticle(position[k],k)
    global_best_value[k]=global_best
    print(global_best)
    r1=np.random.uniform(0,1)
    r2=np.random.uniform(0,1) 
    for j in range(0,particle_size) :
        if fitness_value[k][j][0] < fitness_value[k-1][j][0]:
            local_best_value[k][j][0]= position[k][j][0]
            local_best_value[k][j][1]= position[k][j][1]
        if fitness_value[k][j][0] >= fitness_value[k-1][j][0]:
            local_best_value[k][j][0]= position[k-1][j][0]
            local_best_value[k][j][1]= position[k-1][j][1]
    #velocity update
    for i in range(0,particle_size):
        velocity[k+1][i][0] = w*velocity[k][i][0] + c1*r1*(local_best_value[k][i][0]-position[k][i][0]) + c2*r2*(global_best_value[k][i][0]-position[k][i][0])  
        velocity[k+1][i][1] = w*velocity[k][i][1] + c1*r1*(local_best_value[k][i][1]-position[k][i][1]) + c2*r2*(global_best_value[k][i][1]-position[k][i][1])  
    #position update
    for i in range(0,particle_size):
        position[k+1][i][0] = velocity[k+1][i][0] +position[1][i][0]
        position[k+1][i][1] = velocity[k+1][i][1] +position[1][i][1]
    checkBoundsOnSwarm(position[2]) 
    

x= []    
y= []
z= []
for i in range (0,iterations):
     for j in range(0,particle_size) :
         x.append(position[i][j][0].tolist())
for i in range (0,iterations):
     for j in range(0,particle_size) :
         y.append(position[i][j][1].tolist())
for i in range (0,iterations):
     for j in range(0,particle_size) :
         z.append(fitness_value[i][j][0].tolist())
fig = plt.figure()
ax = plt.axes(projection='3d')
for i in range(0,499):
    for j in range(0,9):
        ax.scatter3D(x[i*10+j],y[i*10+j], z[10*i+j], c=z[10*i+j], cmap='cividis');
        plt.savefig("D:\Images"+("im"+str(i)+'_'+str(j)+".jpg"))