#TODO: pip install numpy
import numpy as np
'''
NumPy is a Python library.
NumPy is used for working with arrays.
NumPy is short for "Numerical Python".
'''

# NumPy Creating Arrays - LIST
listarr = np.array([1, 2, 3, 4, 5])
print(listarr)
print(type(listarr))

# Use a tuple to create a NumPy array:
# import numpy as np
tuparrr = np.array((1, 2, 3, 4, 5))
print(tuparrr)

'''
Dimensions in Arrays
A dimension in arrays is one level of array depth (nested arrays).
'''

# 0-D Arrays
# import numpy as np
zeroarr = np.array(42)
print(zeroarr, "0-D Array")

'''
1-D Arrays
An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
These are the most common and basic arrays.
'''
# import numpy as np
onearr = np.array([1, 2, 3, 4, 5])
print(onearr, "1-D Array")

'''
2-D Arrays
An array that has 1-D arrays as its elements is called a 2-D array.
These are often used to represent matrix or 2nd order tensors.
'''
# import numpy as np
twoarr = np.array([[1, 2, 3], [4, 5, 6]])
print(twoarr, "2-D Array")

# 3-D arrays
'''
An array that has 2-D arrays (matrices) as its elements is called 3-D array.
These are often used to represent a 3rd order tensor.
'''
# import numpy as np
threearr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(threearr, "3-D Array")
