
#! Reshape From 1-D to 2-D
'''
Convert the following 1-D array with 12 elements into a 2-D array.
The outermost dimension will have 4 arrays, each with 3 elements:
'''

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

#! Reshape From 1-D to 3-D
'''
Convert the following 1-D array with 12 elements into a 3-D array.
The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:
'''
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)