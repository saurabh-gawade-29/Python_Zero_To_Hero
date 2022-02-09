# f is variable  and we use open function for read the file
f = open("sample.txt", "r")
data = f.read()
print(data)

# for this o/p comment above f.read()
# we can specify the number of char in read function
text = f.read(10)
print(text)
# op: This file

# TODO: close is important coz by using close() file is use by another person
f.close()