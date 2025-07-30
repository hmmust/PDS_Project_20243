import numpy as np

arr1 = np.array([10,20,30,41])
arr2 = np.array([[10.0,20],[30,40]])
arr3 = np.array(True)
print(arr1.ndim, arr2.ndim, arr3.ndim)
print(arr1.shape, arr2.shape, arr3.shape)
print(type(arr1), type(arr2),type(arr3))
print(arr1.dtype, arr2.dtype, arr3.dtype)

