import pandas as pd 
series1 = pd.Series([10,20,30,40],
                    index=['aya','nadeen',
                           'leen','rana'],dtype=float)
print(series1['leen'])
print(series1[0:2])
print(series1.dtype)
print(series1.sum())
print(series1.mean())
print(series1.median())
#series1.reset_index(inplace=True)
print(series1[['leen','rana']])





