import pandas as pd 
import numpy as np
students = pd.read_csv('./part3/students.csv')
courses= pd.read_csv('./part3/students_courses.csv')
students_courses = pd.merge(students,courses,how="inner",on="Id")


print(students[students['Major']=='DS'])
print(students[students['GPA']>=3])
print(students[  ( (students['Major']=='DS') &  (students['GPA']>=3) )  ])
print(students[  ( (students['Major'].isin(["DS","CS"])) &  (students['GPA']>=3) )  ])

# select median age in each department (group by)
print(students.groupby(by='Major')['Age'].median())

# select maximum GPA on each major (group by)
print(students.groupby(by='Major')['GPA'].max())

# select median GPA for each deparment and ages (group by )

print(students.groupby(by=['Major','Age'])['GPA'].median()) # single aggregation

print(students.groupby(by=['Major','Age'])['GPA'].agg(['median','max','count']))
print(students.groupby(by=['Major','Age'])['GPA'].agg([np.median,np.max]))
print(students.groupby(by=['Major','Age'])['GPA'].aggregate([np.median,np.max]))

students_by_major= students.groupby(by=['Major','Age']) # dataframe

print(students_by_major['GPA'].agg([np.median,np.max]))
print(students_by_major[['GPA','Age']].aggregate([np.median,np.max]))
print(students_by_major['GPA'].agg(['median','max','count']))
students_by_major_counts= students_by_major['GPA'].agg(['count'])
print(students_by_major_counts)
#print(students_by_major_counts['count'])
#print(students_by_major_counts.loc[["DS"],:])



