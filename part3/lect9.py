import pandas as pd 
series1 = pd.Series([10,20,30,40])
series1 = pd.Series([10,20,30,40],
                    index=['aya','nadeen',
                           'leen','rana'])
series1 = pd.Series({'aya':10,'nadeen':20,
                     'leen':30,'rana':40})
series1 = pd.Series({'aya':10,'nadeen':20,
                     'leen':30,'rana':40},
                    dtype=float)
print(series1)
