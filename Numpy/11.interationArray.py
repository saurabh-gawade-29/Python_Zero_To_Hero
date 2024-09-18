
#! Iterate on the elements of the following 1-D array:
import numpy as np
arr = np.array([1, 2, 3])
for x in arr:
  print(x)


#! Iterating 2-D Arrays
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)

#! How to visit each element in above example?
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  for y in x:
    print(y)
    
#! Iterating 3-D Arrays
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  print(x)
  
#! Want to visit each element in nested array
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  for y in x:
    for z in y:
      print(z)
      
#! Iterating Arrays Using nditer()
#* Iterating on Each Scalar Element
import numpy as np
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)