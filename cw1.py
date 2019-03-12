# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 12:34:16 2019

@author: Marcin Niemyjski
"""


import numpy as np
import matplotlib.pyplot as plt
data = np.array([np.sin(4*x+1)+np.cos(x+5) for x in np.linspace(0,50,1000)])
year = np.array([1000+x for x in range(data.size)])

plt.figure(figsize=(10, 10))
plt.plot(year, data)
plt.ylabel('rok')
plt.xlabel('data')
plt.savefig('wykres')
plt.show()

np.min(data)
np.std(data)
np.var(data)
np.sum(data)
np.mean(data)
lol=[]
#for counter, value in enumerate(data):
#    if counter/20 is int:
#        lol.append(value)

data2 = np.split(data,10)
year2 = np.split(year, 10)

#B=A[:2,:2].copy()

#plik tekstowy
x=[]
y=[]
e=[]

try: 
    data4 = open('dane10.csv', 'r')
except:
    sys.exit('cannot find file')

with data:    
    try:
        x.append(data[:1])
        y.append(data[2:3])
        e.append(data[4:5])
except
    sys.exit('cannot create lists')