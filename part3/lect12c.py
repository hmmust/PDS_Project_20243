import pandas as pd 
import numpy as np
students = pd.read_csv('./part3/students.csv')
print(students.Major.value_counts())
students.Major.replace({' SE':'SE','DSS':'DS'}
                       ,inplace=True)

print(students.Year.value_counts(dropna=False))
students.Year.fillna(students.Year.median(),inplace=True)
students.Year= students.Year.astype(np.int16)
print(students.Year.value_counts(dropna=False))

print(students.GPA.value_counts(dropna=False))



