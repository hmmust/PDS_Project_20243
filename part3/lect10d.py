import pandas as pd 
import numpy as np
students = pd.read_csv('./part3/students.csv')
print(students['Id'])
#del students['Id']
students.pop('Id')
students['birthdyear'] = 2025-students['Age']
students['maried']= False
students['FirstName']= [ s.split(' ')[0] for s in students.Name]
students['LastName']= [ s.split(' ')[-1] for s in students.Name]
students.pop('Name')
#students['Year'] = students['Year'].astype(np.int16)
students['Age'] = students['Age'].astype(np.int16)

print(students)
print(students.dtypes)

#print(students.Major)
