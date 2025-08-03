import numpy as np
arr1 = np.array([15,20,0,10,15,16])
arr2= [True, True, False,False,False,True]
f1 = arr1==20
f2 = arr1%2==0
print(f2)
print(arr1[f2])
print(arr1[[True,True,False,False,False,True]])


