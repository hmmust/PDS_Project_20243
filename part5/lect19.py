import json
#dumps : convert Python  object->json
# object: dict or list(of dicts)
rana_data = {'name':'Rana Alhendi',
             'age':21, 'major':'DSAI',
             'graduated':False,"salary":None}
rana_json = json.dumps(rana_data)
print(type(rana_json))

# list of dictionaries
student_data = [{'name':'Rana Alhendi','age':21},
                {'name':'Aya Altaweel','age':20}]
student_json = json.dumps(student_data)
print(student_json)
