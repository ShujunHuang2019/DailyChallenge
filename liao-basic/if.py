age = 5
if age >= 18:
    print("your age is", age)
    print("adult")
elif age >= 6:
    print("your age is", age)
    print("teenager")
else:
    print("your age is", age)
    print("kid")

s = input("birthdate: ")
s = int(s)
if s < 2000:
    print("before 00")
else:
    print("after 00")
