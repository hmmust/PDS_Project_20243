import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot
students = pd.read_csv('./part3/students.csv',
                       names=['id','name','major','age','year','GPA'],
                       dtype={'Age':np.int16 })

students.age.value_counts().plot.bar()
print(students)