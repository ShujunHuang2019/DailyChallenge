[x for x in os.listdir(".") if os.path.isdir(x)]

[x for x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x) == ".py"]
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']