import numpy as np

arr1 = np.array([1, 2, 3, 4]) #int64 
arr2 = np.array(['apple', 'banana', 'cherry']) #<U6 = unicode with max char length 6
#! Create an array with data type string:
arr3 = np.array([1, 2, 3, 4], dtype='S')

print(arr1.dtype)
print(arr2.dtype)
print(arr3)
print(arr3.dtype)
'''
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''