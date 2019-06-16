print "Big data examiner"

a = "Big data"
print(type(a))

b = "examiner"
print type(b)

c = 4.5
print(type(c))

print(isinstance(a, str))
print(isinstance(a, int))
print(isinstance(a, (int, float)))
print(isinstance(c, (int, float)))


a = "Bill gates"
a.tab()

import numpy as np
data_new = [6, 7.5, 7, 9]
data = np.array(data_new)
data

x = [1, 2, 3, 4]
y = x
z = list(x)
print(x is y)
print(x is not z)

programming = ["Python", "R", "Java", "Php"]
print(programming)
programming[2] = "c++"
print(programming)

z_tuple = (9, 3, 4)
z_tuple[1] = "twenty two"

"""
Hi!
Learn Python it is fun!
Data science and machine learning are amazing!
"""

x = "This is big ata examiner"
print(len(x))
x[10] = "f"

x = "Java is a powerful programming language"
y = x.replace("Java", "Python")
print(x)
print(y)

x = 4562
y = str(x)
print(x)
print(y)
print(type(x))
print(type(y))

a = "Python"
print(list(a))
print(a[:3])
print(a[3:])

p = "P is the best programming language"
q = ", I have ever seen"
z = p + q
print(z)

print("Hii space left is just %.3f gb, and the data base is %s" %(0.98, "mysql"))
print("Hii space left is just %f gb, and the data base is %s" %(0.98, "mysql"))
print("Hii space left is just %d gb, and the data base is %s" %(0.98, "mysql"))

print(True and True)
print(False and False)
print(bool([]))
print(bool([1, 2, 3]))
print(bool("Hello"))
print(bool(""))

x = "234"
y = float(x)
bool(x)
bool(y)
print(type(x))
print(type(y))
print(bool(x))

from datetime import datetime, date, time
td = datetime(1986, 12, 1, 1, 30)
print(td)
print(td.date())
print(td.day)
print(td.time())
print(td.year)

tt = datetime.strptime("198599", "%Y%m%d")
print(tt)
datetime(1989, 1, 2, 3, 29)
tf_new = td.replace(hour = 0, minute = 0, second = 0)
print(tf_new)

def return_float(x):
    try:
        return float(x)
    except:
        return x
print(return_float('4.55'))
print(return_float("dddd"))


a = ["a", "b", "a", "d"]
a.count("a")

countries = ["usa", "india", "pakistan", "afghanistan"]
print(countries)
print(len(countries))
y = countries.extend(["britian", "canada", "turkey"])
z = countries.sort(key = len)
print(y)

import bisect
b = [3, 4, 5, 5, 6, 5]
b.sort()
print(b)

x = bisect.bisect(b, 2)
print(x)
