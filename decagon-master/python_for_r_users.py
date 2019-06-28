#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:20:22 2019

@author: shujunhuang
"""

import os
import numpy as np
import pandas as pd

os.getcwd()
os.listdir()

A = np.random.randn(6, 4)
df = pd.DataFrame(A)
### Using pandas package
# returns the name of the rows
df.index
# returns the name of the columns
df.columns
# returns top x rows of data frame
df.head(3)
df.tail(4)
df.shape
len(df)
df.index = ["A", "B", "C", "D", "E", "F"]
df.columns = ["p", "e", "g", "x"]
df.describe

import matplotlib.pyplot as plt 
x = range(100)

y = [val**2 for val in x]
plt.plot(x, y)

fig, axes = plt.subplots(nrows = 1, ncols = 2)
for ax in axes:
    ax.plot(x, y, "r")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("title")
fig.tight_layout()
dir()
!ls
!pwd
%cd ..
!ls
%cd ./Manu-python

import pandas as pd
import numpy as np

df = pd.read_csv("test_data1.csv", encoding = 'gbk', skiprows = 1)
df.head(3)
pd.read_csv("test_data1.csv", delimiter = ',')

f = open("test_data1.csv","r")
f.readlines()