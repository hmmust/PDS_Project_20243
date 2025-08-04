import pandas as pd 
import numpy as np
series1 = pd.Series([10,20,30,40],
                    index=['aya','nadeen',
                           'leen','rana'],dtype=float)
series1 = pd.Series(np.array([10,20,30,40],dtype=float),
                    index=['aya','nadeen',
                           'leen','rana'])

print(series1.dtype)
print(series1.ndim)
print(series1.empty)
print(series1.values)
print(series1.head(2))
print(series1.tail(1))








