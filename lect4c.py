ids = [202201,202202,202203,202204]
names = ['Aya Taweel','Nadeen Qoqas',
            'Rana Hindi','Leen Malkawi']
students = dict(zip(ids,names))

students_emails={id:[name
                     ,f"{name.lower().replace(" ",".")}@uop.edu.jo"] 
                 for id,name in students.items()}
print(students_emails)
