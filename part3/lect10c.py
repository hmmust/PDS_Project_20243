import pandas as pd 
import numpy as np
students = pd.read_csv('./part3/students.csv')
print(students.head())
print(students.tail())
print(students.describe())
print(students.describe(include=['object']))
print(students.dtypes)
print(students.info())


