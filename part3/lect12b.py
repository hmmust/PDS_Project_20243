import pandas as pd 
import numpy as np
students = pd.read_csv('./part3/students.csv')
print(students.isnull().sum())
print(students.isna().sum())

# replace with 2008
#students.Year.fillna(2008,inplace=True)
#students.Year.replace({np.nan:2008},inplace=True)

# replace with median
#students.Year.fillna( students.Year.median(),inplace=True) #2017
#students.Year.replace({np.nan:students.Year.median()},inplace=True)

# replace with next or previous row value
#students.Year.fillna( method='ffill' ,inplace=True) 
#students.Year.fillna( method='bfill' ,inplace=True) 
#students.Year.bfill(inplace=True)
#students.Year.ffill(inplace=True)

# drop rows with null values
#students.dropna(inplace=True)

# drop columns with null values
students.dropna(axis=1, inplace=True)

print(students)
