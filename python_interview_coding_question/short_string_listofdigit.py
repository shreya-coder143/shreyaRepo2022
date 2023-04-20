l1=["1.2","1.1.2", "1.0.0", "1.3.3","201.2.3","120.1","1.0.12", "1.0.2"]
l1.sort(key=lambda x : tuple([int(y) for y in x.split(".")]))
print(l1)