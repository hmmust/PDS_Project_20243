import numpy as np
arr1 = np.array([15,20,0,10,15,16])
arr2= [0,1,1,1,-1]
arr2= [-2,-1]
s1 = np.where(arr1%2==0)
print(s1)
print(arr1[s1])
print(arr1[arr2])
print(arr1[[0,1,1]])





