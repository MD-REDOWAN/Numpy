
# check Dimension

import numpy as np

a = np.array(20)
b = np.array([1, 2, 3])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Output: 
"""
0
1
2
3
"""


print("------------------------------------------------------")

# Access 1D array by indexing

import numpy as np

arr1 = np.array([1,2,3,4,5])

print(arr1[1])

print("-------------------------------------")


# Access 2D arrays by indexing

import numpy as np

arr2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('3rd element on 1st row:', arr2[0, 2])

print('2nd element on 2 row :', arr2[1,1])

print("----------------------------------------------")


# 3D dimension array access by indexing

import numpy as np

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr3)

print("--------------------------------------")

print('2nd element of the 3rd row', arr3[1,1,2])
