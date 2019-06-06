import numpy as np, pandas as pd

arr1 = np.arange(10)
arr1
type(arr1)

s1 = pd.Series(arr1)
s1
type(s1)

dic1 = {"a": 10, "b": 20, "c": 30, "d":40, "e":50}
dic1
type(dic1)

s2 = pd.Series(dic1)
s2
type(s2)


arr2 = np.array(np.arange(12)).reshape(4, 3)
type(arr2)


df1 = pd.DataFrame(arr2)
type(df1)


dic2 = {"a": [1, 2, 3, 4], "b": [5, 6, 7, 8], 
"c": [9, 10 , 11, 12], "d": [13, 14, 15, 16]}
type(dic2)

df2 = pd.DataFrame(dic2)
type(df2)

dic3 = {'one':{'a':1,'b':2,'c':3,'d':4},
'two':{'a':5,'b':6,'c':7,'d':8},
'three':{'a':9,'b':10,'c':11,'d':12}}

df3 = pd.DataFrame(dic3)


df4 = df3[["one", "three"]]
s3 = df3["one"]


s4 = pd.Series(np.array([1, 2, 3, 4, 5, 6, 7]))
s4.index

s4.index = ["a", "b", "c", "d", "e", "f", "g"]

s5 = pd.Series(np.array([10, 13, 12, 19, 30, 40, 50]))
s5.index = ["a", "b", "c", "d", "e", "f", "g"]

s6 = pd.Series(np.array([14, 16, 40, 59, 30, 90, 58]))
s6.index = ["a", "c", "i", "b", "d", "f", "h"]


student = pd.read_csv('student.csv')
