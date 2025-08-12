import pandas as pd 
import numpy as np
students = pd.read_csv('./part3/students.csv')
courses= pd.read_csv('./part3/students_courses.csv')
print(courses)
students_courses = pd.merge(students,courses,how="inner",on="Id")
students_courses = pd.merge(students,courses,how="left",on="Id")
students_courses = pd.merge(students,courses,how="right",on="Id")
students_courses = pd.merge(students,courses,how="outer",on="Id")
print(students_courses)
