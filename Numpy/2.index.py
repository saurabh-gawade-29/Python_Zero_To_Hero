import numpy as np

#! Indexing in Numpy Array
#* Get the first element from the following array:
arr = np.array([1, 2, 3, 4])
print(arr[0])
print(arr[1])
print(arr[-1])
print(arr[-4])
# print(arr[5]) #! index 5 is out of bounds for axis 0 with size 4

#! I Want to add two elements in array
print(arr[2] + arr[3], "Sum")


#! Access 2-D Arrays
twoarr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', twoarr[0, 1])

#! Negative Indexing
# print('Last element from 2nd dim: ', arr[1, -1])

#! Access 3-D Array
threearr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(threearr[0, 1, 2])