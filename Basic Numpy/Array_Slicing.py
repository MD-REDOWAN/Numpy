
# Slicing in python means taling elements from one given index to another given index

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr[3:7]) # 7 index take before index

print("-------------------------------------")


# Slice elements from index 3 to the end 

print(arr[3:])

print("-------------------------------------")


# Slice elements from the beginnig to 5 index

print(arr[:5])

print("--------------------------------------")


# Negative Slicing started from last index

print(arr[-3:-1]) # Output: [7, 8]

print("--------------------------------------")


# Slice using Step take element index 1-5 and write idex 0 and 3

print(arr[1:7:3]) # Output: [2 5]

print("---------------------------------------")



# Return every other element from the entire array:

print(arr[::2])

# Output: [[1 3 5 7]

print("----------------------------------------")

# Slicing 2D Arrays


import numpy as np

arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr2[0,1:4])

# Output: [2 3 4]

print(arr2[1, 1:4])

# Output: [7 8 9]

print("-------------------------------------------")

print(arr2[0:3, 1:4])

# Output: 
