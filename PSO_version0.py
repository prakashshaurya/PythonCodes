# -*- coding: utf-8 -*-
"""
Created on Sun May 29 14:42:47 2022

@author: shaurya
"""
import numpy as np
import math
import random

#constant values to be set for the velocity update and 
w=0.80
c1=.75
c2=.5

master_array =np.zeros((500,8,2),dtype="f")
master_array_fitness =np.zeros((500,8,1),dtype="f")
#define the f(x) value
f_x = np.empty([8,1],dtype='f')
#define the local_best 
l_b = np.zeros([8,2],dtype='f')
#define the global_best
g_b = np.ones([8,2],dtype='f')


#define objective function
def objective_function(x1,x2 ):
    return ((100*(x2-x1**2)**2))+(1-x1)**2


"""
populationEvaluator : 
input : array of particles , (8x2) 
output: value of particles executed over objective function ,(8x1)"""

def populationEvaluator(arr):
    f_x=np.array([objective_function(arr[i][0],arr[i][1] ) for i in np.arange(0,arr.shape[0])],dtype='f').reshape(8,1)
    return f_x

"""
findGlobalBestValue : 
input : value of particles executed over objective function ,(8x1)
output: 8x2 global best value matrix"""

def findGlobalBest(particle_x1_x2) :
    minValue = f_x.min()
    row_index=(np.where(f_x==minValue)[0][0])
    for i in range(0,f_x.shape[0]) :
        g_b[i][0]=particle_x1_x2[row_index][0]
        g_b[i][1]=particle_x1_x2[row_index][1]
    return g_b


def checkBoundsOnSwarm(arr) :
    for i in range(0,arr.shape[0]) :
        if arr[i][0]>5 :
            arr[i][0]=5
        if arr[i][0]<-5 :
            arr[i][0]=5
        if arr[i][1]>5 :
            arr[i][1]=5
        if arr[i][1]<-5 :
            arr[i][1]=-5
    return arr


def findLocalBest(master_array) :
    for i in range(0,l_b.shape[0]) :
        if master_array[0][i][0]<master_array[1][i][0]:
            l_b[i][0]=master_array[0][i][0]
        else:
            l_b[i][0]=master_array[1][i][0]
        if master_array[0][i][1]<master_array[1][i][1]:
            l_b[i][1]=master_array[0][i][1]
        else:
            l_b[i][1]=master_array[1][i][1]
    return l_b 

def populationEvaluator(arr):
    f_x=np.array([objective_function(arr[i][0],arr[i][1] ) for i in np.arange(0,arr.shape[0])],dtype='f').reshape(8,1)
    return f_x

def velocityUpdateX(v1,index,r1,r2) :
    v_2 = v1*w  + c1*r1*(l_b[index][0]-particle_x1_x2[index][0])+c2*r2*(g_b[index][0]-particle_x1_x2[index][0])

    return v_2
def velocityUpdateY(v1,index,r1,r2) :
    v_2 = v1*w  + c1*r1*(l_b[index][1]-particle_x1_x2[index][1])+c2*r2*(g_b[index][1]-particle_x1_x2[index][1])

    return v_2
#define the particle_x1_x2 swarm
x1_list =[random.uniform(-5,5) for x in np.arange(1,9,1) ]
x2_list =[random.uniform(-5,5) for x in np.arange(1,9,1) ] 
particle_x1_x2=np.array((x1_list,x2_list),dtype='f').T

#define the velocity of swarm particles
velocity_v1_v2 = np.zeros((8,2),dtype='f')

#####          generation 1           ######
#define f_x value 
f_x =  populationEvaluator(particle_x1_x2)
g_b =  findGlobalBest(particle_x1_x2)
l_b = particle_x1_x2
master_array[0]=particle_x1_x2
master_array_fitness[0]=f_x

for i in range(0,8):
    r1 = np.random.uniform(0,1)
    r2 = np.random.uniform(0,1)
    v_in_x =  velocity_v1_v2[i][0]
    v_in_y =  velocity_v1_v2[i][1]
    v_out_x =velocityUpdateX(v_in_x,i,r1,r2) 
    v_out_y =velocityUpdateY(v_in_y,i,r1,r2) 
    x_out = particle_x1_x2[i][0] + v_out_x
    y_out = particle_x1_x2[i][1] + v_out_y
    particle_x1_x2[i][0]=x_out
    particle_x1_x2[i][1]=y_out
    velocity_v1_v2[i][0]=v_out_x
    velocity_v1_v2[i][1]=v_out_y

particle_x1_x2 = checkBoundsOnSwarm(particle_x1_x2)
master_array[1]=particle_x1_x2

########## generation 2 #################
for j in range(0,500):
    f_x =  populationEvaluator(particle_x1_x2)
    g_b =  findGlobalBest(particle_x1_x2)
    l_b =  findLocalBest(master_array)
    master_array[j]=particle_x1_x2
    master_array_fitness[j]=f_x
    
    for i in range(0,8):
        r1 = np.random.uniform(0,1)
        r2 = np.random.uniform(0,1)
        v_in_x =  velocity_v1_v2[i][0]
        v_in_y =  velocity_v1_v2[i][1]
        v_out_x =velocityUpdateX(v_in_x,i,r1,r2) 
        v_out_y =velocityUpdateY(v_in_y,i,r1,r2) 
        x_out = particle_x1_x2[i][0] + v_out_x
        y_out = particle_x1_x2[i][1] + v_out_y
        particle_x1_x2[i][0]=x_out
        particle_x1_x2[i][1]=y_out
        velocity_v1_v2[i][0]=v_out_x
        velocity_v1_v2[i][1]=v_out_y
    
    particle_x1_x2 = checkBoundsOnSwarm(particle_x1_x2)
    master_array[j]=particle_x1_x2
    ##### draw graph     ########

import matplotlib.pyplot as plt
x = master_array[0][:,0]
y = master_array[0][:,1]


# plt.scatter(x, y, c="r", alpha=0.5, marker=r'$\clubsuit$',
#             label="Luck")
# plt.xlabel("Leprechauns")
# plt.ylabel("Gold")
# plt.legend(loc='upper left')


# x = master_array[5][:,0]
# y = master_array[5][:,1]
# plt.scatter(x, y, c="g", alpha=0.5, marker=r'$\clubsuit$',
#             label="Luck")
# plt.xlabel("Leprechauns")
# plt.ylabel("Gold")
# plt.legend(loc='upper left')
# plt.savefig( 'd:/saved_figure'+str(5)+'.png')
# x = master_array[10][:,0]
# y = master_array[10][:,1]
# plt.scatter(x, y, c="b", alpha=0.5, marker=r'$\clubsuit$',
#             label="Luck")
# plt.xlabel("Leprechauns")
# plt.ylabel("Gold")
# plt.legend(loc='upper left')
# plt.savefig( 'd:/saved_figure'+str(10)+'.png')
# x = master_array[15][:,0]
# y = master_array[15][:,1]
# plt.scatter(x, y, c="peru", alpha=0.5, marker=r'$\clubsuit$',
#             label="Luck")
# plt.xlabel("Leprechauns")
# plt.ylabel("Gold")
# plt.legend(loc='upper left')
# plt.savefig( 'd:/saved_figure'+str(15)+'.png')
# x = master_array[20][:,0]
# y = master_array[20][:,1]
# plt.scatter(x, y, c="y", alpha=0.5, marker=r'$\clubsuit$',
#             label="Luck")
# plt.xlabel("Leprechauns")
# plt.ylabel("Gold")
# plt.legend(loc='upper left')
# plt.savefig( 'd:/saved_figure'+str(20)+'.png')

# x = master_array[25][:,0]
# y = master_array[25][:,1]
# plt.scatter(x, y, c="c", alpha=0.5, marker=r'$\clubsuit$',
#             label="Luck")
# plt.xlabel("Leprechauns")
# plt.ylabel("Gold")
# plt.legend(loc='upper left')
# plt.savefig( 'd:/saved_figure'+str(25)+'.png')

# x = master_array[30][:,0]
# y = master_array[30][:,1]

# plt.scatter(x, y, c="m", alpha=0.5, marker=r'$\clubsuit$',
#             label="Luck")
# plt.xlabel("Leprechauns")
# plt.ylabel("Gold")
# plt.legend(loc='upper left')
# plt.savefig( 'd:/saved_figure'+str(30)+'.png')

# x = master_array[35][:,0]
# y = master_array[35][:,1]

# plt.scatter(x, y, c="k", alpha=0.5, marker=r'$\clubsuit$',
#             label="Luck")
# plt.xlabel("Leprechauns")
# plt.ylabel("Gold")
# plt.legend(loc='upper left')
# plt.savefig( 'd:/saved_figure'+str(35)+'.png')

# x = master_array[100][:,0]
# y = master_array[100][:,1]

# plt.scatter(x, y, c="lime", alpha=0.5, marker=r'$\clubsuit$',
#             label="Luck")
# plt.xlabel("Leprechauns")
# plt.ylabel("Gold")
# plt.legend(loc='upper left')
# plt.savefig( 'd:/saved_figure'+str(40)+'.png')


x = master_array[499][:,0]
y = master_array[499][:,1]

plt.scatter(x, y, c="darkred", alpha=0.5, marker=r'$\clubsuit$',
            label="Luck")
plt.xlabel("Leprechauns")
plt.ylabel("Gold")
plt.legend(loc='upper left')
plt.savefig( 'd:/saved_figure'+str(45)+'.png')

