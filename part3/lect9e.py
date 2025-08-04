import pandas as pd 
series1 = pd.Series([10,20,30,40],dtype=float)
series2 = pd.Series(['aya','nadeen',
                     'leen','rana'],dtype=str)
students = pd.DataFrame({'id':series1,
                         'name':series2}
                        )
print(students)