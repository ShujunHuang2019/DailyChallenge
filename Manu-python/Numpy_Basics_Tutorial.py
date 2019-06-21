##### N-dimensional Array
import numpy as np
scores = [87, 34.4, 34, 45]
first_arr = np.array(scores)
print(first_arr)
print(first_arr.dtype)

scores_1 = [[1, 3, 4, 4], [2, 5, 6, 6]]
second_arr = np.array(scores_1)
print(second_arr)
print(second_arr.dtype)
print(second_arr.ndim)
print(second_arr.shape)

x = np.zeros(10)
x
print(np.zeros((2, 3)))

np.arange(15)
np.eye(4)

print(first_arr)
print(first_arr * first_arr)
print(first_arr - first_arr)
print(1/first_arr)
print(first_arr ** 0.5)


##### Indexing and Slincing
new_arr = np.arange(12)
print(new_arr)
print(new_arr[5])
print(new_arr[4:9])
new_arr[4:9] = 99
print(new_arr)


modi_arr = new_arr[4:9]
modi_arr
new_arr
modi_arr[1] = 12323


matrix_arr = np.array([[3, 4, 4], [4, 5, 5], [3, 5, 5]])
matrix_arr
matrix_arr[1]
matrix_arr[1][1]
matrix_arr[1, 1]
matrix_arr[0][2]
matrix_arr[0, 2]

from IPython.display import Image
i = Image(filename = "pheeno_and_anna.jpg")
i

personals = np.array(["a", "a", "b", "c"])
print(personals == "a")

from numpy import random
random_no = random.randn(7, 4)
print(random_no)
random_no[personals == 'a']

from numpy import random
algebra = random.randn(2, 3)
algebra

algebra[[0, 1]]

fancy = np.arange(36).reshape(9, 4)
fancy
fancy[[1,4,3,2],[3,2,1,0]]
fancy[[1, 4, 8, 2]]
fancy[[1, 4, 8, 2]][:, [0, 3, 1, 2]]

mtrices =np.arange(-5,5,1)
mtrices

x, y = np.meshgrid(mtrices, mtrices)
x, y

print "Matrix values of y: {}".format(y)


x1= np.array([1,2,3,4,5])
y1 = np.array([6,7,8,9,10])
cond =[True, False, True, True, False]

zip(x1, y1, cond)

z1 = [(x, y, z) for x, y, z in zip(x1, y1, cond)]
z1
np.where(cond, x1, y1)


ra = np.random.randn(5, 4)
print(ra)

print(np.where(ra > 0, 1, -1))
print(np.where(ra > 0, 1, ra))

no = np.arange(5)
no = np.array(no)
no
np.sqrt(no)
np.exp(no)
np.maximum(no)
np.maximum([4, 5, 5],[3, 4, 6])
no.var()
no.std()
no.min()

np.argmax(no)
np.argmin(no)


funky = np.arange(8)
print np.sqrt(funky)
print np.exp(funky)


thie = np.random.randn(5,5)
thie.mean()
thie.max()
no.max()
np.mean(thie)

jp = np.arange(10).reshape(5, 2)
print(jp)
print("the array are: {}".format(jp))

jp.sum()
jp.mean()
jp.cumsum()
print(jp.cumsum(0))
jp.cumsum(1)

print((jp > 5).sum())
print((jp < 5).sum())
test = np.array([True, False, False, True, False, True]).reshape(3, 2)
test
print(test.any())
print(test.all())


lp = np.random.randn(3, 4)
print(lp)
print(np.argmax(lp))
print(np.argmin(lp))
lp.sort(0)
lp

np.unique(personals)
set(personals)
