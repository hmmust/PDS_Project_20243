import pandas as pd
import json
students = pd.read_csv("./part3/students.csv")
print(json.loads(students[students.Id==20207].to_json(orient="records")))
print(json.loads(students[students.Major=='DS'].to_json(orient="records")))
print(list(students['Major'].unique()))
print(list(students['Major'].value_counts().index))
print(list(set(students['Major'])))
