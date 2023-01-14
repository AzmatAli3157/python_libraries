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

arr3d1 = np.arange(144).reshape(9,4,4) #(depth, rows and columns)
print(arr3d1)
"""
OUTPUT
array([[[  0,   1,   2,   3],
        [  4,   5,   6,   7],
        [  8,   9,  10,  11],
        [ 12,  13,  14,  15]],

       [[ 16,  17,  18,  19],
        [ 20,  21,  22,  23],
        [ 24,  25,  26,  27],
        [ 28,  29,  30,  31]],

       [[ 32,  33,  34,  35],
        [ 36,  37,  38,  39],
        [ 40,  41,  42,  43],
        [ 44,  45,  46,  47]],

       [[ 48,  49,  50,  51],
        [ 52,  53,  54,  55],
        [ 56,  57,  58,  59],
        [ 60,  61,  62,  63]],

       [[ 64,  65,  66,  67],
        [ 68,  69,  70,  71],
        [ 72,  73,  74,  75],
        [ 76,  77,  78,  79]],

       [[ 80,  81,  82,  83],
        [ 84,  85,  86,  87],
        [ 88,  89,  90,  91],
        [ 92,  93,  94,  95]],

       [[ 96,  97,  98,  99],
        [100, 101, 102, 103],
        [104, 105, 106, 107],
        [108, 109, 110, 111]],

       [[112, 113, 114, 115],
        [116, 117, 118, 119],
        [120, 121, 122, 123],
        [124, 125, 126, 127]],

       [[128, 129, 130, 131],
        [132, 133, 134, 135],
        [136, 137, 138, 139],
        [140, 141, 142, 143]]])


"""
#Now you can direct use calculations with numpy array like Addition, Multiplications or division directly
#for example

#arr2d = np.arange(20).reshape(1,20)
#arr2d = np.arange(20).reshape(20,1)
#arr2d = np.arange(20).reshape(4,5)
arr2d = np.arange(20).reshape(5,4)
# arr2d = np.arange(20).reshape(10,2)
# arr2d = np.arange(20).reshape(2,10)
print(arr2d)
""""
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [16, 17, 18, 19]])

"""


arr2d * 10
"""
output

array([[  0,  10,  20,  30],
       [ 40,  50,  60,  70],
       [ 80,  90, 100, 110],
       [120, 130, 140, 150],
       [160, 170, 180, 190]])


"""