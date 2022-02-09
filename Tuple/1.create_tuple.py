# tuples are immutable
# we cannot change the element of tuple
# Creating a tuple

# empty tuple
a = ()

# integer tuple
b = (1, 2, 3, 4, 5)

# number tuple
c = (1, 2, 3.5, 4.5, 5)

# char tuple
d = ('a', 'b', 'c', 'd')

# string tuple
e = ("one", "two", "three")
# print(a)

# You can also create Empty tuple as
f = tuple()
# print(f)

# tuple with single value
# g = (3)
# ^
# it will store a value as integer

# to solve this problem we need to add " , " in the tuple
g = (3, )
# or
g = 3,
# print(g)
# print(type(g))

longtuple = (
    1, 2, 3,
    4, 5, 6
)
# print(longtuple)

# nested tuple
nestedTuple = (1, 2, (3, 4), 5)

# creating a tuple from existing sequence
t1 = tuple("SAURABH")
# output: ('S', 'A', 'U', 'R', 'A', 'B', 'H')

# typecasting:

l1 = [1, 2, 3]
t2 = tuple(l1)

print(t2)
print(type(t2))
# output: (1, 2, 3)