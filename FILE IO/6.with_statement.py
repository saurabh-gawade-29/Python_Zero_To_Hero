# no need to write f.close() while using with statement
with open("sample.txt") as f:
    data = f.read()
print(data)

