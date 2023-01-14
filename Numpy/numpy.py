#Numpy
"""
What does Numpy means and what are Numpy can do
1. Numerical Python
2. Numerical Array
3. Fastest
4. Vectorized Operation
5 Contigious Memory
6. Numpy is an array
"""
#import numpy as np
import numpy as np
x = np.array([22,33,44,55])
print(x)
print(x.size)
print(x.shape)
print(x.ndim)

####
arr1d = np.arange(10)
print(arr1d)
#Output: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

arr2d = np.array([[1,2,3,4],[11,22,33,44],[111,222,333,444],[1111,2222,3333,4444]])
print(arr2d)
#output: 
"""
array([[   1,    2,    3],
       [  11,   22,   33],
       [ 111,  222,  333],
       [1111, 2222, 3333]])

"""
arr3d = np.arange(64).reshape(4,4,4)# (depth, row, colums)
                                    # (matrixnum, row, col)
print(arr3d)
"""
array([[[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11],
        [12, 13, 14, 15]],

       [[16, 17, 18, 19],
        [20, 21, 22, 23],
        [24, 25, 26, 27],
        [28, 29, 30, 31]],

       [[32, 33, 34, 35],
        [36, 37, 38, 39],
        [40, 41, 42, 43],
        [44, 45, 46, 47]],

       [[48, 49, 50, 51],
        [52, 53, 54, 55],
        [56, 57, 58, 59],
        [60, 61, 62, 63]]])

"""