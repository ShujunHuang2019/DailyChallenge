### https://www.liaoxuefeng.com/wiki/1016959663602400/1017623135437088

import os
os.name

os.path.abspath(".")
os.path.join(os.path.abspath("."), "testdir")

os.mkdir(os.path.join(os.path.abspath("."), "testdir"))
os.rmdir(os.path.join(os.path.abspath("."), "testdir"))

os.mkdir('/Users/shujunhuang/Workspaces/python-training/testdir')
os.rmdir('/Users/shujunhuang/Workspaces/python-training/testdir')

os.path.split('/Users/shujunhuang/Workspaces/python-training/liao-basic')
os.path.split('/Users/shujunhuang/Workspaces/python-training/liao-basic/test.txt')

## to get the extension of the file
os.path.splitext('/Users/shujunhuang/Workspaces/python-training/liao-basic/test.txt')

cd /Users/shujunhuang/Workspaces/python-training
os.path.abspath(".")

os.rename("./liao-basic/test.txt", "./liao-basic/test_os.txt")
os.rename("./liao-basic/test_os.txt", "./liao-basic/test.txt")
os.remove("./liao-basic/os_test.py")

os.listdir(".")
os.listdir("./liao-basic")
os.path.isdir(".")


[x for x in os.listdir(".") if os.path.isdir(x)]

[x for x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x) == ".py"]
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

import os
os.listdir(".")
os.path.abspath(".")
os.path.join(os.path.abspath("."), "other_tutorials")
os.mkdir(os.path.join(os.path.abspath("."), "other_tutorials"))

cd /Users/shujunhuang/Workspaces/python-training/other_tutorials
os.listdir(".")
