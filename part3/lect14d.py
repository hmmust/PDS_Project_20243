import pandas as pd 
import numpy as np
students = pd.read_csv('./part3/students.csv')
students.Major = pd.Categorical(students.Major,
                                categories=[' SE','CS', 'DS','VR', 'IS'])

# mapping  cat -> number
print(students.info())
print(students.Major.cat.categories)
#students.Major= students.Major.cat.remove_categories("DSS")
print(students)

# scikit-learn -> preprocessing -> labeling (LabelEncoder) -> CS->0, DS-1