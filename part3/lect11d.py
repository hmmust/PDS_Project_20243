import pandas as pd 
import numpy as np
students = pd.read_csv('./part3/students.csv')
students['Birthyear']= 2025-students['Age']
print(students.loc[:,['Age','Year','GPA']].cov())
print(students['Age'].corr(students['GPA'] ))
print(students['Age'].corr(students['Birthyear'] ))
print(students['Age'].cov(students['Birthyear'] ))





