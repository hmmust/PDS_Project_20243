import json
#
rana_text = '{"name": "Rana Alhendi", "age": 21, "major": "DSAI", "graduated": false, "salary": null}'
rana= json.loads(rana_text)
print(type(rana))

students_text= '[{"name": "Rana Alhendi", "age": 21}, {"name": "Aya Altaweel", "age": 20}]'
students = json.loads(students_text)
print(type(students))
