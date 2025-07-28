ids = [202201,202202,202203,202204]
names = ['Aya Taweel','Nadeen Qoqas',
            'Rana Hindi','Leen Malkawi']
ages = [20,21,19,22]
students = dict(zip(ids,list(zip(names,ages))))
print(students)
"""
students_emails={id:[name
                     ,f"{name.lower().replace(" ",".")}@uop.edu.jo"] 
                 for id,name in students.items()}
print(students_emails)
"""