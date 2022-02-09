# len() Method
# Count element in tuple
t1 = (1, 2, 3, 4, 5, 9)

# index : 0-5
# basic math: 6
# print(len(t1))

# max() method
# max value return in tuple
# print(max(t1))

# max() method in string
t2 = ('saurabh', 'komal', 'shubham', 'abhay')
# print(max(t2))

ab = (1, 1.5, "1", [3, 4], (3, 4))
# print(max(ab))
# Output: TypeError: '>' not supported between instances of 'str' and 'float'

ab2 = ([3, 4], (3, 4))
# print(max(ab2))

# min() Method
# min value return in tuple
t3 = (1, 2, 3, 4, 5, 9)
# print(min(t3))

t4 = ('saurabh', 'komal', 'shubham', 'abhay')
# print(min(t4))

# Index() Method
t5 = (1, 3, 5, 7, 2)
indexValue = t5.index(5)
# print(indexValue)

# The Count() function
# count() Method

t6 = (1, 2, 3, 4, 5, 1, 2, 4, 5, 1, 2, 4, 5, 5)
countValue = t6.count(5)
# print(countValue)

# tuple() Method

# empty tuple
x = tuple()

# tuple from list
y = tuple([1, 2, 3])

# Creating tuple from string
z = tuple("hello")

# Creating a tuple from keys of dir
w = tuple({1: "1", 2: "2", 'abhay': "jo_darta_nahi"})
print(w)

