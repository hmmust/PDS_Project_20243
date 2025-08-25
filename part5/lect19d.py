import json
#
rana_file = './part5/rana.json'
f= open(rana_file,mode="rt")
rana= json.load(f)
print(rana)


students_file= './part5/students.json'
with open(students_file) as f:
    students= json.load(f)
print(students[0]['age'])
