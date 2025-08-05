import pandas as pd 
import numpy as np
students = pd.DataFrame({
    'id':np.array([10,20,30,40],dtype=int),
                         'name':['aya','nadeen',
                      'leen','rana']}
                        ) #dict of columns
students = pd.DataFrame([[10,'aya'],
                         [20,'nadeen'],
                         [30,'leen'],
                         [40,'rana']],
                        columns=['id','name'])
students.columns=['stdid','fullname']
print(students)
print(students.columns)