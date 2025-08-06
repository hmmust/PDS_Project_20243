import pandas as pd 
import numpy as np
students = pd.read_csv('./part3/students.csv')
print(students.count())
print(students.loc[:,['Age','Year','GPA']].mean())
print(students['Age'].mean())
print(students.Age.mean())
print(students.Age.min())
print(students.Age.max())
ages_median = students.Age.median()
print(students.Year.value_counts(dropna=False))


