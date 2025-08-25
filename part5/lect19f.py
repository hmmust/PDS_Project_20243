import pandas as pd

students = pd.read_json('./part5/students.json')
students['age'] += 2
students['username']= [ s.lower().replace(" ",".")
                    for s in students['name']]
print(students)
students.to_json('./part5/students_filtered.json',
                 orient='records')

