import json
import pandas as pd
students_file= './part5/students.json'
with open(students_file) as f:
    students= json.load(f)
students = pd.DataFrame(students)
print(students)
