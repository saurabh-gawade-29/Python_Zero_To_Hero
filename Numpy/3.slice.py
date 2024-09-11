import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
# Slice elements from index 1 to index 5 from the following array:
print(arr[1:5])
# Slice elements from index 4 to the end of the array:
print(arr[4:])
# Slice elements from index 4 to the end of the array:
print(arr[:4])
# Slice from the index 3 from the end to index 1 from the end:
print(arr[-3:-1])
#TODO: STEP
# Use the step value to determine the step of the slicing:
print(arr[1:5:2])
# Return every other element from the entire array:
print(arr[::2])