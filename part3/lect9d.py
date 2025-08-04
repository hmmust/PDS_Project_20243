import pandas as pd 
import numpy as np
series1 = pd.Series([10,20,30,40],
                    index=['aya','nadeen',
                           'leen','rana'],dtype=float)
series2 = pd.Series([e*e for e in series1])
print(series2)