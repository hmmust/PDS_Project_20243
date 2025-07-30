import numpy as np

arr1 = np.array([10,20,30,41])
print(arr1,arr1.ndim,arr1.shape)
print(arr1[0],arr1[-1]) #indexing
print(arr1[0:2]) #slicing
print(arr1[arr1%2==0]) # advanced indexing
print(arr1[[0,1,0,1,0]]) # advanced indexing

arr2 = np.array([[10,20],[30,40]])
#print(arr2,arr2.ndim,arr2.shape)