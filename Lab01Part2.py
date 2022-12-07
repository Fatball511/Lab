#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 23:48:00 2022

@author: Ho Hang Cheng SID: 210058323
"""

import numpy as np
import matplotlib as plt

x= np.arange(5,16)
print(x)
y = np.linspace(0,23,7)
print(y)

z = np.random.uniform(-1,1,100)
plt.pyplot.hist(z,bins=15)

a = np.random.randint(1,50,10)
b = np.random.randint(1,50,10)

temp = a - b
dist = np.sqrt(np.sum(np.square(temp)))

print('the Euclidean distance between the arrays is '+str(dist))


