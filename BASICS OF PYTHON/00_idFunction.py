a = 5
b = 10
print(id(a))
print(id(b))
a, b = b, a
print(id(a))
print(id(b))
print(a, b)