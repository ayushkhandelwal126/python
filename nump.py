 import numpy as np

 arr = np.array([5,9,6,3,12],int) ##or arr = np.array([5,9,6,3,12])

 print(arr)
 print(type(arr))
 arr = np.array(12)
 print(arr)
 arr = np.array([[1,2,3],[4,5,6]])
 print(arr)
 arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
 print(arr)
 a = np.array(42)
 b = np.array([1, 2, 3, 4, 5])
 c = np.array([[1, 2, 3], [4, 5, 6]])
 d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

 print(a.ndim)
 print(b.ndim)
 print(c.ndim)
 print(d.ndim)
 arr = np.array([1], ndmin=5)

 print(arr)
 print('number of dimensions :', arr.ndim)
 arr = np.array([1, 2, 3, 4])

 print(arr[3])
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st dim: ', arr[1, 1])

