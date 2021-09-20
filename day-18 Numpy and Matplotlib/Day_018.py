#-------------------------------
"""
data with one feature called univariate 
data with more than one feature called multivariate
numpy : 
    numerical python 
    math operation - fast 
matplotlib:
    for data visulization(graphs)
    mother of seaborn 
"""
#-------------------------------

list1 = [1,2,3,4,5,6,7,8,9,10]

list1*10 #10 times repetition

list1 = [0]*10 #list with 10 zeros 

list2 = []
for item in list1:
    list2.append (item*10)
    
[item*10 for item in list1]
"""
using loop for large amount of data is not advisable 
because of time compexity 
so we need numpy for that and it is fast because of vectorization 
ndarray = n d array , n=number , d= dimension 
to check version of numpy : np.__version__

"""
list1 = [1,2,3,4,5,6,7,8,9,10]

import numpy as np

x = np.array(list1) #convert list to ndarray
#each item in array will store in 64 bit bydefault but we can change this size 
#df.values : represent all the data in nd list
#df.values -> ndarray

x.shape 
x.ndim #1

y = 10 #scaler value

y = np.array(y)
y.shape #()
y.ndim  #0

y = [10] #1D

y = np.array(y)

y.shape #(1,)
y.ndim #1

y = [[10]] #2D

y = np.array(y)
y.shape #(1,1)
y.ndim #2

list1 = [1,2,3,4,5,6,7,8,9]

x = np.array(list1)
x = x.reshape(3,3) #it will convert list to 3x3 array
x=np.arange(5) #it will creat array of 5 intergers
x = np.arange(5, dtype = np.int32) #data size will be 32 bit 
#in ones and zeros all the data will be in float type 
#reduction in size 64 bit to 32 bit may lose the data 
np.ones((3,4), dtype = np.int8)

np.zeros((2,4))
#----------------------------------------------
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,2,3,4,5]

plt.scatter(x,y)
plt.plot(x,y)

x =  np.arange(20)
y = [item**3 for item in x] 

plt.scatter(x,y)

plt.plot(x,y)

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
branchnames = ('CSE', 'ECE', 'IT', 'EE')
sizes = [10, 5, 5, 2]
apart = (0, 0, 0, 0.1)  # only "explode" the 4th slice (i.e. 'EE')


plt.pie(sizes, explode=apart ,labels=branchnames, autopct='%.2f%%')

plt.show()



