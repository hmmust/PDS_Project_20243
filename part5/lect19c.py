import json
#dump : convert Python  object->file
# object: dict or list(of dicts)
rana_data = {'name':'Rana Alhendi',
             'age':21, 'major':'DSAI',
             'graduated':False,"salary":None}
f = open("./part5/rana.json",mode="wt")
json.dump(rana_data,f)
f.close()


# list of dictionaries
student_data = [{'name':'Rana Alhendi','age':21},
                {'name':'Aya Altaweel','age':20}]

with open("./part5/students.json",mode="wt") as f:
    json.dump(student_data,f)
