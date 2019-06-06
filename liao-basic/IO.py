f = open("test1.txt", "r")
f.read()

with open("test1.txt", "r") as f:
	print(f.read())


for line in f.readlines():
	print(line.strip())



with open('test1.txt', 'w') as f:
    f.write('Good evening!')